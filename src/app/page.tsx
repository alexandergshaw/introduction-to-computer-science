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
      <header className="mb-10 overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-600 via-violet-700 to-purple-800 p-8 shadow-2xl shadow-indigo-900/60 ring-1 ring-white/10 sm:p-10">
        {/* Top row: course label + progress pill */}
        <div className="flex flex-wrap items-start justify-between gap-6">
          <div>
            <p className="text-xs font-bold uppercase tracking-widest text-indigo-200">
              Introduction to Computer Science
            </p>
            <h1 className="mt-2 text-4xl font-black tracking-tight text-white sm:text-5xl">
              Student Portfolio
            </h1>
            <p className="mt-3 max-w-md text-indigo-200">
              Complete each module in order — every assignment you finish unlocks the next.
            </p>
          </div>

          {/* Progress badge */}
          <div className="flex flex-col items-center gap-2 rounded-2xl bg-white/10 px-6 py-4 ring-1 ring-white/20 backdrop-blur-sm">
            <span className="text-4xl font-black text-white">
              {completedCount}
              <span className="text-xl font-semibold text-indigo-200"> / {statuses.length}</span>
            </span>
            <span className="text-xs font-semibold uppercase tracking-widest text-indigo-200">
              Modules Completed
            </span>
          </div>
        </div>

        {/* Progress bar */}
        <div className="mt-8">
          <div className="mb-2 flex items-center justify-between text-xs font-semibold text-indigo-200">
            <span>Overall Progress</span>
            <span>{progressPercent}%</span>
          </div>
          <div className="h-2.5 w-full overflow-hidden rounded-full bg-white/20">
            <div
              className="h-full rounded-full bg-gradient-to-r from-emerald-400 to-teal-300 transition-all duration-700"
              style={{ width: `${progressPercent}%` }}
            />
          </div>
        </div>

        {/* Legend */}
        <div className="mt-5 flex flex-wrap gap-4 text-xs font-semibold">
          <span className="flex items-center gap-1.5 text-emerald-300">
            <span className="inline-block h-2.5 w-2.5 rounded-full bg-emerald-400" />
            Completed
          </span>
          <span className="flex items-center gap-1.5 text-amber-300">
            <span className="inline-block h-2.5 w-2.5 rounded-full bg-amber-400" />
            In Progress
          </span>
          <span className="flex items-center gap-1.5 text-slate-300">
            <span className="inline-block h-2.5 w-2.5 rounded-full bg-slate-400" />
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
