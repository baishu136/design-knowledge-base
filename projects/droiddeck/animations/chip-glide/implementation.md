# 实现原理

同一Canvas画背景；index决定lead/end与trail/start谁先走，尾缘delay40ms后spring。glideShape在pinch=0使用边缘，在pinch=1变到中心±drop。当前ChipGlide只将pinch归0，不能据此宣称每次必有pinch收球阶段。

## 生命周期与快速触发

LaunchedEffect键改变取消旧协程；初次/同index/无上次或scale0直接snap。看不见或shown<.5先把几何移到目标以避免看见穿越。

## 框架无关行为

输入：index、at Rect、visible、Motion.scale

状态从 `{"start_end": "previous selection edges"}` 到 `{"start_end": "new selection edges", "pinch": 0}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

Keyboard输入模式时此ChipGlide本身不显示，交给其他焦点反馈；不能把胶囊背景当唯一可访问选中语义。

## 性能（静态分析，无 FPS 或内存实测）

Canvas绘制替代每个tab独立布局动画；Rect测量与Compose状态仍需布局消费者配合。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/SharedMotion.kt:44` — `internal fun BoxScope.ChipGlide`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/SharedMotion.kt#L44)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
