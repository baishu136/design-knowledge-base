# typography

默认13档sizeSequence从13/18到128/128；step=1/2将每个语义档向后移并封顶，tokens.json保留step0值。官方typography.css明确正文走各平台系统字体；等宽字体在global.css为GeistMono-Regular（RN接受单字体名）。font-bold被覆写为600，与font-semibold同重，这是明确定义而非误差。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/utils/typography-scale.ts:24` — `const sizeSequence`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/utils/typography-scale.ts#L24)
- [`packages/design-tokens/src/styles/tokens/typography.css:24` — `--font-weight-bold`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/design-tokens/src/styles/tokens/typography.css#L24)
- [`src/frontend/styles/global.css:16` — `--font-mono`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/styles/global.css#L16)
