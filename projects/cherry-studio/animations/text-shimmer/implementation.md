# 实现原理

渐变中间foreground、两端foreground25%透明混合；移动background-position而非文字几何。will-change声明提示优化，并不保证GPU复合。

## 生命周期与快速触发

类移除停止CSS动画；再次附加通常重启。没有自定义相位保存。

## 框架无关行为

输入：animation-shimmer class attached

状态从 `{"backgroundPosition": "200% 0"}` 到 `{"backgroundPosition": "-200% 0"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

CSS基础类没有通用reduce-motion覆盖；PlaceholderShimmerText消费者另加motion-reduce:!animate-none。SessionItem/FileTree等其他消费者需分别检查，不能泛化为全部覆盖或全部缺失。forced-colors/打印未实测。

## 性能（静态分析，无 FPS 或内存实测）

background-position/clip:text可能逐帧paint；长文本或多行大量实例比小图标旋转更昂贵。没有基准数据。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/renderer/assets/styles/animation.css:236` — `@keyframes animation-shimmer`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/assets/styles/animation.css#L236)
- [`src/renderer/components/chat/messages/blocks/PlaceholderShimmerText.tsx:3` — `export function PlaceholderShimmerText`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/messages/blocks/PlaceholderShimmerText.tsx#L3)
