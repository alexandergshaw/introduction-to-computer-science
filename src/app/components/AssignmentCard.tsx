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
    "border border-slate-700/60 bg-slate-800/50 opacity-60 shadow-sm backdrop-blur-sm",
  "in-progress":
    "border border-amber-400/40 bg-gradient-to-br from-slate-800/90 to-amber-900/30 shadow-lg shadow-amber-900/20 ring-1 ring-amber-400/20 backdrop-blur-sm",
  completed:
    "border border-emerald-400/40 bg-gradient-to-br from-slate-800/90 to-emerald-900/30 shadow-lg shadow-emerald-900/20 ring-1 ring-emerald-400/20 backdrop-blur-sm",
};

// ── Status badge styles ──────────────────────────────────────────────────────
const statusBadgeStyles: Record<AssignmentCardProps["status"], string> = {
  locked: "bg-slate-700 text-slate-400 ring-1 ring-slate-600",
  "in-progress": "bg-amber-500/20 text-amber-300 ring-1 ring-amber-400/40",
  completed: "bg-emerald-500/20 text-emerald-300 ring-1 ring-emerald-400/40",
};

const statusLabels: Record<AssignmentCardProps["status"], string> = {
  locked: "🔒 Locked",
  "in-progress": "▶ In Progress",
  completed: "✓ Completed",
};

// ── Module-type badge styles ─────────────────────────────────────────────────
// Assignments, reviews, and exams each get a distinct color so students can
// quickly see what kind of work they're looking at.
const typeBadgeStyles: Record<ModuleType, string> = {
  assignment: "bg-indigo-500/20 text-indigo-300 ring-1 ring-indigo-400/30",
  review: "bg-sky-500/20 text-sky-300 ring-1 ring-sky-400/30",
  exam: "bg-rose-500/20 text-rose-300 ring-1 ring-rose-400/30",
};

const typeLabels: Record<ModuleType, string> = {
  assignment: "Assignment",
  review: "Review",
  exam: "Exam",
};

// ── Left-accent bar color ────────────────────────────────────────────────────
const accentBar: Record<AssignmentCardProps["status"], string> = {
  locked: "bg-slate-600",
  "in-progress": "bg-gradient-to-b from-amber-400 to-amber-600",
  completed: "bg-gradient-to-b from-emerald-400 to-emerald-600",
};

export function AssignmentCard({ slug, week, title, type, status }: AssignmentCardProps) {
  return (
    <article className={`relative flex overflow-hidden rounded-2xl transition-all duration-200 hover:scale-[1.015] ${cardStyles[status]}`}>
      {/* Colored left accent bar */}
      <div className={`w-1 shrink-0 rounded-l-2xl ${accentBar[status]}`} />

      <div className="flex flex-1 flex-col gap-3 p-5">
        {/* Top row: week + status badge */}
        <div className="flex items-center justify-between gap-2">
          <p className="text-xs font-bold uppercase tracking-widest text-slate-400">
            Week {week}
          </p>
          <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ${statusBadgeStyles[status]}`}>
            {statusLabels[status]}
          </span>
        </div>

        {/* Title */}
        <h2 className="text-base font-bold leading-snug text-white">{title}</h2>

        {/* Type + slug row */}
        <div className="flex flex-wrap items-center gap-2">
          <span className={`rounded-full px-2 py-0.5 text-xs font-semibold ${typeBadgeStyles[type]}`}>
            {typeLabels[type]}
          </span>
          <span className="text-xs text-slate-500">{slug}</span>
        </div>

        {/* Instruction */}
        <p className="mt-auto text-xs leading-relaxed text-slate-400">
          Open{" "}
          <code className="rounded bg-slate-700 px-1.5 py-0.5 font-mono text-slate-200">
            assignments/{slug}
          </code>{" "}
          and complete{" "}
          <code className="rounded bg-slate-700 px-1.5 py-0.5 font-mono text-slate-200">
            student_work.py
          </code>
          .
        </p>
      </div>
    </article>
  );
}
