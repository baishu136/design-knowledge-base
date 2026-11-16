# overview

Menu打开须完成测量；关闭立即pointerEvents=none及隐藏无障碍子树，但保留绘制至动画结束。Android键盘改变锚点时关闭菜单。ZoomableImage在1倍时禁用pan，避免抢导航；pinch/pan同时而doubleTap与其Race。开关Android/Web是items-start/end直接切换，不能宣称自定义spring。项目gesture arbitration文档自称设计目标，不应当作所有组件均已实现的事实。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/components/menu/use-menu-motion.ts:13` — `export function useMenuMotion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/use-menu-motion.ts#L13)
- [`packages/ui/src/components/menu/menu-panel.tsx:16` — `export function MenuPanel`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-panel.tsx#L16)
- [`packages/ui/src/components/menu/menu-content.tsx:19` — `export function MenuContent`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-content.tsx#L19)
- [`src/frontend/components/ArtifactPreview/components/ArtifactImageViewer/ZoomableImage.tsx:17` — `export function ZoomableImage`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/components/ArtifactPreview/components/ArtifactImageViewer/ZoomableImage.tsx#L17)
- [`packages/ui/src/components/switch/switch-control/switch-control.tsx:15` — `export function SwitchControl`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/switch/switch-control/switch-control.tsx#L15)
- [`DESIGN.md:194` — `## Motion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/DESIGN.md#L194)
