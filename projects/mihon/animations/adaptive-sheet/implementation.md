# 实现原理

AnchoredDraggableState 初始1，容器测量后建0@0与1@height两个锚点；LaunchedEffect animateTo(0)。nested scroll 在向上预滚动/向下后滚动消费位移，fling settle 使用 sheetAnimationSpec。平板 animateFloatAsState 只驱动 alpha。

## 生命周期与快速触发

手机 observe settledValue，drop首值后只有到1才通知；协程随组合离开取消。平板关闭回调立即执行，没有等待 alpha=0 的门闩。

## 框架无关行为

输入：进入组合；返回/背景点击；纵向拖拽释放

状态从 `{"phone_offset": "containerHeight", "tablet_alpha": 0}` 到 `{"phone_offset": 0, "tablet_alpha": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：UserInput delta→dispatchRawDelta；释放后settle；56dp位置阈值。速度阈值来自依赖，未知。

## 无障碍

BackHandler 及系统 Dialog 由包装层参与；本文件未显式读取减少动态效果。依赖/系统动画比例未验证。

## 性能（静态分析，无 FPS 或内存实测）

手机 offset 在布局 placement 阶段更新；可避免每帧重测整个内容，但仍需处理位置更新。大内容组合和嵌套滚动成本取决于内容。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt:53` — `fun AdaptiveSheet`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt#L53)
