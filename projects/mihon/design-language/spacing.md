# spacing

共享 Padding 为 4/8/16/24/32 dp。CollapsibleBox 标题行另用水平24、垂直12 dp；这是局部几何，不是额外全局刻度。TwoPanelBox 扣除左右 Insets 后，起始列=min(可用宽/2,450dp)，末列使用余量。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/material/Constants.kt:12` — `class Padding`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/material/Constants.kt#L12)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/CollapsibleBox.kt:26` — `fun CollapsibleBox`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/CollapsibleBox.kt#L26)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/TwoPanelBox.kt:19` — `fun TwoPanelBox`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/TwoPanelBox.kt#L19)
