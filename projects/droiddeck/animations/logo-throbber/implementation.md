# 实现原理

单线性loop驱动三组分段函数；bend在.10..24上升、.76..90下降；turn在.16..84做360；ball在.12..30缩小、.70..88恢复。remember缓存Path对象，几何点列表由LogoShape预建，Canvas每帧reset/rebuild path。

## 生命周期与快速触发

still将绘制p强制0，但rememberInfiniteTransition的建立在still判断之前；仅从running=false不能证明clock停止。离开组合才解除本循环生命周期。

## 框架无关行为

输入：组合挂载并running且Motion.scale非0

状态从 `{"phase": 0, "ball_scale": 1, "bend": 0}` 到 `{"phase": "repeat1→0", "ball_scale": 1, "bend": 0}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

Motion.scale0显示静止图案；本Canvas函数自身无progressbar语义参数，使用者需配文字/状态。

## 性能（静态分析，无 FPS 或内存实测）

缓存Path减少分配，但顶点计算和path绘制仍逐帧发生；不是Shader，不能宣称所有计算在GPU。无实际数据。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/Throbber.kt:24` — `internal fun LogoThrobber`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Throbber.kt#L24)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
