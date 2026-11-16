// Adapted from https://github.com/CherryHQ/cherry-studio at c3263227592ad14313da2b4153bf88502c466454
// Source: src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts
// Attribution: Cherry Studio contributors. AGPL-3.0; modified for this knowledge base.
// Framework-free controller; explicit dispose replaces React effect cleanup.
export function createScrollController(getNode, raf, caf) {
  let pending = null;
  let running = false;
  function cancel() {
    if (pending !== null) caf(pending);
    pending = null;
    running = false;
  }
  function scrollTo(target, options = {}) {
    cancel();
    const node = getNode();
    if (!node) return;
    const start = node.scrollTop;
    const frames = Math.max(1, options.frames ?? 50);
    const easing = options.easing ?? (t => 1 - 2 ** (-10 * t));
    let frame = 0;
    running = true;
    function step() {
      pending = null;
      const current = getNode();
      if (!current) { running = false; return; }
      frame++;
      current.scrollTop = start + (target() - start) * Math.min(1, easing(frame / frames));
      if (frame >= frames) {
        current.scrollTop = target();
        running = false;
        options.onComplete?.();
      } else pending = raf(step);
    }
    pending = raf(step);
  }
  return { scrollTo, cancel, dispose: cancel, isAnimating: () => running };
}
