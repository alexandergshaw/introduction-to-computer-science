"use client";

import Link from "next/link";
import { statusLabels, type AssignmentStatus, type SceneAssignment } from "./statusStyles";

const dotColor: Record<AssignmentStatus, string> = {
  locked: "bg-slate-500/80",
  "in-progress": "bg-amber-400",
  completed: "bg-emerald-400",
};

const dotGlow: Record<AssignmentStatus, string> = {
  locked: "",
  "in-progress": "shadow-[0_0_10px_2px] shadow-amber-400/50",
  completed: "shadow-[0_0_10px_2px] shadow-emerald-400/50",
};

type AssignmentMenuProps = {
  assignments: SceneAssignment[];
  highlightedSlug: string | null;
  onHover: (slug: string | null) => void;
  completedCount: number;
  total: number;
  progressPercent: number;
};

export function AssignmentMenu({
  assignments,
  highlightedSlug,
  onHover,
  completedCount,
  total,
  progressPercent,
}: AssignmentMenuProps) {
  return (
    <div className="pointer-events-none flex flex-col items-center gap-3">
      {/* Title, centered above the menu */}
      <h1 className="text-center text-2xl font-semibold tracking-tight text-white drop-shadow-[0_2px_12px_rgba(0,0,0,0.6)] sm:text-3xl">
        Introduction to Computer Science
      </h1>

      {/* Minimal horizontal menu — a dot per assignment, in a frosted pill */}
      <nav
        aria-label="Assignments"
        className="pointer-events-auto relative flex items-center gap-2.5 rounded-full border border-white/10 bg-white/[0.04] px-5 py-3 shadow-lg shadow-black/20 backdrop-blur-md"
      >
        {/* subtle connector line through the dots */}
        <span aria-hidden className="absolute inset-x-5 top-1/2 h-px -translate-y-1/2 bg-white/10" />

        {assignments.map((assignment) => {
          const active = assignment.slug === highlightedSlug;
          return (
            <Link
              key={assignment.slug}
              href={`/assignments/${assignment.slug}`}
              onMouseEnter={() => onHover(assignment.slug)}
              onMouseLeave={() => onHover(null)}
              onFocus={() => onHover(assignment.slug)}
              onBlur={() => onHover(null)}
              className="group relative z-10 flex h-4 w-4 items-center justify-center rounded-full outline-none focus-visible:ring-1 focus-visible:ring-cyan-300/70"
            >
              <span
                className={`block rounded-full transition-all duration-200 ${dotColor[assignment.status]} ${
                  assignment.status === "in-progress" ? "toc-current" : ""
                } ${
                  active ? `h-3.5 w-3.5 ${dotGlow[assignment.status]}` : "h-2 w-2 group-hover:h-2.5 group-hover:w-2.5"
                }`}
              />
              <span className="sr-only">
                {assignment.title} — week {assignment.week}, {statusLabels[assignment.status]}
              </span>

              {/* Tooltip, shown when this assignment is active (hovered here or its moon) */}
              <span
                className={`pointer-events-none absolute left-1/2 top-full mt-3 -translate-x-1/2 whitespace-nowrap rounded-md border border-white/10 bg-slate-900/95 px-2.5 py-1 text-center shadow-lg backdrop-blur transition-all duration-150 ${
                  active ? "translate-y-0 opacity-100" : "translate-y-1 opacity-0"
                }`}
              >
                <span className="block text-[11px] font-semibold leading-tight text-slate-100">
                  {assignment.title}
                </span>
                <span className="block text-[9px] uppercase tracking-wide text-slate-400">
                  Week {assignment.week} · {statusLabels[assignment.status]}
                </span>
              </span>
            </Link>
          );
        })}
      </nav>

      {/* Compact progress caption */}
      <p className="text-[11px] text-slate-400/90">
        <span className="font-semibold text-slate-200">{completedCount}</span> of {total} complete{" "}
        <span className="text-slate-600">·</span>{" "}
        <span className="font-semibold text-cyan-300">{progressPercent}%</span>
      </p>
    </div>
  );
}
