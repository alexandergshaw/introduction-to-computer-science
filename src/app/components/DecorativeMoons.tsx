import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import { getDecorativeOrbit, rand } from "./orbits";
import { createMoonMaterial, MOON_GEOMETRY } from "./moonMaterial";

type DecorativeMoonsProps = {
  reducedMotion: boolean;
  count?: number;
};

// A rocky base tone derived deterministically from the moon's index — a spread
// of greys and warm browns so the field looks varied.
function rockyColor(index: number): THREE.Color {
  const t = rand(index * 7.3 + 91.7);
  return new THREE.Color().setHSL(0.06 + t * 0.05, 0.1 + t * 0.14, 0.3 + t * 0.22);
}

// A large field of purely decorative moons that fill the orbits around Jupiter.
// All of them animate from a single useFrame, share one geometry, and are not
// raycast (so they never intercept hovers/clicks on the assignment moons).
export function DecorativeMoons({ reducedMotion, count = 72 }: DecorativeMoonsProps) {
  const orbits = useMemo(
    () => Array.from({ length: count }, (_, i) => getDecorativeOrbit(i)),
    [count],
  );
  const materials = useMemo(
    () =>
      orbits.map((orbit, i) =>
        createMoonMaterial({ baseColor: rockyColor(i), seed: orbit.phase * 2.1 + i }),
      ),
    [orbits],
  );

  const moverRefs = useRef<(THREE.Group | null)[]>([]);
  const angles = useRef<number[]>(orbits.map((orbit) => orbit.phase));

  useFrame((_, delta) => {
    for (let i = 0; i < orbits.length; i++) {
      const orbit = orbits[i];
      if (!reducedMotion) angles.current[i] += delta * orbit.speed;
      const mover = moverRefs.current[i];
      if (mover) {
        const a = angles.current[i];
        mover.position.set(Math.cos(a) * orbit.radius, 0, Math.sin(a) * orbit.radius);
      }
    }
  });

  return (
    <>
      {orbits.map((orbit, i) => (
        <group key={i} rotation={[orbit.inclination, orbit.node, 0]}>
          <group
            ref={(el) => {
              moverRefs.current[i] = el;
            }}
            position={[
              Math.cos(orbit.phase) * orbit.radius,
              0,
              Math.sin(orbit.phase) * orbit.radius,
            ]}
          >
            <mesh
              geometry={MOON_GEOMETRY}
              material={materials[i]}
              scale={orbit.size}
              raycast={() => null}
            />
          </group>
        </group>
      ))}
    </>
  );
}
