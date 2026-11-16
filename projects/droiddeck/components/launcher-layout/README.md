# LauncherLayout与AppScale

`droiddeck.component.launcher-layout` · source-verified · runtime unverified

## 用途

底部/侧边导航与用户界面缩放

## 结构

自定义Layout测navigation→1dp line→剩余内容，placeRelative支持方向

## 参数

narrowScreen<600dp；NarrowPaneWidth520；AppScale选75/85/100/115/125/150%

## 交互状态

bottomNavigation切向；宽高约束重算；scaled density和configuration同步

## 输入、输出与状态

bottomNavigation,divider,navigation,content,modifier；scaledAppDensity/scaledAppConfiguration

## 反馈与生命周期

dualScreen调用处可强制侧栏；不是仅由orientation或600自动决定

## 框架无关迁移

迁移时保留字体缩放、导航占位与断点基准；勿单独scale绘制画面让命中框失配

## 最小用法（说明性片段，未编译）

```
LauncherLayout(bottomNavigation=true,divider=pal.line,navigation={ Nav() },content={ Page() })
```

## 限制

直接把Android Configuration dp当浏览器CSS px断点

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/Layout.kt:23` — `internal fun LauncherLayout`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/Layout.kt#L23)
- [`app/src/main/java/com/droiddeck/launcher/ui/AppScale.kt:8` — `internal fun scaledAppDensity`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/AppScale.kt#L8)
