import { promises as fs } from "node:fs";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { marked } from "marked";
import { moduleDefinitions, type ModuleType } from "../components/modules";
import type { AssignmentStatus } from "../components/statusStyles";

const projectRoot = process.cwd();
const assignmentsDir = path.join(projectRoot, "assignments");

export type AssignmentStatusInfo = {
  slug: string;
  week: number;
  title: string;
  type: ModuleType;
  completed: boolean;
  unlocked: boolean;
  status: AssignmentStatus;
};

function toStatus(completed: boolean, unlocked: boolean): AssignmentStatus {
  // A module stays locked until everything before it passes — even if its own
  // tests happen to pass.
  if (!unlocked) return "locked";
  return completed ? "completed" : "in-progress";
}

// ── Python detection ──────────────────────────────────────────────────────────
// Resolve a working Python launcher once. `undefined` = not checked yet,
// `null` = none available.
let pythonCmd: string[] | null | undefined;
function getPythonCmd(): string[] | null {
  if (pythonCmd !== undefined) return pythonCmd;
  for (const candidate of [["python"], ["py", "-3"], ["python3"]]) {
    try {
      execFileSync(candidate[0], [...candidate.slice(1), "--version"], { stdio: "ignore" });
      pythonCmd = candidate;
      return pythonCmd;
    } catch {
      // try the next candidate
    }
  }
  pythonCmd = null;
  return null;
}

// A module counts as complete only when its unit tests pass (pytest exit 0).
// If Python isn't available (e.g. a Node-only build), fall back to treating the
// shipped solutions as passing so the reference site still renders.
function assignmentTestsPass(slug: string): boolean {
  const py = getPythonCmd();
  if (!py) return true;
  try {
    execFileSync(py[0], [...py.slice(1), "-m", "pytest", path.posix.join("assignments", slug), "-q"], {
      cwd: projectRoot,
      stdio: "ignore",
    });
    return true;
  } catch {
    return false;
  }
}

export async function getAllAssignmentSlugs(): Promise<string[]> {
  const entries = await fs.readdir(assignmentsDir, { withFileTypes: true });
  return entries.filter((entry) => entry.isDirectory()).map((entry) => entry.name);
}

/**
 * Determine each module's status. A module is "completed" when its unit tests
 * pass; modules unlock sequentially (each completed module unlocks the next).
 * Memoized so pytest runs once per server process / build, not per request.
 */
let statusesPromise: Promise<AssignmentStatusInfo[]> | null = null;
export function loadAssignmentStatuses(): Promise<AssignmentStatusInfo[]> {
  if (!statusesPromise) statusesPromise = computeStatuses();
  return statusesPromise;
}

async function computeStatuses(): Promise<AssignmentStatusInfo[]> {
  const directoryNames = await getAllAssignmentSlugs();

  const definitionMap = new Map(moduleDefinitions.map((item) => [item.slug, item]));
  const orderMap = new Map(moduleDefinitions.map((item, index) => [item.slug, index]));

  const discovered = directoryNames
    .map(
      (slug) =>
        definitionMap.get(slug) ?? {
          slug,
          week: Number.MAX_SAFE_INTEGER,
          title: slug,
          type: "assignment" as const,
        },
    )
    .sort((a, b) => {
      const aOrder = orderMap.get(a.slug);
      const bOrder = orderMap.get(b.slug);
      if (aOrder !== undefined && bOrder !== undefined) return aOrder - bOrder;
      if (aOrder !== undefined) return -1;
      if (bOrder !== undefined) return 1;
      return a.slug.localeCompare(b.slug);
    });

  const baseStatuses = discovered.map((moduleInfo) => ({
    slug: moduleInfo.slug,
    week: moduleInfo.week,
    title: moduleInfo.title,
    type: moduleInfo.type,
    completed: assignmentTestsPass(moduleInfo.slug),
  }));

  let shouldUnlockNext = true;
  return baseStatuses.map((moduleStatus) => {
    const unlocked = shouldUnlockNext;
    if (shouldUnlockNext) shouldUnlockNext = moduleStatus.completed;
    return {
      ...moduleStatus,
      unlocked,
      status: toStatus(moduleStatus.completed, unlocked),
    };
  });
}

export type AssignmentDetail = AssignmentStatusInfo & { contentHtml: string };

/** Full detail for one assignment, including its rendered INSTRUCTIONS.md. */
export async function getAssignmentDetail(slug: string): Promise<AssignmentDetail | null> {
  const statuses = await loadAssignmentStatuses();
  const info = statuses.find((item) => item.slug === slug);
  if (!info) return null;

  let markdown = "";
  try {
    markdown = await fs.readFile(path.join(assignmentsDir, slug, "INSTRUCTIONS.md"), "utf-8");
  } catch {
    markdown = "";
  }

  // Drop the leading "# Title" — the page header already shows the title.
  const body = markdown.replace(/^\s*#\s+.*(?:\r?\n)+/, "");
  const contentHtml = body ? await marked.parse(body) : "";
  return { ...info, contentHtml };
}
