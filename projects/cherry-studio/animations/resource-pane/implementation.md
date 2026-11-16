# 实现原理

AnimatePresence initial=false；motion.div animate依据open。hasOpened让首次打开后的children继续保留；closed态width0/opacity0而不是每次重挂载。isResizing直接transition duration0。

## 生命周期与快速触发

Motion新目标接管当前值；React保留树维持列表状态。关闭inert/aria-hidden即刻变化，不等待视觉结束。

## 框架无关行为

输入：open Boolean；isResizing

状态从 `{"width": 0, "opacity": 0}` 到 `{"width": "resolvedWidth", "opacity": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

有键盘splitter props；本组件未直接useReducedMotion，本轮不保证宿主全局覆盖。

## 性能（静态分析，无 FPS 或内存实测）

width动画必须重排相邻主内容，文本折行/虚拟列表测量可能昂贵；暂停复杂编辑器resize工作或缩短过渡是目标项目优化建议，非原实现已完成。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/renderer/components/chat/shell/PageSidebar.tsx:28` — `export function PageSidebar`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/PageSidebar.tsx#L28)
- [`src/renderer/components/chat/shell/paneLayout.ts:5` — `export const CHAT_SHELL_TRANSITION`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/paneLayout.ts#L5)
