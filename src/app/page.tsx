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
  const progressPercent = Math.round((completedCount / statuses.length) * 100);

  return (
    <main className="mx-auto min-h-screen w-full max-w-6xl px-4 py-10 sm:px-8">
      {/* ── Hero Header ─────────────────────────────────────────────────── */}
      <header className="relative mb-10 overflow-hidden rounded-2xl border border-slate-700/40 bg-slate-900/75 p-8 shadow-2xl shadow-black/40 backdrop-blur-sm sm:p-10">
        {/* Subtle top accent glow line */}
        <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-blue-500/70 to-transparent" />
        <div className="absolute inset-x-0 top-0 h-20 bg-gradient-to-b from-blue-600/8 to-transparent" />

        {/* Top row: course label + stats widget */}
        <div className="relative flex flex-wrap items-start justify-between gap-6">
          <div>
            <p className="text-xs font-semibold uppercase tracking-[0.18em] text-blue-400">
              Introduction to Computer Science
            </p>
            <h1 className="mt-2 text-4xl font-bold tracking-tight text-white sm:text-5xl">
              Student Portfolio
            </h1>
            <p className="mt-3 max-w-md text-sm text-slate-400">
              Complete each module in order — every assignment you finish unlocks the next.
            </p>
          </div>

          {/* Stats widget */}
          <div className="flex items-stretch divide-x divide-slate-700/60 rounded-xl border border-slate-700/50 bg-slate-800/60">
            <div className="flex flex-col items-center justify-center px-6 py-4">
              <span className="text-3xl font-bold tabular-nums text-white">{completedCount}</span>
              <span className="mt-0.5 text-xs text-slate-400">Completed</span>
            </div>
            <div className="flex flex-col items-center justify-center px-6 py-4">
              <span className="text-3xl font-bold tabular-nums text-white">{statuses.length}</span>
              <span className="mt-0.5 text-xs text-slate-400">Total</span>
            </div>
            <div className="flex flex-col items-center justify-center px-6 py-4">
              <span className="text-3xl font-bold tabular-nums text-blue-400">{progressPercent}%</span>
              <span className="mt-0.5 text-xs text-slate-400">Progress</span>
            </div>
          </div>
        </div>

        {/* Progress bar */}
        <div className="relative mt-8">
          <div className="h-1 w-full overflow-hidden rounded-full bg-slate-700/60">
            <div
              className="h-full rounded-full bg-gradient-to-r from-blue-500 to-cyan-400 transition-all duration-700"
              style={{ width: `${progressPercent}%` }}
            />
          </div>
        </div>

        {/* Legend */}
        <div className="relative mt-4 flex flex-wrap gap-5 text-xs text-slate-400">
          <span className="flex items-center gap-2">
            <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
            Completed
          </span>
          <span className="flex items-center gap-2">
            <span className="h-1.5 w-1.5 rounded-full bg-amber-400" />
            In Progress
          </span>
          <span className="flex items-center gap-2">
            <span className="h-1.5 w-1.5 rounded-full bg-slate-600" />
            Locked
          </span>
        </div>
      </header>

      {/* ── Assignment Grid ──────────────────────────────────────────────── */}
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
