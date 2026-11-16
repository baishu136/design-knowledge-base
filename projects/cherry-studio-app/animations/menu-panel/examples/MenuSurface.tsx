// Adapted from https://github.com/CherryHQ/cherry-studio-app at e6d157d2ea604ef65d38ca14e88ba92de706ad8a
// Source: packages/ui/src/components/menu/{use-menu-motion,menu-panel,menu-motion}.ts(x)
// Attribution: Cherry Studio contributors. AGPL-3.0; modified for this knowledge base.
// Subset: content motion only. No anchor, size expansion, blur, focus management or portal.
import React, { type ReactNode, useEffect, useState } from 'react';
import Animated, {
  Easing, cancelAnimation, runOnJS, useAnimatedStyle, useReducedMotion,
  useSharedValue, withTiming,
} from 'react-native-reanimated';

export function MenuSurface({ open, children }: { open: boolean; children: ReactNode }) {
  const p = useSharedValue(0);
  const reduced = useReducedMotion();
  const [retained, setRetained] = useState(open);
  useEffect(() => {
    let current = true;
    if (open) setRetained(true);
    const done = () => { if (current) setRetained(false); };
    p.value = withTiming(open ? 1 : 0, {
      duration: reduced ? 0 : open ? 350 : 250,
      easing: open ? Easing.bezier(.34, 1.25, .64, 1) : Easing.bezier(.22, 1, .36, 1),
    }, finished => { if (finished && !open) runOnJS(done)(); });
    return () => { current = false; cancelAnimation(p); };
  }, [open, reduced, p]);
  const style = useAnimatedStyle(() => ({
    opacity: p.value,
    transform: [{ translateX: 40 * (1 - p.value) }, { scale: .97 + .03 * p.value }],
  }));
  if (!open && !retained) return null;
  return <Animated.View style={style} pointerEvents={open ? 'auto' : 'none'}
    accessibilityElementsHidden={!open} importantForAccessibility={open ? 'auto' : 'no-hide-descendants'}>
    {children}
  </Animated.View>;
}
