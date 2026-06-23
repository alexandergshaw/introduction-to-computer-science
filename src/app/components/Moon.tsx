import { useMemo, useRef, useState } from "react";
import { useFrame } from "@react-three/fiber";
import { Html } from "@react-three/drei";
import * as THREE from "three";
import type { OrbitParams } from "./orbits";
import { createMoonMaterial, MOON_GEOMETRY } from "./moonMaterial";
import { statusMoonColors, type AssignmentStatus } from "./statusStyles";

type MoonProps = {
  orbit: OrbitParams;
  title: string;
  week: number;
  status: AssignmentStatus;
  reducedMotion: boolean;
  highlighted: boolean;
  current: boolean;
  onHover: (over: boolean) => void;
  onSelect: () => void;
};

const HIGHLIGHT_SCALE = 2.4;

export function Moon({
  orbit,
  title,
  week,
  status,
  reducedMotion,
  highlighted,
  current,
  onHover,
  onSelect,
}: MoonProps) {
  const moverRef = useRef<THREE.Group>(null);
  const meshRef = useRef<THREE.Mesh>(null);
  const angleRef = useRef(orbit.phase);
  const scaleRef = useRef(orbit.size);
  const highlightRef = useRef(0);
  const [hovered, setHovered] = useState(false);
  const colors = statusMoonColors[status];

  const material = useMemo(
    () =>
      createMoonMaterial({
        baseColor: colors.color,
        emissive: colors.emissive,
        emissiveIntensity: colors.emissiveIntensity,
        seed: orbit.phase * 1.7 + orbit.radius,
      }),
    [colors.color, colors.emissive, colors.emissiveIntensity, orbit.phase, orbit.radius],
  );

  const active = hovered || highlighted;

  useFrame((state, delta) => {
    // Orbit.
    if (!reducedMotion) angleRef.current += delta * orbit.speed;
    if (moverRef.current) {
      const a = angleRef.current;
      moverRef.current.position.set(Math.cos(a) * orbit.radius, 0, Math.sin(a) * orbit.radius);
    }

    // The assignment the student is on: subtly, slowly, smoothly pulse it.
    const pulse = current && !reducedMotion ? 0.5 - 0.5 * Math.cos(state.clock.elapsedTime * 1.4) : 0; // 0 → 1, ~4.5s cycle

    // Smoothly ease scale toward the active target (hover wins; otherwise the
    // current moon gently breathes larger and back).
    const targetScale = orbit.size * (active ? HIGHLIGHT_SCALE : 1 + pulse * 0.45);
    scaleRef.current = THREE.MathUtils.damp(scaleRef.current, targetScale, 9, delta);
    if (meshRef.current) meshRef.current.scale.setScalar(scaleRef.current);

    highlightRef.current = THREE.MathUtils.damp(highlightRef.current, active ? 1 : 0, 9, delta);
    material.uniforms.uHighlight.value = highlightRef.current;

    // Brighten the current moon's glow in time with the breathing.
    material.uniforms.uEmissiveIntensity.value = colors.emissiveIntensity + pulse * 1.1;
  });

  const setCursor = (over: boolean) => {
    setHovered(over);
    onHover(over);
    if (typeof document !== "undefined") {
      document.body.style.cursor = over ? "pointer" : "auto";
    }
  };

  return (
    // Tilt + rotate the orbital plane; the inner group rides around it.
    <group rotation={[orbit.inclination, orbit.node, 0]}>
      <group
        ref={moverRef}
        position={[Math.cos(orbit.phase) * orbit.radius, 0, Math.sin(orbit.phase) * orbit.radius]}
      >
        <mesh
          ref={meshRef}
          geometry={MOON_GEOMETRY}
          material={material}
          scale={orbit.size}
          onPointerOver={(e) => {
            e.stopPropagation();
            setCursor(true);
          }}
          onPointerOut={(e) => {
            e.stopPropagation();
            setCursor(false);
          }}
          onClick={(e) => {
            e.stopPropagation();
            onSelect();
          }}
        />

        {active && (
          <Html center distanceFactor={9} zIndexRange={[40, 0]} style={{ pointerEvents: "none" }}>
            <div className="-translate-y-8 whitespace-nowrap rounded-md border border-cyan-400/40 bg-slate-900/90 px-2.5 py-1 text-center shadow-lg shadow-cyan-500/10 backdrop-blur-sm">
              <span className="block text-[11px] font-semibold leading-tight text-slate-100">
                {title}
              </span>
              <span className="block text-[9px] uppercase tracking-wide text-slate-400">
                Week {week}
              </span>
            </div>
          </Html>
        )}
      </group>
    </group>
  );
}
