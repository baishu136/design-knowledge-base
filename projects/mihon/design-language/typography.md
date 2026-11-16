# typography

主主题没有传入自建 Typography 数值表，而是使用 MaterialExpressiveTheme 默认；本轮未把依赖默认字号伪写成项目定义。可确认的组标题为 bodyMedium.copy(color=onSurfaceVariant,fontWeight=SemiBold)。sp 会受 Android 字体缩放影响；移植时保留角色与缩放能力，不能把 dp 间距当成字号。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt:37` — `BaseTachiyomiTheme`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt#L37)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/theme/Typography.kt:9` — `Typography.header`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/theme/Typography.kt#L9)
