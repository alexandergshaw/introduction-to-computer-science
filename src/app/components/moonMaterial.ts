import * as THREE from "three";

// Shared low-poly sphere for every moon (they're small on screen).
export const MOON_GEOMETRY = new THREE.SphereGeometry(1, 20, 20);

// Direction *toward* the sun, matching the directionalLight in SceneCanvas and
// Jupiter's own lighting so every body is lit consistently.
const LIGHT_DIR = new THREE.Vector3(5, 3, 5).normalize();

const vertexShader = /* glsl */ `
  varying vec3 vPos;
  varying vec3 vWorldNormal;

  void main() {
    vPos = position;
    vWorldNormal = normalize(mat3(modelMatrix) * normal);
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

const fragmentShader = /* glsl */ `
  precision highp float;

  varying vec3 vPos;
  varying vec3 vWorldNormal;

  uniform vec3 uLightDir;
  uniform vec3 uBaseColor;
  uniform vec3 uEmissive;
  uniform float uEmissiveIntensity;
  uniform float uSeed;
  uniform float uHighlight;

  // Seamless 3D value noise (sampled off the surface direction — no UV seam).
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
    vec3 dir = normalize(vPos);
    vec3 np = dir * 2.0 + vec3(uSeed);

    // Mottled regolith: broad maria/highland variation + fine grain.
    float broad = fbm(np * 1.6);
    float detail = fbm(np * 5.5);
    float surf = broad * 0.6 + detail * 0.4;

    // Craters: sharp dark pits punched out of a mid-frequency field.
    float pit = smoothstep(0.60, 0.48, fbm(np * 2.6 + 11.0));
    // Bright ejecta rims around the larger craters.
    float rimRing = smoothstep(0.46, 0.60, fbm(np * 2.6 + 11.0)) *
                    smoothstep(0.70, 0.58, fbm(np * 2.6 + 11.0));

    vec3 albedo = uBaseColor * (0.58 + 0.6 * surf);
    albedo *= 1.0 - pit * 0.45;            // darken crater floors
    albedo += uBaseColor * rimRing * 0.25; // lighten crater rims

    // Diffuse lighting with a soft terminator + ambient fill.
    vec3 N = normalize(vWorldNormal);
    float diff = max(dot(N, normalize(uLightDir)), 0.0);
    float light = 0.10 + 1.0 * diff;
    vec3 col = albedo * light;

    // Tiny relief pop so grain reads even on the lit side.
    col += (detail - 0.5) * 0.04;

    // Self-illumination for completed / in-progress moons (status glow).
    float rim = pow(1.0 - max(dot(N, vec3(0.0, 0.0, 1.0)), 0.0), 2.5);
    col += uEmissive * uEmissiveIntensity * (0.45 + 0.55 * surf);
    col += uEmissive * uEmissiveIntensity * rim * 0.6;

    // Highlight (hover / hovered list row): brighten and wrap in a cyan-white
    // fresnel halo. Driven smoothly from the component.
    col *= 1.0 + uHighlight * 0.5;
    col += vec3(0.55, 0.82, 1.0) * uHighlight * (0.3 + 1.1 * rim);

    gl_FragColor = vec4(col, 1.0);
  }
`;

export type MoonMaterialOptions = {
  baseColor: THREE.ColorRepresentation;
  emissive?: THREE.ColorRepresentation;
  emissiveIntensity?: number;
  seed?: number;
};

export function createMoonMaterial({
  baseColor,
  emissive = "#000000",
  emissiveIntensity = 0,
  seed = 0,
}: MoonMaterialOptions): THREE.ShaderMaterial {
  return new THREE.ShaderMaterial({
    uniforms: {
      uLightDir: { value: LIGHT_DIR.clone() },
      uBaseColor: { value: new THREE.Color(baseColor) },
      uEmissive: { value: new THREE.Color(emissive) },
      uEmissiveIntensity: { value: emissiveIntensity },
      uSeed: { value: seed },
      uHighlight: { value: 0 },
    },
    vertexShader,
    fragmentShader,
  });
}
