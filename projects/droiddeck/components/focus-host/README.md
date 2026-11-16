# FocusGlideHost与glideBorder

`droiddeck.component.focus-host` · source-verified · runtime unverified

## 用途

整窗口手柄/键盘焦点提示

## 结构

Host管理hot来源栈；Modifier登记LayoutCoordinates/Shape；drawWithContent画统一ring

## 参数

2dp热边/1dp静边；默认fill.14，focusGlide可设0；远距360dp策略

## 交互状态

首次、方向移动、连按、远距droplet、布局跟随、hidden、跨窗口回退

## 输入、输出与状态

glideBorder(hot,shape,hotColor,restColor,hotWidth,restWidth,hotFillAlpha)；Host/Window组合边界

## 反馈与生命周期

claim/release维护热源；VeilRing遮蔽临时效果，坐标attach校验防读废布局

## 框架无关迁移

需要窗口坐标系与焦点生命周期，不能把所有控件的border设为同一位置

## 最小用法（说明性片段，未编译）

```
FocusGlideHost { item(Modifier.focusGlide()) } // 私有项目环境用法
```

## 限制

跨Activity/Popup直接共享同一个View host

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:189` — `private fun Modifier.focusGlideOverlay`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L189)
- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:120` — `internal fun Modifier.glideBorder`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L120)
