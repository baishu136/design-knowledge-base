// Knowledge-base-owned verification harness. Runs only authored source-only examples, no upstream install.
import assert from 'node:assert/strict';
import { createScrollController } from '../projects/cherry-studio/animations/smooth-scroll/examples/controller.mjs';
import { advanceClock, phaseAt } from '../projects/cherry-studio-app/animations/foil-loader/examples/clock.mjs';

let seed = 0;
const queue = new Map();
const raf = cb => { queue.set(++seed, cb); return seed; };
const caf = id => queue.delete(id);
function tick() { const batch = [...queue.values()]; queue.clear(); batch.forEach(cb => cb()); }
function flush() { for (let i = 0; queue.size && i < 200; i++) tick(); assert.equal(queue.size, 0); }
let node = { scrollTop: 30 };
let target = 200;
let completed = 0;
const c = createScrollController(() => node, raf, caf);
c.scrollTo(() => target, { onComplete: () => completed++ });
for (let i = 0; i < 49; i++) tick();
assert.equal(completed, 0);
target = 340; tick();
assert.equal(node.scrollTop, 340); assert.equal(completed, 1); assert.equal(c.isAnimating(), false);
c.scrollTo(() => 1000, { onComplete: () => completed++ }); tick();
const stopped = node.scrollTop; c.cancel(); flush();
assert.equal(node.scrollTop, stopped); assert.equal(completed, 1);
c.scrollTo(() => 800); tick(); c.scrollTo(() => 80); flush(); assert.equal(node.scrollTop, 80);
c.scrollTo(() => 999, { onComplete: () => completed++ }); node = null; tick();
assert.equal(c.isAnimating(), false); assert.equal(completed, 1);
node = { scrollTop: 0 }; c.scrollTo(() => 123, { frames: 0 }); tick(); assert.equal(node.scrollTop, 123);
c.scrollTo(() => 900); c.dispose(); assert.equal(queue.size, 0);
assert.equal(advanceClock(10, 1000, true), 10.064);
assert.equal(advanceClock(10, 16, false), 0);
assert.ok(Math.abs(advanceClock(1199.99, 64, true) - .054) < 1e-9);
assert.ok(Math.abs(phaseAt(2.4).cycle) < 1e-9);
assert.ok(Math.abs(phaseAt(1.2).eased - .5) < 1e-9);
console.log(JSON.stringify({result:'passed',scope:'scroll controller cancellation, replacement, disposal, missing DOM, moving target and one-frame boundary; loader clock cap, reset, wrap and phase',visual_runtime:false}));
