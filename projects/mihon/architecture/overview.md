# overview

presentation-core 放跨页面基础组件和主题扩展；app 的 eu/kanade/presentation 放具体功能的 Compose UI、导航包装；ui/reader 仍有传统 View 阅读器。domain/data/source-api/source-local 是数据和来源层，不应直接复制进通用组件。Navigator 的 saveableState 包住屏幕内容，返回由 BackHandler 分发。

迁移优先抽出颜色角色、几何公式和状态机，再替换 Voyager、Injekt/DI、业务 preferences；保留这些私有依赖会使“最小示例”无法独立使用。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/eu/kanade/presentation/util/Navigator.kt:39` — `DefaultNavigatorScreenTransition`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/util/Navigator.kt#L39)
- [`app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt:37` — `BaseTachiyomiTheme`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt#L37)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt:53` — `fun AdaptiveSheet`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt#L53)
