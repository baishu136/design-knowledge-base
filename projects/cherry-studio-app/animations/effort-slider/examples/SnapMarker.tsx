// Adapted from https://github.com/CherryHQ/cherry-studio-app at e6d157d2ea604ef65d38ca14e88ba92de706ad8a
// Source: src/frontend/features/chat/components/ChatInput/effortSlider/utils/constants.ts
// Attribution: Cherry Studio contributors. AGPL-3.0; modified for this knowledge base.
// Subset: programmatic snapping only. Does not implement drag, magnetism or adjustable semantics.
import React, { useEffect } from 'react';
import Animated, {
  Easing, cancelAnimation, useAnimatedStyle, useReducedMotion, useSharedValue, withTiming,
} from 'react-native-reanimated';

export function SnapMarker({ index, count, travel }: { index: number; count: number; travel: number }) {
  const p = useSharedValue(0);
  const reduced = useReducedMotion();
  const target = Math.max(0, Math.min(count - 1, index)) / Math.max(1, count - 1);
  useEffect(() => {
    p.value = reduced ? target : withTiming(target, { duration: 200, easing: Easing.out(Easing.cubic) });
    return () => cancelAnimation(p);
  }, [p, target, reduced]);
  const style = useAnimatedStyle(() => ({ transform: [{ translateX: p.value * Math.max(0, travel) }] }));
  return <Animated.View accessible={false} style={[{ width: 20, height: 20, borderRadius: 10, backgroundColor: '#666' }, style]} />;
}
