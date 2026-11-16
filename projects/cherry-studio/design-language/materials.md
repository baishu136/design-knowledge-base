# materials

官方层级为background地面、card内容、popover短暂浮层、sidebar导航区。Dialog overlay黑50%、z80；content bg-card/shadow-xl/rounded-3xl且no-drag避免Electron标题栏拖拽吞点击。文本shimmer通过background-clip:text与background-position，不是Shader；will-change不能保证零重绘。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`DESIGN.md:22` — `## 1. Design direction`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/DESIGN.md#L22)
- [`packages/ui/src/components/primitives/dialog.tsx:87` — `function DialogContent(`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/dialog.tsx#L87)
- [`src/renderer/assets/styles/animation.css:245` — `.animation-shimmer {`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/assets/styles/animation.css#L245)
