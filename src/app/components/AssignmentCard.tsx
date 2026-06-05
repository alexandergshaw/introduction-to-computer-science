import type { ModuleType } from "./modules";

type AssignmentCardProps = {
  slug: string;
  week: number;
  title: string;
  type: ModuleType;
  status: "locked" | "in-progress" | "completed";
};

const statusStyles: Record<AssignmentCardProps["status"], string> = {
  locked: "bg-zinc-100 text-zinc-500 border-zinc-200",
  "in-progress": "bg-amber-50 text-amber-700 border-amber-200",
  completed: "bg-emerald-50 text-emerald-700 border-emerald-200",
};

const statusLabels: Record<AssignmentCardProps["status"], string> = {
  locked: "Locked",
  "in-progress": "In Progress",
  completed: "Completed",
};

const typeLabels: Record<ModuleType, string> = {
  assignment: "Assignment",
  review: "Review",
  exam: "Exam",
};

export function AssignmentCard({ slug, week, title, type, status }: AssignmentCardProps) {
  return (
    <article className="rounded-xl border border-zinc-200 bg-white p-4 shadow-sm">
      <div className="mb-3 flex items-start justify-between gap-3">
        <div>
          <p className="text-xs font-semibold uppercase tracking-wide text-zinc-500">Week {week}</p>
          <h2 className="text-lg font-semibold text-zinc-900">{title}</h2>
          <p className="text-sm text-zinc-500">{typeLabels[type]} · {slug}</p>
        </div>
        <span
          className={`rounded-full border px-3 py-1 text-xs font-semibold ${statusStyles[status]}`}
          aria-label={`Status: ${statusLabels[status]}`}
        >
          {status === "completed" ? "✓ " : ""}
          {statusLabels[status]}
        </span>
      </div>
      <p className="text-sm text-zinc-600">
        Open <code className="rounded bg-zinc-100 px-1 py-0.5 text-zinc-700">assignments/{slug}</code> and
        complete <code className="rounded bg-zinc-100 px-1 py-0.5 text-zinc-700">student_work.py</code>.
      </p>
    </article>
  );
}
