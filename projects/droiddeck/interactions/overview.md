# overview

手柄A确认只处理首次ACTION_DOWN，B/Back返回、LB/RB可切tab；hover/focus共同形成hot，而按压独立。TabStrip对选中项bringIntoView，提供Role.Tab/selectableGroup。焦点滑移层按窗口View身份绑定，弹窗有FocusGlideWindow避免跨窗口错位。

Motion.refresh读取应用animationsEnabled和Android ANIMATOR_DURATION_SCALE；部分入口refresh并不等于所有设置变化立即有监听，本轮未断言热更新。LiftHero在ON_STOP清open/shown/launching；关闭、手势取消和launching有不同路径。LaunchFlood覆盖阶段主动consume全部触摸，是源实现的暂时输入门闩，不应给所有目标UI普遍增加阻塞。

移植时必须分别验证触摸、键盘/手柄和读屏，不把焦点高亮的存在等同所有无障碍任务完成。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt:167` — `internal fun TabStrip`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt#L167)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
- [`app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt:176` — `internal fun LiftHero`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/LaunchFlood.kt:108` — `internal fun LaunchFlood`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LaunchFlood.kt#L108)
- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:120` — `internal fun Modifier.glideBorder`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L120)
