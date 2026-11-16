# overview

Electron main拥有系统服务、窗口和数据能力；renderer组合页面；packages/ui拥有框架共享primitives与主题契约；shared承载跨进程类型。ThemeProvider通过IPC读取native主题，并使用preference hook；组件迁移应替换宿主状态，而不是引入整个Electron主进程。

动画有三条实现路径：Tailwind/CSS data-state用于Radix presence；Motion React用于多栏宽度；自定义RAF用于明确阅读导航。不同路径的时钟与生命周期不相同，不抽成一个无差别“300ms动画”函数。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`src/renderer/components/ThemeProvider.tsx:28` — `export const ThemeProvider`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/ThemeProvider.tsx#L28)
- [`packages/ui/src/components/primitives/dialog.tsx:87` — `function DialogContent(`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/dialog.tsx#L87)
- [`src/renderer/components/chat/shell/PageSidebar.tsx:28` — `export function PageSidebar`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/PageSidebar.tsx#L28)
- [`src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts:58` — `export function useSmoothScrollAnimation`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts#L58)
