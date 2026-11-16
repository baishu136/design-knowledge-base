# overview

面板输入 enableImplicitDismiss 控制返回/手势入口；手机在隐藏锚点 settledValue=1 后通知 dismiss。平板分支 targetAlpha=0 后立即调用 onDismissRequest，调用方若卸载，淡出不一定完整可见，不能宣称两端都有完整350ms退出。快滚条只有可见且列表不在滚动时装配拖拽；拖拽越界值限制在轨道内。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt:53` — `fun AdaptiveSheet`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt#L53)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/VerticalFastScroller.kt:189` — `val alpha = remember`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/VerticalFastScroller.kt#L189)
