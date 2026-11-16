# spacing

核心形状Shape12=12dp、Shape14=14dp、Shape16=16dp；面板SheetCorner18dp、左右SheetInset12dp。TabStrip外框12dp、内tab9dp、内层padding3dp、条间gap6dp。局部Button有复杂start/end/top/bottom参数，并非全仓8点网格。

LauncherLayout先测量导航，再扣除其宽或高以及1dp分隔线，内容拿到剩余固定Constraints。600dp为isNarrowScreen门槛；520dp为NarrowPaneWidth常量，两者不可互换。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt:167` — `internal fun TabStrip`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt#L167)
- [`app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt:176` — `internal fun LiftHero`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/Layout.kt:23` — `internal fun LauncherLayout`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Layout.kt#L23)
