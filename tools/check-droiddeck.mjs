import assert from 'node:assert/strict';
import { advanceSpring } from '../projects/droiddeck/animations/focus-glide/examples/spring.mjs';

// Convergence, retargeting and clock semantics; this does not run Compose or measure FPS.
for (const hz of [30, 60, 120, 144]) {
  let state = { x: 0, v: 0 };
  for (let i = 0; i < hz * 2; i++) state = advanceSpring(state, 240, 1 / hz);
  assert.equal(state.x, 240); assert.equal(state.v, 0);
}
let moving = { x: 0, v: 0 };
for (let i = 0; i < 5; i++) moving = advanceSpring(moving, 300, 1 / 60);
assert.ok(moving.v > 0);
const retargeted = advanceSpring(moving, -100, 1 / 120);
const restarted = advanceSpring({ x: moving.x, v: 0 }, -100, 1 / 120);
assert.notEqual(retargeted.x, restarted.x);
assert.notEqual(retargeted.v, restarted.v);
let final = retargeted;
for (let i = 0; i < 240; i++) final = advanceSpring(final, -100, 1 / 120);
assert.deepEqual(final, { x: -100, v: 0 });
assert.deepEqual(advanceSpring(moving, 10, 5, { motionScale: 0 }), { x: 10, v: 0 });
assert.deepEqual(advanceSpring({ x: 0, v: 0 }, 100, 5), advanceSpring({ x: 0, v: 0 }, 100, .1));
assert.deepEqual(advanceSpring({ x: 0, v: 0 }, 100, .05, { motionScale: .5 }), advanceSpring({ x: 0, v: 0 }, 100, .1));
const reference = (t, k) => 1 - (1 + Math.sqrt(k) * t) * Math.exp(-Math.sqrt(k) * t);
let critical = { x: 0, v: 0 };
for (let i = 0; i < 12; i++) critical = advanceSpring(critical, 100, 1 / 120, { dampingRatio: 1, stiffness: 2400 });
assert.ok(Math.abs(critical.x / 100 - reference(.1, 2400)) < .04);
console.log(JSON.stringify({ result: 'passed', scope: 'DroidDeck adapted single-edge spring: convergence at multiple simulated timesteps, velocity retention, latest target, disabled motion, dt cap and scale, critical damping reference', visual_runtime: false }));
