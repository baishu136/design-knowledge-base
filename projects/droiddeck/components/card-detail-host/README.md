# CardDetailHost

`droiddeck.component.card-detail-host` · source-verified · runtime unverified

## 用途

从游戏grid进入详情且保留返回画面

## 结构

Offscreen渐隐Host→保留的grid Column→shown详情树→PageFlood

## 参数

gridScale.95；fade顶部14dp；PAGE_RETURN_MS900基础窗口

## 交互状态

open/shown/leaving/from；grid焦点在covering时拒绝enter

## 输入、输出与状态

open:String?,detailScroll,gridScrolled,onDetailFocus,wrap,grid,detail及bleedInsets

## 反馈与生命周期

打开读取StoresMotion卡片原点，关闭延迟清shown，重开取消旧effect

## 框架无关迁移

稳定身份与可测量卡片原点优先，无法定位时必须有回退

## 最小用法（说明性片段，未编译）

```
CardDetailHost(open,scroll,{false},{},grid={ Grid() },detail={ key -> Details(key) })
```

## 限制

无限保留所有详情或跨Window原点未换坐标

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/CardDetailHost.kt:60` — `internal fun CardDetailHost`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/CardDetailHost.kt#L60)
- [`app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt:80` — `internal fun PageFlood`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt#L80)
