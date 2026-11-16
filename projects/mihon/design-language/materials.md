# materials

AdaptiveSheet 使用 shapes.extraLarge 和 surfaceContainerHigh；具体圆角由 Material 主题提供，本轮不补默认 dp。阅读工具栏取 surfaceColorAtElevation(3dp)，暗色 alpha=.9，浅色=.95。这里是色彩叠加，不是已证实的实时背景模糊。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt:53` — `fun AdaptiveSheet`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt#L53)
- [`app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt:46` — `fun ReaderAppBars`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt#L46)
