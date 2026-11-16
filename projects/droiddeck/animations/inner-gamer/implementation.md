# 实现原理

key(speed)重建周期但起始hue从Themes.rgbHue保留；infiniteTransition线性推进360，stepped=floor((hue%360)/3)*3，再SideEffect写入状态。Palette生成仍执行readable与渐变对比度修正，故实际primary不是未经修正的HSV原值。

## 生命周期与快速触发

离开主题移除周期组合；app Motion.scale0不建InnerGamerCycle。系统时钟动画比例另生效。代码没有本组件AppState后台监听，不能宣称显式后台停帧。

## 框架无关行为

输入：主题选择inner_gamer，speed1..10，Motion.scale非0

状态从 `{"hue": "remembered rgbHue"}` 到 `{"hue": "start+360 loop; stored in 3 degree steps"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

关闭应用/系统动画可静止；动态色仍须维护文字配对。4.5算法覆盖onPrimary渐变样本，不代表其他角色全部合规。

## 性能（静态分析，无 FPS 或内存实测）

3度量化减少整组palette状态变动次数（每理想周期120个档位），但infiniteTransition仍按帧推进，SideEffect及校正计算不是只跑120帧。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/Theme.kt:211` — `private fun InnerGamerCycle`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Theme.kt#L211)
- [`app/src/main/java/com/droiddeck/launcher/ui/ThemeColors.kt:11` — `internal object ThemeColors`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/ThemeColors.kt#L11)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
