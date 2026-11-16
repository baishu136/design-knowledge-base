# materials

表面层次主要用background/surface/surfaceVariant和line/line2。PrimaryButton用primary→primary2渐变，hot时阴影elevation目标14dp，rest6dp，并将ambient/spot颜色设signal；这是阴影变化，不只是scale的合成成本。

LiftHero用Canvas Path绘制曲边与rim、黑色.42遮罩，背景按1-.05*sink缩放；PageFlood用圆角路径clip封面并按cover比例缩放图像。CardDetailHost明确创建Offscreen图层用于顶部DstIn渐隐。这些效果不能笼统称作“模糊玻璃”或假设全部零重绘。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt:176` — `internal fun LiftHero`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt:80` — `internal fun PageFlood`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt#L80)
- [`app/src/main/java/com/droiddeck/launcher/ui/CardDetailHost.kt:60` — `internal fun CardDetailHost`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/CardDetailHost.kt#L60)
