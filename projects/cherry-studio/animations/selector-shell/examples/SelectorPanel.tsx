// Adapted from https://github.com/CherryHQ/cherry-studio at c3263227592ad14313da2b4153bf88502c466454
// Source: src/renderer/assets/styles/animation.css
// Attribution: Cherry Studio contributors. AGPL-3.0; modified for this knowledge base.
// Subset: visual tracks only. Parent must retain closed content for 120ms and manage focus.
import React, { type ReactNode } from 'react';
import './selector.css';
export function SelectorPanel({ open, children }: { open: boolean; children: ReactNode }) {
  return <div className="selector" data-state={open ? 'open' : 'closed'} aria-hidden={!open} inert={!open}>
    <div className="selector-panel">{children}</div>
  </div>;
}
