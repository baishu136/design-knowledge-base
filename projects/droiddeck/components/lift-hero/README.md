# LiftHero

`droiddeck.component.lift-hero` · source-verified · runtime unverified

## 用途

Hero页面的设置/启动复合层

## 结构

背景/遮罩→Canvas面板壁→tabs与rows→联动play按钮→分段piece

## 参数

sheetInset12、corner18、pieces12；sheetTop=max(paneH/6,minAbove+buttonH/2-ride)

## 交互状态

open/shown/dragging/launching/stopped；DropSheet仲裁

## 输入、输出与状态

key,tabs,onOpen,onPrimary,background,words,button,rows,onOpenChange,drop

## 反馈与生命周期

open时移焦点，Back关闭；ON_STOP清临时状态；启动先fold再onPrimary

## 框架无关迁移

拆成geometry、presentation状态与业务启动回调，保留手势/焦点恢复顺序

## 最小用法（说明性片段，未编译）

```
LiftHero(key="game", tabs=tabs, onOpen={}, onPrimary=launch, background=bg, words=title, button=play, rows=settings)
```

## 限制

普通弹窗无需移植整套Hero状态依赖

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt:176` — `internal fun LiftHero`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt#L176)
