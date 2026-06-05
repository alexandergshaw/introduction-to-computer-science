import type { ModuleType } from "./modules";

type AssignmentCardProps = {
  slug: string;
  week: number;
  title: string;
  type: ModuleType;
  status: "locked" | "in-progress" | "completed";
};

// ── Card container styles ────────────────────────────────────────────────────
// Each status gets its own gradient, border color, and shadow to make the
// visual state immediately obvious at a glance.
const cardStyles: Record<AssignmentCardProps["status"], string> = {
  locked:
    "border border-slate-800 bg-slate-900/40 opacity-50",
  "in-progress":
    "border border-slate-700/60 bg-slate-900/80 shadow-lg shadow-black/30 ring-1 ring-amber-400/10",
  completed:
    "border border-slate-700/60 bg-slate-900/80 shadow-lg shadow-black/30 ring-1 ring-emerald-400/10",
};

// ── Status badge styles ──────────────────────────────────────────────────────
const statusBadgeStyles: Record<AssignmentCardProps["status"], string> = {
  locked: "bg-slate-800 text-slate-500 ring-1 ring-slate-700/60",
  "in-progress": "bg-amber-500/10 text-amber-400 ring-1 ring-amber-500/25",
  completed: "bg-emerald-500/10 text-emerald-400 ring-1 ring-emerald-500/25",
};

const statusLabels: Record<AssignmentCardProps["status"], string> = {
  locked: "Locked",
  "in-progress": "In Progress",
  completed: "Completed",
};

const statusIcons: Record<AssignmentCardProps["status"], string> = {
  locked: "Locked",
  "in-progress": "In Progress",
  completed: "Completed",
};

// ── Module-type badge styles ─────────────────────────────────────────────────
// Assignments, reviews, and exams each get a distinct color so students can
// quickly see what kind of work they're looking at.
const typeBadgeStyles: Record<ModuleType, string> = {
  assignment: "bg-blue-500/10 text-blue-400 ring-1 ring-blue-500/20",
  review: "bg-sky-500/10 text-sky-400 ring-1 ring-sky-500/20",
  exam: "bg-rose-500/10 text-rose-400 ring-1 ring-rose-500/20",
};

const typeLabels: Record<ModuleType, string> = {
  assignment: "Assignment",
  review: "Review",
  exam: "Exam",
};

// ── Left-accent bar color ────────────────────────────────────────────────────
const accentBar: Record<AssignmentCardProps["status"], string> = {
  locked: "bg-slate-700",
  "in-progress": "bg-amber-400",
  completed: "bg-emerald-400",
};

export function AssignmentCard({ slug, week, title, type, status }: AssignmentCardProps) {
  return (
    <article className={`relative flex overflow-hidden rounded-xl transition-all duration-200 hover:scale-[1.012] hover:shadow-xl ${cardStyles[status]}`}>
      {/* Colored left accent bar */}
      <div className={`w-0.5 shrink-0 ${accentBar[status]}`} />

      <div className="flex flex-1 flex-col gap-3 p-5">
        {/* Top row: week + status badge */}
        <div className="flex items-center justify-between gap-2">
          <p className="text-xs font-semibold uppercase tracking-widest text-slate-500">
            Week {week}
          </p>
          <span
            className={`rounded-full px-2.5 py-0.5 text-xs font-medium ${statusBadgeStyles[status]}`}
            aria-label={`Status: ${statusLabels[status]}`}
          >
            {statusIcons[status]}
          </span>
        </div>

        {/* Title */}
        <h2 className="text-sm font-semibold leading-snug text-slate-100">{title}</h2>

        {/* Type + slug row */}
        <div className="flex flex-wrap items-center gap-2">
          <span className={`rounded-full px-2 py-0.5 text-xs font-medium ${typeBadgeStyles[type]}`}>
            {typeLabels[type]}
          </span>
          <span className="text-xs text-slate-600">{slug}</span>
        </div>

        {/* Instruction */}
        <p className="mt-auto text-xs leading-relaxed text-slate-500">
          Open{" "}
          <code className="rounded bg-slate-800 px-1.5 py-0.5 font-mono text-slate-300">
            assignments/{slug}
          </code>{" "}
          and complete{" "}
          <code className="rounded bg-slate-800 px-1.5 py-0.5 font-mono text-slate-300">
            student_work.py
          </code>
          .
        </p>
      </div>
    </article>
  );
}
