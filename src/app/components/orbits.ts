import type { ModuleType } from "./modules";

// ── Deterministic orbit parameters ───────────────────────────────────────────
// Each assignment becomes a moon on its own orbit. We derive every orbit
// parameter from the assignment's index so the layout is stable across renders
// and identical on the server and client (no Math.random at render time).

export type OrbitParams = {
  radius: number; // distance from Jupiter's center, in scene units
  speed: number; // angular velocity, radians per second
  inclination: number; // tilt of the orbital plane (radians)
  node: number; // rotation of the orbital plane about the vertical axis
  phase: number; // starting angle along the orbit
  size: number; // moon radius
};

// Cheap hash → pseudo-random number in [0, 1), stable for a given seed.
export function rand(seed: number): number {
  const x = Math.sin(seed * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
}

const JUPITER_RADIUS = 3.3;

export function getOrbit(index: number, total: number, type: ModuleType): OrbitParams {
  const r1 = rand(index + 1);
  const r2 = rand(index * 1.7 + 13.3);
  const r3 = rand(index * 2.3 + 47.7);

  // A fairly tight ring band sitting just off Jupiter's surface, with a little
  // radial scatter so it isn't a perfect circle.
  const spread = total > 1 ? index / (total - 1) : 0;
  const radius = JUPITER_RADIUS + 1.5 + spread * 1.5 + (r1 - 0.5) * 0.4; // ≈ 4.6 .. 6.5

  // Very slow, stately orbits — closer moons still drift a little faster
  // (loosely Keplerian) with a touch of variation.
  const speed = (0.03 + r2 * 0.02) * (3.6 / radius);

  // Gentle tilts give the ring some thickness without scattering moons all over.
  const inclination = (r2 - 0.5) * 0.5; // ≈ ±14°
  const node = r1 * Math.PI * 2;
  const phase = r3 * Math.PI * 2;

  // Small moons relative to Jupiter (radius 2.2). Exams/reviews are a touch
  // larger so milestones still stand out.
  const baseSize = type === "assignment" ? 0.06 : 0.085;
  const size = baseSize + r3 * 0.02;

  return { radius, speed, inclination, node, phase, size };
}

// Background "filler" moons that populate the ring — purely decorative, not
// tied to any assignment. They share the same tight ring band as the assignment
// moons (with a touch more scatter) and are mostly tiny so the assignment moons
// still read.
export function getDecorativeOrbit(index: number): OrbitParams {
  const r1 = rand(index * 1.3 + 101.1);
  const r2 = rand(index * 2.7 + 211.7);
  const r3 = rand(index * 3.9 + 307.3);
  const r4 = rand(index * 5.1 + 401.9);

  const radius = JUPITER_RADIUS + 1.3 + r4 * 2.2; // ≈ 4.6 .. 6.8
  const speed = (0.022 + r2 * 0.022) * (3.6 / radius);
  const inclination = (r1 - 0.5) * 0.6; // ≈ ±17°, ring with some thickness
  const node = r2 * Math.PI * 2;
  const phase = r3 * Math.PI * 2;
  const size = 0.018 + r1 * 0.04; // tiny .. small

  return { radius, speed, inclination, node, phase, size };
}
