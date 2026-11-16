# colors

固定预设含Graphite、Paper、Icon Blue、Electric和White Red；Paper实际是黑底白强调，不能按名称当作浅主题。White Red才是明确浅底红强调。DroidDeckTheme始终调用darkColorScheme映射Palette，即便Palette是浅色；不能从构造函数名推断最终背景。

Gradient通过readable把亮度过低的输入提升；inkFor在深墨#03111F/白之间按两端最差对比度选择，再fitTo和0..32渐变采样修正，目标4.5并留.02余量。该算法不是全部文字、边界和系统控件已通过无障碍认证的证据。True Black另由函数生成纯黑surface，动态主题须保留参数，未在tokens.json伪造一组不变颜色。Inner Gamer在色环上转动，经同一校正算法生成整组角色。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/Theme.kt:167` — `fun DroidDeckTheme`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Theme.kt#L167)
- [`app/src/main/java/com/droiddeck/launcher/ui/ThemeColors.kt:11` — `internal object ThemeColors`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/ThemeColors.kt#L11)
- [`app/src/main/java/com/droiddeck/launcher/ui/Theme.kt:211` — `private fun InnerGamerCycle`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Theme.kt#L211)
