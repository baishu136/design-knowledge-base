# 实现原理

每条边计算到屏幕对应边的travel与lead=travel/far，距离越远延迟越少且stiffness越高。边首次>=1后reached保持covered判定不随回弹反复变化；四边均触达即回调onCovered，不等待所有spring settle。圆角以sin(pi*mean)中间鼓起、渐变两端以mix=min(mean*2,1)向signal合并。

## 生命周期与快速触发

LaunchedEffect/page生命周期取消；rememberUpdatedState保持回调新鲜。四边reached只在本次记忆状态中保留；重新启动业务需新实例。scale0立即覆盖并通知。

## 框架无关行为

输入：LaunchOrigin取到有效按钮bounds；Canvas测量完成

状态从 `{"edge_progress": [0, 0, 0, 0], "from": "button rect"}` 到 `{"edge_progress": [1, 1, 1, 1], "covered": true}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

VeilRing暂时遮去焦点；覆盖Canvas消费触摸，必须限定在真实启动交接；scale0走snap。

## 性能（静态分析，无 FPS 或内存实测）

每帧Canvas渐变+圆角重绘，目标变化不是系统共享元素。平均进度回调可能增加重组；大屏和背景合成面积需实测。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/LaunchFlood.kt:108` — `internal fun LaunchFlood`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LaunchFlood.kt#L108)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
