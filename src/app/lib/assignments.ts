import { promises as fs } from "node:fs";
import path from "node:path";
import { marked } from "marked";
import { moduleDefinitions, type ModuleType } from "../components/modules";
import type { AssignmentStatus } from "../components/statusStyles";

const assignmentsDir = path.join(process.cwd(), "assignments");

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
  if (completed) return "completed";
  return unlocked ? "in-progress" : "locked";
}

function isCompleted(slug: string, studentWork: string): boolean {
  if (slug === "assignment0") {
    const studentNameMatch = studentWork.match(/STUDENT_NAME\s*=\s*["']([^"']+)["']/);
    const studentName = studentNameMatch?.[1]?.trim() ?? "";
    return studentName.length > 0 && studentName !== "Your Name";
  }

  return /MODULE_COMPLETED\s*=\s*True\b/.test(studentWork);
}

export async function getAllAssignmentSlugs(): Promise<string[]> {
  const entries = await fs.readdir(assignmentsDir, { withFileTypes: true });
  return entries.filter((entry) => entry.isDirectory()).map((entry) => entry.name);
}

/**
 * Reads every assignment directory, determines completion from its
 * student_work.py, and unlocks modules sequentially (each completed module
 * unlocks the next).
 */
export async function loadAssignmentStatuses(): Promise<AssignmentStatusInfo[]> {
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

  const baseStatuses = await Promise.all(
    discovered.map(async (moduleInfo) => {
      const studentWorkPath = path.join(assignmentsDir, moduleInfo.slug, "student_work.py");
      const studentWork = await fs.readFile(studentWorkPath, "utf-8");
      return {
        slug: moduleInfo.slug,
        week: moduleInfo.week,
        title: moduleInfo.title,
        type: moduleInfo.type,
        completed: isCompleted(moduleInfo.slug, studentWork),
      };
    }),
  );

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
