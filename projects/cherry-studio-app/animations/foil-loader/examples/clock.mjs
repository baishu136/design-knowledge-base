// Adapted from https://github.com/CherryHQ/cherry-studio-app at e6d157d2ea604ef65d38ca14e88ba92de706ad8a
// Source: packages/ui/src/components/loading/image-generation-loader{,-effect}.ts(x)
// Attribution: Cherry Studio contributors. AGPL-3.0; modified for this knowledge base.
// Framework-free clock/phase model only. This does not render or compile SkSL.
export function advanceClock(seconds, deltaMs, active) {
  if (!active) return 0;
  return (seconds + Math.max(0, Math.min(deltaMs ?? 0, 64)) / 1000) % 1200;
}
export function phaseAt(seconds) {
  const cycle = ((seconds / 2.4) % 1 + 1) % 1;
  return { cycle, eased: .5 * cycle + .5 * cycle * cycle * (3 - 2 * cycle) };
}
