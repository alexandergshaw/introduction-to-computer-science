"use client";

import dynamic from "next/dynamic";
import { useRouter } from "next/navigation";
import { useCallback, useEffect, useState } from "react";
import { AssignmentList } from "./AssignmentList";
import { AssignmentMenu } from "./AssignmentMenu";
import type { SceneAssignment } from "./statusStyles";

// WebGL only ever runs in the browser.
const SceneCanvas = dynamic(() => import("./SceneCanvas"), { ssr: false });

type JupiterSceneProps = {
  assignments: SceneAssignment[];
  completedCount: number;
  total: number;
  progressPercent: number;
};

export function JupiterScene({
  assignments,
  completedCount,
  total,
  progressPercent,
}: JupiterSceneProps) {
  const router = useRouter();
  const [highlightedSlug, setHighlightedSlug] = useState<string | null>(null);
  const [reducedMotion, setReducedMotion] = useState(false);
  const [webglAvailable, setWebglAvailable] = useState(true);

  // Detect reduced-motion preference + WebGL support on mount.
  useEffect(() => {
    const motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    setReducedMotion(motionQuery.matches);
    const onMotionChange = () => setReducedMotion(motionQuery.matches);
    motionQuery.addEventListener("change", onMotionChange);

    try {
      const canvas = document.createElement("canvas");
      setWebglAvailable(Boolean(canvas.getContext("webgl2") || canvas.getContext("webgl")));
    } catch {
      setWebglAvailable(false);
    }

    return () => motionQuery.removeEventListener("change", onMotionChange);
  }, []);

  // Navigate to an assignment's detail page (callback passed into the canvas, so
  // moons don't need router context inside R3F's separate reconciler).
  const handleSelect = useCallback(
    (slug: string) => router.push(`/assignments/${slug}`),
    [router],
  );

  // Prefetch detail routes so navigation feels instant.
  useEffect(() => {
    assignments.forEach((assignment) => router.prefetch(`/assignments/${assignment.slug}`));
  }, [assignments, router]);

  // ── No-WebGL fallback: the vertical list on its own ─────────────────────────
  if (!webglAvailable) {
    return (
      <main className="mx-auto h-[100dvh] w-full max-w-md" style={{ height: "100dvh" }}>
        <AssignmentList
          assignments={assignments}
          highlightedSlug={highlightedSlug}
          onHover={setHighlightedSlug}
          completedCount={completedCount}
          total={total}
          progressPercent={progressPercent}
        />
      </main>
    );
  }

  return (
    // Inline sizing (not utility classes) so the container has a real height
    // synchronously at mount — R3F only initializes once it measures a non-zero
    // container.
    <main className="relative w-full overflow-hidden" style={{ height: "100dvh" }}>
      {/* 3D scene fills the viewport behind everything else. */}
      <div className="absolute inset-0" style={{ position: "absolute", inset: 0 }}>
        <SceneCanvas
          assignments={assignments}
          reducedMotion={reducedMotion}
          highlightedSlug={highlightedSlug}
          onHover={setHighlightedSlug}
          onSelect={handleSelect}
        />
      </div>

      {/* Title + minimal horizontal menu, centered above Jupiter. */}
      <div className="pointer-events-none absolute inset-x-0 top-0 z-20 flex justify-center px-4 pt-6 sm:pt-8">
        <AssignmentMenu
          assignments={assignments}
          highlightedSlug={highlightedSlug}
          onHover={setHighlightedSlug}
          completedCount={completedCount}
          total={total}
          progressPercent={progressPercent}
        />
      </div>

      {/* Hint */}
      <p className="pointer-events-none absolute inset-x-0 bottom-4 z-20 px-6 text-center text-xs text-slate-500">
        Hover a moon or menu dot to highlight it · click to open · scroll to zoom · drag to look around
      </p>
    </main>
  );
}
