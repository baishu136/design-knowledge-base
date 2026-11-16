# 实现原理

animateFloatAsState scale以pressed优先；shadow独立tween。graphicsLayer再clip按钮形状、画渐变、glideBorder；普通按压不必引入整页LaunchFlood，但点击会登记原点供后续使用。

## 生命周期与快速触发

目标切换由animateFloatAsState接管；enabled时hot才生效，disabled用surfaceVariant渐变及line2边框。LaunchOrigin.flooding匹配此按钮时alpha0避免复制画面叠在原件。

## 框架无关行为

输入：InteractionSource pressed与rememberHot且enabled

状态从 `{"scale": 1, "shadow_dp": 6}` 到 `{"pressed_scale": 0.955, "hot_scale": 1.02, "hot_shadow_dp": 14}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

Role.Button且enabled控制点击；键盘主动作FocusRequester在组件挂卸时登记计数。scale0不移除焦点语义。

## 性能（静态分析，无 FPS 或内存实测）

scale通常局部图层，彩色阴影仍可能增加绘制/合成开销；不要按scale成本评估整个效果。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
