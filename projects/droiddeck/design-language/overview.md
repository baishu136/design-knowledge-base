# overview

源码与官方themes.md：Palette定义五层表面/边界、两级文本、primary/primary2/onPrimary/signal/good/error。主动作按钮使用渐变；焦点通过独立覆盖层滑移，手柄输入并非触摸反馈的附属物。

分析：辨识度来自深色层次、鲜明动作渐变、焦点的空间连续性以及按钮扩张成下一场景的因果关系。复现应保留焦点可见性、手柄/触摸双路径和主题配对；游戏封面、Steam商标及Linux桌面不是可随意迁移的原生UI资产。不要简化为“全局蓝黑Steam风”。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/Theme.kt:167` — `fun DroidDeckTheme`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Theme.kt#L167)
- [`docs/development/themes.md:1` — `# Themes`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/docs/development/themes.md#L1)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:189` — `private fun Modifier.focusGlideOverlay`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L189)
