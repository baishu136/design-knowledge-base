# materials

菜单MenuPanel用popover表面、2点blur随progress衰减，另有容器宽高插值；不只是合成层scale。图片生成Loader用单Skia Shader绘制珠光、光带和细纹，适配表面亮度；静止态uStatic把效果alpha置0，保留中性底。BottomSheet用原生presentation和scrim token，不推测其内部弹簧。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/components/menu/menu-panel.tsx:16` — `export function MenuPanel`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-panel.tsx#L16)
- [`packages/ui/src/components/menu/menu-content.tsx:19` — `export function MenuContent`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-content.tsx#L19)
- [`packages/ui/src/components/loading/image-generation-loader-effect.ts:3` — `const IMAGE_GENERATION_LOADER_SKSL`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/loading/image-generation-loader-effect.ts#L3)
- [`packages/ui/src/components/loading/image-generation-loader.tsx:106` — `function useLoaderClock`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/loading/image-generation-loader.tsx#L106)
- [`packages/ui/src/components/bottom-sheet/bottom-sheet.tsx:113` — `export function BottomSheet(props`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/bottom-sheet/bottom-sheet.tsx#L113)
