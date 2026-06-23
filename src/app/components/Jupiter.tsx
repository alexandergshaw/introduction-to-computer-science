import { useMemo, useRef } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";

export const JUPITER_RADIUS = 3.3;

// Direction *toward* the sun (matches the directionalLight in SceneCanvas) so
// the planet's terminator lines up with how the moons are lit.
const LIGHT_DIR = new THREE.Vector3(5, 3, 5).normalize();

const vertexShader = /* glsl */ `
  varying vec2 vUv;
  varying vec3 vWorldNormal;
  varying vec3 vPos;

  void main() {
    vUv = uv;
    vWorldNormal = normalize(mat3(modelMatrix) * normal);
    // Object-space position drives the cloud noise — it's continuous all the way
    // around the sphere, so there's no seam where the UVs wrap.
    vPos = position;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const fragmentShader = /* glsl */ `
  precision highp float;

  varying vec2 vUv;
  varying vec3 vWorldNormal;
  varying vec3 vPos;

  uniform float uTime;
  uniform vec3 uLightDir;

  // ── Seamless 3D noise + fractal Brownian motion ──────────────────────────
  // Sampling noise in 3D (off the surface direction) avoids the vertical seam a
  // 2D UV lookup creates where longitude wraps from 1 back to 0.
  float hash(vec3 p) {
    return fract(sin(dot(p, vec3(127.1, 311.7, 74.7))) * 43758.5453123);
  }
  float noise(vec3 x) {
    vec3 i = floor(x);
    vec3 f = fract(x);
    f = f * f * (3.0 - 2.0 * f);
    return mix(
      mix(mix(hash(i + vec3(0.0, 0.0, 0.0)), hash(i + vec3(1.0, 0.0, 0.0)), f.x),
          mix(hash(i + vec3(0.0, 1.0, 0.0)), hash(i + vec3(1.0, 1.0, 0.0)), f.x), f.y),
      mix(mix(hash(i + vec3(0.0, 0.0, 1.0)), hash(i + vec3(1.0, 0.0, 1.0)), f.x),
          mix(hash(i + vec3(0.0, 1.0, 1.0)), hash(i + vec3(1.0, 1.0, 1.0)), f.x), f.y),
      f.z);
  }
  // 5 octaves of noise for turbulent, cloud-like detail.
  float fbm(vec3 p) {
    float v = 0.0;
    float amp = 0.5;
    for (int i = 0; i < 5; i++) {
      v += amp * noise(p);
      p *= 2.0;
      amp *= 0.5;
    }
    return v;
  }

  void main() {
    // Surface direction (seamless) drives the noise; latitude still bands on uv.y
    // (the seam is only in longitude, so uv.y is fine).
    vec3 dir = normalize(vPos);
    float lat = vUv.y;

    // Slow zonal flow — clouds drift along the bands.
    float flow = uTime * 0.015;

    // Domain warp: push the band coordinate around with fbm so belts billow and
    // swirl rather than sitting in straight stripes.
    float warpX = fbm(dir * 2.5 + vec3(0.0, 0.0, flow));
    float warpY = fbm(dir * 2.5 + vec3(4.7, 2.1, -flow));
    float bandCoord = lat * 24.0 + (warpX - 0.5) * 7.0;

    // High-frequency turbulence layered on top for filaments and curls.
    float turb = fbm(dir * 6.0 + vec3(warpY, 0.0, flow * 2.0));

    // Belt/zone profile, softened by the turbulence.
    float belts = sin(bandCoord) * 0.5 + 0.5;
    belts = mix(belts, turb, 0.4);

    // Rich Jupiter palette: bright cream zones, vivid amber, rust belts, deep maroon.
    vec3 cZone  = vec3(0.99, 0.91, 0.75);
    vec3 cTan   = vec3(0.93, 0.63, 0.31);
    vec3 cBelt  = vec3(0.76, 0.37, 0.17);
    vec3 cDark  = vec3(0.47, 0.19, 0.13);

    vec3 col = mix(cBelt, cZone, smoothstep(0.30, 0.85, belts));
    col = mix(col, cTan, smoothstep(0.35, 0.65, turb) * 0.5);
    col = mix(col, cDark, smoothstep(0.20, 0.0, belts) * 0.6);

    // Subtle polar darkening / haze (warm, not grey).
    float pole = smoothstep(0.55, 1.0, abs(lat - 0.5) * 2.0);
    col = mix(col, vec3(0.42, 0.28, 0.22), pole * 0.5);

    // Great Red Spot — an oval storm with internal swirl, rotates in and out.
    vec2 sp = vUv - vec2(0.60, 0.40);
    sp.x *= 2.0;
    float r = length(sp);
    float ang = atan(sp.y, sp.x) + r * 7.0;          // spiral the interior
    float spotMask = smoothstep(0.12, 0.03, r);
    float spotTurb = fbm(vec3(cos(ang), sin(ang), 0.0) * 3.0 + r * 6.0);
    vec3 spotCol = mix(vec3(0.80, 0.25, 0.15), vec3(0.94, 0.52, 0.33), spotTurb);
    col = mix(col, spotCol, spotMask * 0.92);

    // Lift saturation for richer, more vivid bands.
    float luma = dot(col, vec3(0.299, 0.587, 0.114));
    col = mix(vec3(luma), col, 1.2);

    // ── Lighting ─────────────────────────────────────────────────────────────
    vec3 n = normalize(vWorldNormal);
    float diff = max(dot(n, normalize(uLightDir)), 0.0);
    float light = smoothstep(-0.12, 1.0, diff);        // soft, wide terminator
    col *= 0.10 + 1.05 * light;

    // Bluish atmospheric rim toward the camera.
    float rim = pow(1.0 - max(dot(n, vec3(0.0, 0.0, 1.0)), 0.0), 3.0);
    col += vec3(0.35, 0.46, 0.72) * rim * 0.22;

    gl_FragColor = vec4(col, 1.0);
  }
`;

export function Jupiter({ reducedMotion }: { reducedMotion: boolean }) {
  const meshRef = useRef<THREE.Mesh>(null);

  const material = useMemo(
    () =>
      new THREE.ShaderMaterial({
        uniforms: {
          uTime: { value: 0 },
          uLightDir: { value: LIGHT_DIR.clone() },
        },
        vertexShader,
        fragmentShader,
      }),
    [],
  );

  useFrame((_, delta) => {
    material.uniforms.uTime.value += delta;
    if (meshRef.current && !reducedMotion) {
      // Slow, stately rotation.
      meshRef.current.rotation.y += delta * 0.018;
    }
  });

  return (
    // Outer group applies Jupiter's slight axial tilt; the mesh spins on its own axis.
    <group rotation={[0, 0, 0.05]}>
      <mesh
        ref={meshRef}
        material={material}
        // Swallow pointer events so moons passing behind the planet can't be
        // hovered or clicked through it.
        onPointerOver={(e) => e.stopPropagation()}
        onPointerMove={(e) => e.stopPropagation()}
        onClick={(e) => e.stopPropagation()}
      >
        <sphereGeometry args={[JUPITER_RADIUS, 96, 96]} />
      </mesh>
    </group>
  );
}
