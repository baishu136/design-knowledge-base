# PrimaryButton

`droiddeck.component.primary-button` · source-verified · runtime unverified

## 用途

手柄/触摸共用的启动主动作

## 结构

Row+InteractionSource→graphicsLayer→gradient→glideBorder→Icon/Text

## 参数

Shape12/pill；minHeight48/compact44/pill40dp；字15/17/12sp；图标17/20dp

## 交互状态

enabled、pressed、hot、LaunchOrigin.flooding隐藏原按钮；禁用不是单纯alpha降低

## 输入、输出与状态

text,enabled,main,compact,large,icon,fill,onClick；main登记primary FocusRequester

## 反馈与生命周期

按压优先scale.955；hot1.02；点击记录bounds供LaunchFlood

## 框架无关迁移

把原点登记、焦点模型与视觉动作分层，业务禁用条件不能只传给动画

## 最小用法（说明性片段，未编译）

```
PrimaryButton("Play", main=true, enabled=ready) { launch() }
```

## 限制

依赖私有LocalFrontFocus/LaunchOrigin却声称独立可编译

## 源码

- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt:176` — `internal fun PrimaryButton`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndWidgets.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
