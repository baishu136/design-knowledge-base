// Adapted from https://github.com/Droid-Deck/DroidDeck @ f65e7a3d436bee56f32626dc3536708d12e43162
// Source: app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt
// Attribution: DroidDeck contributors. GPL-3.0. Modified for this knowledge base.
// Numeric single-edge model, not the Compose host, four-edge delays, droplet or focus lifecycle.
export function advanceSpring({ x, v }, target, elapsedSeconds, {
  dampingRatio = .62, stiffness = 700, motionScale = 1,
} = {}) {
  // The source caller handles disabled motion before entering the integrator.
  if (motionScale === 0) return { x: target, v: 0 };
  let left = Math.max(0, Math.min(elapsedSeconds, .1)) / Math.max(motionScale, .01);
  const friction = 2 * dampingRatio * Math.sqrt(stiffness);
  while (left > 0) {
    const h = Math.min(left, .004);
    v += (-stiffness * (x - target) - friction * v) * h;
    x += v * h;
    left -= h;
  }
  return Math.abs(x - target) < .3 && Math.abs(v) < 3 ? { x: target, v: 0 } : { x, v };
}
