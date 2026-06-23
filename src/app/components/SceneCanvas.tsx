"use client";

import { useEffect } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Stars } from "@react-three/drei";
import { DecorativeMoons } from "./DecorativeMoons";
import { Jupiter } from "./Jupiter";
import { Moon } from "./Moon";
import { getOrbit } from "./orbits";
import type { SceneAssignment } from "./statusStyles";

type SceneCanvasProps = {
  assignments: SceneAssignment[];
  reducedMotion: boolean;
  highlightedSlug: string | null;
  onHover: (slug: string | null) => void;
  onSelect: (slug: string) => void;
};

// The WebGL scene. Imported with `ssr: false` from JupiterScene so three.js
// never runs on the server.
export default function SceneCanvas({
  assignments,
  reducedMotion,
  highlightedSlug,
  onHover,
  onSelect,
}: SceneCanvasProps) {
  // R3F initializes only once react-use-measure reports a non-zero container,
  // and it only re-measures (from {0,0}) on a window resize. In dev the route
  // CSS can apply a frame after mount, so without a nudge the canvas stays at
  // its 300×150 default. Dispatch a resize each frame until the canvas fills its
  // container, then stop. (Independent of R3F state to avoid a chicken-and-egg
  // with onCreated, which never fires while the container measures zero.)
  useEffect(() => {
    let frame = 0;
    let raf = 0;
    const sync = () => {
      const canvas = document.querySelector("canvas");
      const parent = canvas?.parentElement;
      if (canvas && parent) {
        const { width } = parent.getBoundingClientRect();
        if (width > 0 && Math.abs(canvas.clientWidth - width) <= 1) return; // sized, stop
      }
      window.dispatchEvent(new Event("resize"));
      if (frame++ < 120) raf = requestAnimationFrame(sync);
    };
    raf = requestAnimationFrame(sync);
    return () => cancelAnimationFrame(raf);
  }, []);

  return (
    <Canvas
      // Pulled back so Jupiter sits with margin around it (not filling the frame),
      // but still close enough that perspective keeps depth: a moon past the near
      // face looms larger, one behind the planet recedes. Zoom in for more drama.
      camera={{ position: [0, 3.0, 11.6], fov: 52 }}
      dpr={[1, 1.8]}
      gl={{ alpha: true, antialias: true }}
    >
      <ambientLight intensity={0.25} />
      <directionalLight position={[5, 3, 5]} intensity={1.5} color="#fff6e8" />

      {/* Static starfield (speed 0 — the stars never drift). */}
      <Stars radius={120} depth={60} count={2600} factor={3.4} fade speed={0} />

      <Jupiter reducedMotion={reducedMotion} />

      {/* Background field of small moons that populate the rings. */}
      <DecorativeMoons reducedMotion={reducedMotion} count={72} />

      {assignments.map((assignment, index) => (
        <Moon
          key={assignment.slug}
          orbit={getOrbit(index, assignments.length, assignment.type)}
          title={assignment.title}
          week={assignment.week}
          status={assignment.status}
          reducedMotion={reducedMotion}
          highlighted={assignment.slug === highlightedSlug}
          onHover={(over) => onHover(over ? assignment.slug : null)}
          onSelect={() => onSelect(assignment.slug)}
        />
      ))}

      {/* Drag to look around, scroll wheel to zoom (clamped so you can't go
          inside the ring or drift too far). Pan stays off to keep Jupiter centered. */}
      <OrbitControls
        enablePan={false}
        enableZoom
        minDistance={8}
        maxDistance={32}
        autoRotate={!reducedMotion}
        autoRotateSpeed={0.12}
        minPolarAngle={Math.PI * 0.28}
        maxPolarAngle={Math.PI * 0.72}
      />
    </Canvas>
  );
}
