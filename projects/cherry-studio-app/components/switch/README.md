# SwitchControl（Android/Web）

`cherry-studio-app.component.switch` · source-verified · runtime unverified

## 用途

布尔偏好控制

## 结构

Pressable track→描边thumb外壳→白色内芯

## 参数

default44×24、thumb20；lg48×28、thumb24；sm36×20、thumb16；hitSlop8

## 交互状态

value切items-start/end与control-active/border-selected；disabled.opacity40；无插值动画

## 输入、输出与状态

value受控、onValueChange(!value)、disabled、size及accessibilityLabel

## 反馈与生命周期

accessibilityRole=switch；checked/disabled同步

## 框架无关迁移

UI控件几何与父行的触摸目标分离；iOS另走平台文件，不能混作一份源码

## 最小用法（说明性片段，未编译）

```
<SwitchControl value={enabled} onValueChange={setEnabled} accessibilityLabel="Enabled" />
```

## 限制

把小轨道当唯一完整触摸目标且不保留hitSlop

## 源码

- [`packages/ui/src/components/switch/switch-control/switch-control.tsx:15` — `export function SwitchControl`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/switch/switch-control/switch-control.tsx#L15)
