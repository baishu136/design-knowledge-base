# overview

源码事实：TachiyomiTheme 按 AppTheme / 系统深浅色 / AMOLED 选择 ColorScheme，交给 MaterialExpressiveTheme；不是一套固定蓝色覆盖所有用户。Typography.header 从 bodyMedium 派生，以 onSurfaceVariant 和 SemiBold 建立组标题。

分析：其辨识度来自封面内容优先、Material 语义层次和可退出的阅读控制层。复现时保留 surface/onSurface 配对、书库状态与阅读内容的分层；可以调整主题色，不应把默认预设蓝当作品牌强制色。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt:37` — `BaseTachiyomiTheme`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt#L37)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/theme/Typography.kt:9` — `Typography.header`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/theme/Typography.kt#L9)
- [`app/src/main/java/eu/kanade/presentation/theme/colorscheme/BaseColorScheme.kt:17` — `getColorScheme`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/theme/colorscheme/BaseColorScheme.kt#L17)
