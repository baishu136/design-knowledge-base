# spacing

DESIGN.md规定采用Tailwind默认4/8/12/16/20/24/32/40/48/64刻度。按钮default水平px-4、垂直py-2.5，icon size-5；这是类值，RN端需由Uniwind转换。radius基础8px，rounded-xl=1.4倍=11.2，rounded-4xl=2.6倍=20.8；不要误用旧桌面圆角。BottomSheet的32圆角是当前源码局部常量，与文档“不得numeric borderRadius”的统一要求存在偏差，本库并列记录而不私自修复。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`DESIGN.md:194` — `## Motion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/DESIGN.md#L194)
- [`packages/ui/src/components/button/button.tsx:48` — `const rootBaseStyles`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/button/button.tsx#L48)
- [`packages/ui/src/components/bottom-sheet/bottom-sheet.tsx:113` — `export function BottomSheet(props`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/bottom-sheet/bottom-sheet.tsx#L113)
- [`packages/design-tokens/src/styles/native.css:96` — `--radius-xl`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/design-tokens/src/styles/native.css#L96)
