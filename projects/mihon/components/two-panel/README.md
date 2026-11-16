# TwoPanelBox

`mihon.component.two-panel` · source-verified · runtime unverified

## 用途

大屏主从信息并列

## 结构

BoxWithConstraints→TopStart Box + TopEnd Box

## 参数

可用宽扣除Insets；首列不超过450dp，末列余量；无内建断点

## 交互状态

宽度变化重算；无拖拽或动画

## 输入、输出与状态

startContent、endContent、modifier、contentWindowInsets

## 反馈与生命周期

布局方向感知start/end；不是固定left/right

## 框架无关迁移

available=W-insets；a=min(available/2,450dp)；b=available-a

## 最小用法（说明性片段，未编译）

```
TwoPanelBox(startContent={ Text("Info") }, endContent={ Text("Chapters") })
```

## 限制

窄屏自动变单栏；调用方先判断

## 源码

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/TwoPanelBox.kt:19` — `fun TwoPanelBox`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/TwoPanelBox.kt#L19)
