# 实现原理

外层只负责透明度，直接子.animation-selector-shell-panel负责translate/scale，避免不同animation覆盖同一个transform。transform-origin用Radix Popover计算变量。

## 生命周期与快速触发

CSS data-state切换；SelectorShell声明destroy/lazy-keep两种挂载策略并用useExitPresence保留退出。lazy-keep仅建议高频列表，具体快速连击/焦点恢复未运行。

## 框架无关行为

输入：data-selector-shell-content的data-state和data-side

状态从 `{"scale": 0.95, "offset": "±.5rem", "alpha": 0}` 到 `{"scale": 1, "offset": 0, "alpha": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

prefers-reduced-motion下外层/面板同时animation:none及transform:none；键盘导航由选择组件负责。

## 性能（静态分析，无 FPS 或内存实测）

transform/opacity为主；避免把尺寸计算放入每帧JS，锚点定位仍有布局测量。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/renderer/assets/styles/animation.css:170` — `@keyframes animation-selector-shell-panel-enter`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/assets/styles/animation.css#L170)
- [`src/renderer/components/SelectorShell.tsx:41` — `const SELECTOR_CONTENT_POSITION_CLASS`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/SelectorShell.tsx#L41)
