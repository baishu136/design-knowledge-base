# typography

Theme中的ContentDirected由Material Typography默认角色派生，只改TextDirection.Content，不是完整自建字体字号表。局部实际组件：Title26sp Bold，Lede/Note13sp；章节标题12sp SemiBold，字距1.5sp；PrimaryButton large17/普通15/compact12sp、字距.5sp。这里只将这些局部值标为组件Token，不宣称全仓统一13/26刻度。

AppScale把Density乘用户百分比但保留fontScale，同时反向调整Configuration中的screenWidthDp等；字号和断点判断因此都受appScale影响。FittedLabel测量单行标签并以.5sp减小，最低10sp；长字符串适配与大字体可读性需实机检查，不能默认所有文本都自适应。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/Theme.kt:167` — `fun DroidDeckTheme`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Theme.kt#L167)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:91` — `internal fun Title`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L91)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/AppScale.kt:8` — `internal fun scaledAppDensity`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/AppScale.kt#L8)
