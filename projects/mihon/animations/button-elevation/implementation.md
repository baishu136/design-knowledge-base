# 实现原理

animateElevation 根据 to 优先、否则 from 选 TweenSpec；两者都无时 snapTo。默认交互进入120ms、离开150ms，hover离开120ms。原文件是Compose M3复制代码且保留AOSP版权。

## 生命周期与快速触发

Animatable.animateTo 的协程取消与新目标协作；不能建立每次press排队的时间轴。

## 框架无关行为

输入：Interaction流的前后态

状态从 `{"elevation": "from interaction target"}` 到 `{"elevation": "to interaction target"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

同时处理FocusInteraction；disabled/未知态snap，无局部Reduce Motion判断。

## 性能（静态分析，无 FPS 或内存实测）

阴影高度改变可能增加渲染负担；不是单纯transform，需目标设备实测。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/util/Elevation.kt:50` — `animateElevation`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/util/Elevation.kt#L50)
- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/material/Button.kt:283` — `val animatable = remember`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/material/Button.kt#L283)
