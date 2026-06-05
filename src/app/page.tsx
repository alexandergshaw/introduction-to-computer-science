import { promises as fs } from "node:fs";
import path from "node:path";
import { AssignmentCard } from "./components/AssignmentCard";
import { moduleDefinitions } from "./components/modules";

type AssignmentStatus = {
  slug: string;
  week: number;
  title: string;
  type: "assignment" | "review" | "exam";
  completed: boolean;
  unlocked: boolean;
};

type BaseAssignmentStatus = Omit<AssignmentStatus, "unlocked">;

function isCompleted(slug: string, studentWork: string): boolean {
  if (slug === "assignment0") {
    const studentNameMatch = studentWork.match(/STUDENT_NAME\s*=\s*["']([^"']+)["']/);
    const studentName = studentNameMatch?.[1]?.trim() ?? "";
    return studentName.length > 0 && studentName !== "Your Name";
  }

  return /MODULE_COMPLETED\s*=\s*True\b/.test(studentWork);
}

async function loadAssignmentStatuses(): Promise<AssignmentStatus[]> {
  const assignmentsDir = path.join(process.cwd(), "assignments");
  const entries = await fs.readdir(assignmentsDir, { withFileTypes: true });

  const directoryNames = entries.filter((entry) => entry.isDirectory()).map((entry) => entry.name);

  const definitionMap = new Map(moduleDefinitions.map((item) => [item.slug, item]));
  const orderMap = new Map(moduleDefinitions.map((item, index) => [item.slug, index]));
  const discovered = directoryNames
    .map((slug) => definitionMap.get(slug) ?? { slug, week: Number.MAX_SAFE_INTEGER, title: slug, type: "assignment" as const })
    .sort((a, b) => {
      const aOrder = orderMap.get(a.slug);
      const bOrder = orderMap.get(b.slug);

      if (aOrder !== undefined && bOrder !== undefined) {
        return aOrder - bOrder;
      }

      if (aOrder !== undefined) {
        return -1;
      }

      if (bOrder !== undefined) {
        return 1;
      }

      return a.slug.localeCompare(b.slug);
    });

  const baseStatuses: BaseAssignmentStatus[] = await Promise.all(
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
    if (!shouldUnlockNext) {
      return { ...moduleStatus, unlocked: false };
    }

    shouldUnlockNext = moduleStatus.completed;
    return { ...moduleStatus, unlocked: true };
  });
}

export default async function Home() {
  const statuses = await loadAssignmentStatuses();
  const completedCount = statuses.filter((status) => status.completed).length;

  return (
    <main className="mx-auto min-h-screen w-full max-w-6xl px-4 py-10 sm:px-8">
      <header className="mb-8 rounded-2xl border border-zinc-200 bg-white p-6 shadow-sm">
        <p className="text-sm font-semibold uppercase tracking-wide text-zinc-500">Introduction to Computer Science</p>
        <h1 className="mt-2 text-3xl font-bold text-zinc-900">Student Portfolio Dashboard</h1>
        <p className="mt-3 text-zinc-600">
          Progress tracker for semester assignments, reviews, and exam practice modules.
        </p>
        <p className="mt-4 text-sm font-medium text-zinc-700">
          Completed: {completedCount} / {statuses.length}
        </p>
      </header>

      <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {statuses.map((status) => (
          <AssignmentCard
            key={status.slug}
            {...status}
            status={status.completed ? "completed" : status.unlocked ? "in-progress" : "locked"}
          />
        ))}
      </section>
    </main>
  );
}
