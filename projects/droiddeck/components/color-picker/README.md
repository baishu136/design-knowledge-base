# ColorPickerDialog

`droiddeck.component.color-picker` · source-verified · runtime unverified

## 用途

自定义渐变和True Black强调色

## 结构

AppDialog→旧新swatch→触摸色轮→三ValueSlider→hex→OK/Cancel

## 参数

maxWidth460dp；色轮168dp；ColorCube44dp；Swatch48dp；hue0..360 step5，S/V0..100 step2

## 交互状态

输入合法/非法、触摸调整、controller调整、确认/关闭

## 输入、输出与状态

title,initial:Int,onDismiss,onApply(Int)；parseHex仅3/6位，可选#

## 反馈与生命周期

非法hex禁用OK；色轮是触摸路径，滑杆/hex提供其他输入方式

## 框架无关迁移

保留原始候选与确认应用分离；Palette校正可改变所见最终颜色，不将picker原值当最终主题值

## 最小用法（说明性片段，未编译）

```
ColorPickerDialog("Primary",initial,onDismiss={open=false},onApply={ save(it) })
```

## 限制

需要alpha/8位hex的编辑器，原实现只支持不透明色

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/ColorPickerDialog.kt:62` — `internal fun ColorPickerDialog`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/ColorPickerDialog.kt#L62)
- [`app/src/main/java/com/droiddeck/launcher/ui/ThemeColors.kt:11` — `internal object ThemeColors`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/ThemeColors.kt#L11)
