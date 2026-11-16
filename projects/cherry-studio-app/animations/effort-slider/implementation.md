# 实现原理

trackXToFraction先归一化；magnetize改变视觉position；nearestStopIndex变化时才runOnJS(onCommit)。onFinalize选最近档位，按reducedMotion立即赋值或withTiming。

## 生命周期与快速触发

onFinalize包括取消路径；disabled禁用gesture。连续拖动用shared values更新，不为每帧建立JS状态；外部值同步仍需组件协作。

## 框架无关行为

输入：Pan minDistance0；programmatic value change由组件处理

状态从 `{"position": "current fraction"}` 到 `{"position": "nearest stop fraction"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：begin/update seek；finalize吸附；跨档commit去重。

## 无障碍

reducedMotion参数直接跳最终值；手势hook本身不提供屏幕阅读器adjustable action，不能单独用作完整可访问slider。

## 性能（静态分析，无 FPS 或内存实测）

UI worklet负责每帧，JS仅跨档commit。大量档位或昂贵onCommit仍需限流/分离副作用。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/frontend/features/chat/components/ChatInput/effortSlider/hooks/useEffortSliderGesture.ts:38` — `export function useEffortSliderGesture`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/features/chat/components/ChatInput/effortSlider/hooks/useEffortSliderGesture.ts#L38)
- [`src/frontend/features/chat/components/ChatInput/effortSlider/utils/constants.ts:9` — `export const effortSliderSnapTiming`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/features/chat/components/ChatInput/effortSlider/utils/constants.ts#L9)
