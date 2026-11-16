# 实现原理

useLayoutEffect比较前后placement，只标记home-to-docked；属性函数添加CSS class；useEffect在280ms后清标记。220ms绘制时长与280ms清理窗口应分开。

## 生命周期与快速触发

effect cleanup清timer；反向placement直接清transition，不播放相反动画。

## 框架无关行为

输入：previousPlacement=home且placement=docked

状态从 `{"translateY": -18, "scale": 0.985, "opacity": 0.98}` 到 `{"translateY": 0, "scale": 1, "opacity": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

prefers-reduced-motion时取消动画与transform。

## 性能（静态分析，无 FPS 或内存实测）

只变transform/opacity，但布局位置本身由业务先改变，本动画并非FLIP测量任意距离。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/renderer/assets/styles/animation.css:81` — `@keyframes animation-chat-composer-dock-down`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/assets/styles/animation.css#L81)
- [`src/renderer/components/chat/motion/composerDockMotion.ts:9` — `export function useComposerDockMotionTransition`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/motion/composerDockMotion.ts#L9)
