# icons

启动器使用Compose Material Icons，PrimaryButton接受ImageVector，可选图标尺寸普通17dp/large20dp且contentDescription=null（同一按钮已有文字）。设置导航的LB/RB是44dp触摸区内的文字键帽，提供contentDescription且不再进入普通焦点序列。LogoThrobber的品牌形状是Canvas路径，并非可无署名复用的通用加载图标；本库只记录行为，不搬运商标图像。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt:167` — `internal fun TabStrip`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt#L167)
- [`app/src/main/java/com/droiddeck/launcher/ui/Throbber.kt:24` — `internal fun LogoThrobber`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Throbber.kt#L24)
