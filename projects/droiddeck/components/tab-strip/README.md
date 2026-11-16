# TabStrip与BumperKey

`droiddeck.component.tab-strip` · source-verified · runtime unverified

## 用途

手柄LB/RB与触摸横向tab

## 结构

Row：可选LB→可滚动SelectableGroup→tabs→RB

## 参数

外12dp/内9dp圆角，padding3dp，gap6dp；字compact12/常规14sp，键帽触摸盒44dp

## 交互状态

on/hot/focused，溢出后tight padding16→10，选中bringIntoView

## 输入、输出与状态

tabs,selected,onSelect,focusRequesters,bumpers,compact

## 反馈与生命周期

Role.Tab/selected语义，环绕索引；tab不会由ChipGlide统一动画，本文件使用直接背景+glideBorder

## 框架无关迁移

保留可达选中项与空列表约束；不要仅复制LB/RB标签

## 最小用法（说明性片段，未编译）

```
TabStrip(listOf("Games","Setup"),selected,{ selected=it })
```

## 限制

tabs为空却启用模运算bumpers

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt:167` — `internal fun TabStrip`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/SettingsWidgets.kt#L167)
