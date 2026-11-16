# 实现原理

每次请求取消旧RAF，不排队；固定startOffset，对动态target每帧求值。frame>=frames时再取一次target并精确写入；完成仅正常终止回调。不是dt驱动，60Hz约833ms仅为理论换算，120Hz约417ms，不是FPS实测。

## 生命周期与快速触发

cancel取消RAF清animating；unmount cleanup；DOM消失停止；用户输入中断需调用方主动cancel。

## 框架无关行为

输入：controller.scrollTo(getTargetOffset,options)

状态从 `{"offset": "current scrollTop"}` 到 `{"offset": "latest getTargetOffset()"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

hook没有读取prefers-reduced-motion，调用方应决定直接跳转；这是迁移建议。

## 性能（静态分析，无 FPS 或内存实测）

每帧scrollTop写入可导致滚动/虚拟列表更新；getTargetOffset若读取昂贵DOM几何会引起同步布局。高刷新屏幕时长会变，应在需要恒定节奏时改为时间驱动并标注adapted。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts:58` — `export function useSmoothScrollAnimation`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts#L58)
