import type { ModuleType } from "./modules";

// ── Shared status vocabulary ─────────────────────────────────────────────────
// A single source of truth for how an assignment's status is represented, used
// by both the 2D card / detail panel (Tailwind classes) and the 3D moons (hex
// colors fed into three.js materials).
export type AssignmentStatus = "locked" | "in-progress" | "completed";

// A serializable assignment shape passed from the server page into the client
// scene. Keep this free of any client-only imports so the server component can
// import the type too.
export type SceneAssignment = {
  slug: string;
  week: number;
  title: string;
  type: ModuleType;
  status: AssignmentStatus;
};

// ── DOM (Tailwind) styles ────────────────────────────────────────────────────
export const statusBadgeStyles: Record<AssignmentStatus, string> = {
  locked: "bg-slate-800 text-slate-500 ring-1 ring-slate-700/60",
  "in-progress": "bg-amber-500/10 text-amber-400 ring-1 ring-amber-500/25",
  completed: "bg-emerald-500/10 text-emerald-400 ring-1 ring-emerald-500/25",
};

export const statusLabels: Record<AssignmentStatus, string> = {
  locked: "Locked",
  "in-progress": "In Progress",
  completed: "Completed",
};

export const accentBar: Record<AssignmentStatus, string> = {
  locked: "bg-slate-700",
  "in-progress": "bg-amber-400",
  completed: "bg-emerald-400",
};

export const typeBadgeStyles: Record<ModuleType, string> = {
  assignment: "bg-blue-500/10 text-blue-400 ring-1 ring-blue-500/20",
  review: "bg-sky-500/10 text-sky-400 ring-1 ring-sky-500/20",
  exam: "bg-rose-500/10 text-rose-400 ring-1 ring-rose-500/20",
};

export const typeLabels: Record<ModuleType, string> = {
  assignment: "Assignment",
  review: "Review",
  exam: "Exam",
};

// ── 3D moon material colors ──────────────────────────────────────────────────
// Completed moons glow green, in-progress moons glow amber, and locked moons
// are dim and rocky so the planet's progress reads at a glance.
export const statusMoonColors: Record<
  AssignmentStatus,
  { color: string; emissive: string; emissiveIntensity: number }
> = {
  locked: { color: "#475569", emissive: "#1e293b", emissiveIntensity: 0.15 },
  "in-progress": { color: "#fbbf24", emissive: "#f59e0b", emissiveIntensity: 0.55 },
  completed: { color: "#34d399", emissive: "#10b981", emissiveIntensity: 0.7 },
};
