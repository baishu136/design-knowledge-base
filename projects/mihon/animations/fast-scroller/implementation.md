# 实现原理

DROP_OLDEST 容量1事件流经sample(.1.seconds)，collectLatest 取消上次等待/淡出；允许显示时snapTo(1)，delay(2.seconds) 后animateTo(0)。graphicsLayer读取alpha，placement更新thumb位置。

## 生命周期与快速触发

collectLatest 用新事件替换旧淡出任务；remember Animatable 保留当前值。LaunchedEffect 离开组合时取消。

## 框架无关行为

输入：scrolled SharedFlow；拖动thumb

状态从 `{"alpha": 0}` 到 `{"scrolling_alpha": 1, "idle_alpha": 0}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：拖动累计delta并coerceIn轨道；scrollTo对应比例；释放后显隐仍由事件流管理。

## 无障碍

源码设置 systemGestureExclusion 仅在必要时启用；thumb拖动键盘与无障碍替代路径仍需专项审查。

## 性能（静态分析，无 FPS 或内存实测）

在placement读取scroll state的注释和代码可确认；sample限制事件处理，不表示以10FPS绘制。拖动scrollTo可能触发Lazy内容加载。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/VerticalFastScroller.kt:189` — `val alpha = remember`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/VerticalFastScroller.kt#L189)
