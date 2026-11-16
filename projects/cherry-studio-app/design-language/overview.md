# overview

官方 DESIGN.md 明确中性优先、可读性优先、主题平价以及先用文字/间距建立层级。primary 为随主题变档的green-900，control-active为固定绿色开关轨道，brand=#ff5757仅为品牌。这三者不能合并成“Cherry红色主题”。

分析：视觉识别来自连续中性表面、紧凑文字与少量绿色强调。重现时保留动作色/品牌色分离、组间留白优先于卡片框；业务内容可以自由变化。mobile Token 已fork，不能套桌面数值。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`DESIGN.md:194` — `## Motion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/DESIGN.md#L194)
- [`packages/design-tokens/src/styles/product.css:36` — `--control-active`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/design-tokens/src/styles/product.css#L36)
