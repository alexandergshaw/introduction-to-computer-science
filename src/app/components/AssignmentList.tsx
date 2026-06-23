"use client";

import Link from "next/link";
import {
  statusLabels,
  typeLabels,
  type AssignmentStatus,
  type SceneAssignment,
} from "./statusStyles";

const dotColor: Record<AssignmentStatus, string> = {
  locked: "bg-slate-600",
  "in-progress": "bg-amber-400 shadow-[0_0_8px_2px] shadow-amber-400/50",
  completed: "bg-emerald-400 shadow-[0_0_8px_2px] shadow-emerald-400/50",
};

const pillColor: Record<AssignmentStatus, string> = {
  locked: "text-slate-500",
  "in-progress": "text-amber-300",
  completed: "text-emerald-300",
};

type AssignmentListProps = {
  assignments: SceneAssignment[];
  highlightedSlug: string | null;
  onHover: (slug: string | null) => void;
  completedCount: number;
  total: number;
  progressPercent: number;
};

export function AssignmentList({
  assignments,
  highlightedSlug,
  onHover,
  completedCount,
  total,
  progressPercent,
}: AssignmentListProps) {
  return (
    <nav
      aria-label="Assignments"
      className="pointer-events-auto flex h-full w-80 max-w-[85vw] flex-col border-r border-white/10 bg-slate-950/65 backdrop-blur-xl"
    >
      {/* Header */}
      <div className="border-b border-white/10 p-5">
        <h1 className="text-lg font-bold tracking-tight text-white">
          Introduction to Computer Science
        </h1>

        <div className="mt-4 flex items-baseline justify-between text-xs text-slate-400">
          <span>
            <span className="font-semibold text-slate-100">{completedCount}</span> / {total} complete
          </span>
          <span className="font-semibold text-cyan-300">{progressPercent}%</span>
        </div>
        <div className="mt-2 h-1 w-full overflow-hidden rounded-full bg-white/10">
          <div
            className="h-full rounded-full bg-gradient-to-r from-blue-500 to-cyan-400 transition-all duration-700"
            style={{ width: `${progressPercent}%` }}
          />
        </div>
      </div>

      {/* Rows */}
      <ul className="flex-1 space-y-0.5 overflow-y-auto p-2">
        {assignments.map((assignment) => {
          const active = assignment.slug === highlightedSlug;
          return (
            <li key={assignment.slug}>
              <Link
                href={`/assignments/${assignment.slug}`}
                onMouseEnter={() => onHover(assignment.slug)}
                onMouseLeave={() => onHover(null)}
                onFocus={() => onHover(assignment.slug)}
                onBlur={() => onHover(null)}
                className={`group flex items-center gap-3 rounded-lg px-3 py-2.5 outline-none transition-all duration-200 focus-visible:ring-1 focus-visible:ring-cyan-400/60 ${
                  active
                    ? "bg-white/10 ring-1 ring-white/15"
                    : "hover:bg-white/[0.06]"
                }`}
              >
                <span
                  className={`h-2 w-2 shrink-0 rounded-full transition-transform duration-200 ${dotColor[assignment.status]} ${active ? "scale-150" : ""}`}
                />
                <span className="min-w-0 flex-1">
                  <span
                    className={`block truncate text-sm font-medium ${
                      assignment.status === "locked" ? "text-slate-400" : "text-slate-100"
                    }`}
                  >
                    {assignment.title}
                  </span>
                  <span className="block text-[11px] text-slate-500">
                    Week {assignment.week} · {typeLabels[assignment.type]}
                  </span>
                </span>
                <span
                  className={`shrink-0 text-[10px] font-medium uppercase tracking-wide ${pillColor[assignment.status]}`}
                >
                  {statusLabels[assignment.status]}
                </span>
              </Link>
            </li>
          );
        })}
      </ul>

      {/* Legend */}
      <div className="flex flex-wrap gap-4 border-t border-white/10 px-5 py-3 text-[11px] text-slate-400">
        <span className="flex items-center gap-1.5">
          <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" /> Completed
        </span>
        <span className="flex items-center gap-1.5">
          <span className="h-1.5 w-1.5 rounded-full bg-amber-400" /> In Progress
        </span>
        <span className="flex items-center gap-1.5">
          <span className="h-1.5 w-1.5 rounded-full bg-slate-600" /> Locked
        </span>
      </div>
    </nav>
  );
}
