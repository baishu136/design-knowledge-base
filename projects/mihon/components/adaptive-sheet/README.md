# AdaptiveSheet

`mihon.component.adaptive-sheet` · source-verified · runtime unverified

## 用途

手机底部面板/平板居中面板

## 结构

Dialog包装→全屏Box→Surface→content

## 参数

maxWidth460dp；extraLarge形状；surfaceContainerHigh；平板垂直padding16dp

## 交互状态

open、dragging、settling、dismissed；无hover状态定义

## 输入、输出与状态

isTabletUi、enableImplicitDismiss、onDismissRequest、modifier、content

## 反馈与生命周期

见adaptive-sheet动画；平板关闭直接回调

## 框架无关迁移

把两种呈现规则和dismiss生命周期分离；Insets由目标平台负责

## 最小用法（说明性片段，未编译）

```
AdaptiveSheet(isTabletUi=false, enableImplicitDismiss=true, onDismissRequest={ open=false }) { Text("Options") }
```

## 限制

精确多档高度控制

## 源码

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt:53` — `fun AdaptiveSheet`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/AdaptiveSheet.kt#L53)
