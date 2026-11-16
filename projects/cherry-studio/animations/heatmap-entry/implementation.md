# 实现原理

本条提取CSS基础轨道。调用点可能额外设置animationDelay；本轮没有将业务错峰公式确认为项目全局规范。

## 生命周期与快速触发

由CSS生命周期控制，非弹簧；重加类是否重播取决于DOM/浏览器样式刷新。

## 框架无关行为

输入：animation-usage-heatmap-cell-enter class attached

状态从 `{"scale": 0.7, "opacity": 0}` 到 `{"scale": 1, "opacity": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

prefers-reduced-motion时transform:none/animation:none。

## 性能（静态分析，无 FPS 或内存实测）

单格transform/opacity较轻，大量独立格子仍可能提高图层与调度成本；逐个will-change不是免费优化。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/renderer/assets/styles/animation.css:97` — `@keyframes animation-usage-heatmap-cell-enter`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/assets/styles/animation.css#L97)
