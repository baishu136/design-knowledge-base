# CherryUI Button

`cherry-studio-app.component.button` · source-verified · runtime unverified

## 用途

动作按钮与文字/图标动作

## 结构

Pressable→变体/尺寸Context→Label、可选icon/Spinner

## 参数

default gap2 px4 py2.5 text-base；rounded/pill；default前景底/背景字，中性而非绿色

## 交互状态

active opacity.8；disabled opacity.4；loading禁用及spinner；无自定义按压spring

## 输入、输出与状态

variant、size、shape、icon、loading和Pressable事件；Label子组件

## 反馈与生命周期

loading与disabled参与阻止提交；accessibilityRole=button

## 框架无关迁移

保留业务busy/disabled与视觉态一致；不要移植源码内私有cn/Spinner路径

## 最小用法（说明性片段，未编译）

```
<Button onPress={save}><Button.Label>Save</Button.Label></Button>
```

## 限制

需要纯Web hover状态全等复现，需平台适配

## 源码

- [`packages/ui/src/components/button/button.tsx:48` — `const rootBaseStyles`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/button/button.tsx#L48)
