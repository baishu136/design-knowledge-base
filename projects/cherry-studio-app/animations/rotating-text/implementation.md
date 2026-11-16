# 实现原理

独立translateY spring和opacity timing；新短语若完全不可见则重置入场边，否则保持当前位置再设目标；测量层保证尺寸。弹簧时长未显式指定，420ms只能作为源码注释中的近似，不记为固定duration。

## 生命周期与快速触发

每次effect先cancelAnimation两轨；源码注释称保留position/velocity，但显式取消后的速度连续性未运行确认，不保证C1连续。

## 框架无关行为

输入：active phrase / direction / measured / still

状态从 `{"translateY": "±8", "opacity": 0}` 到 `{"translateY": 0, "opacity": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

useReducedMotion或isEnabled=false走still；非active短语屏蔽无障碍后代。

## 性能（静态分析，无 FPS 或内存实测）

transform/opacity适合局部复合；同时挂载多个短语与测量文本有额外内存/排版成本。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`packages/ui/src/motion.ts:11` — `export const easing`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/motion.ts#L11)
- [`packages/ui/src/components/text-animation/text-animation.tsx:312` — `function RotatingPhrase`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/text-animation/text-animation.tsx#L312)
