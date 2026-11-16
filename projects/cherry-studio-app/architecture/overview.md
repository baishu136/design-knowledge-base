# overview

packages/design-tokens拥有颜色来源与生成校验；packages/ui拥有公开组件/动效词汇；src/frontend/features负责业务，shared与backend不应被复制进独立UI。平台同名文件.ios/.android提供native适配；例如Android spinner用ActivityIndicator以避免持续Fabric提交，iOS开关另有原生实现。根入口需要自定义development client，不能承诺Expo Go即可运行。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/motion.ts:11` — `export const easing`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/motion.ts#L11)
- [`src/frontend/styles/global.css:3` — `@import`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/styles/global.css#L3)
- [`packages/ui/src/components/loading/spinner/spinner-control/spinner-control.android.tsx:11` — `export function SpinnerControl`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/loading/spinner/spinner-control/spinner-control.android.tsx#L11)
- [`packages/ui/src/components/switch/switch-control/switch-control.ios.tsx:21` — `export function SwitchControl`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/switch/switch-control/switch-control.ios.tsx#L21)
