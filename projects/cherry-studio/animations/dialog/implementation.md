# 实现原理

Tailwind动画工具由data-state驱动；Content必须为Portal直接子元素，否则Radix Presence拿不到DOM ref就可能过早卸载。motion=fade-scale在本版本只关闭directional类，不能凭名称写出scale(.95)。

## 生命周期与快速触发

Radix presence延迟卸载；KeyboardLayer释放跟焦点恢复协作。Imperative host卸载延迟另外定义，不能等同CSS时长。

## 框架无关行为

输入：Radix data-state open/closed

状态从 `{"overlay_alpha": 0, "content_alpha": 0, "content_translateY": "bottom-4"}` 到 `{"overlay_alpha": 0.5, "content_alpha": 1, "content_translateY": 0}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

motion-reduce:animate-none；保留Dialog焦点和Escape行为需Radix/KeyboardLayer协作，不等于复制CSS即可实现模态框。

## 性能（静态分析，无 FPS 或内存实测）

opacity/translate适合局部复合；shadow-xl与大内容合成层增加开销。无实际层树或帧时间数据。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`packages/ui/src/components/primitives/dialog.tsx:87` — `function DialogContent(`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/dialog.tsx#L87)
