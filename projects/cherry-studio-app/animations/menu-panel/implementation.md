# 实现原理

一个shared progress连接容器几何与内容轨道。打开使用y控制点1.25的超调Bezier，关闭用settle。外壳向上展开时top随animatedHeight变化，以锚边保持视觉连接。不要把声明的menuFadeMotion200ms误记为这个useMenuMotion的独立淡入轨道。

## 生命周期与快速触发

cleanup cancelAnimation并使旧finishExit失效；完成回调仅finished为真时runOnJS卸载。未完成退出重开从当前progress继续。

## 框架无关行为

输入：isOpen且isMeasured；关闭请求

状态从 `{"progress": 0, "size": [32, 32], "opacity": 0}` 到 `{"progress": 1, "size": "measured", "opacity": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

useReducedMotion打开直接1，关闭duration0；关闭时立即移除交互和可访问子树。

## 性能（静态分析，无 FPS 或内存实测）

width/height会触发布局；blur可能增加离屏成本。panel固定内容宽、测量变化阈值>1减少回写抖动，但不等于零布局开销。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`packages/ui/src/motion.ts:11` — `export const easing`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/motion.ts#L11)
- [`packages/ui/src/components/menu/menu-motion.ts:6` — `export const menuOpenMotion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-motion.ts#L6)
- [`packages/ui/src/components/menu/use-menu-motion.ts:13` — `export function useMenuMotion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/use-menu-motion.ts#L13)
- [`packages/ui/src/components/menu/menu-panel.tsx:16` — `export function MenuPanel`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-panel.tsx#L16)
- [`packages/ui/src/components/menu/menu-content.tsx:19` — `export function MenuContent`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-content.tsx#L19)
