# Shadcn Button

`cherry-studio.component.button` · source-verified · runtime unverified

## 用途

桌面工具栏和表单动作

## 结构

button或Radix Slot→可选Loader+children

## 参数

default min-h7.5/13px；navbar30px/18px图标；default黑白中性；shadow-xs

## 交互状态

hover、focus-visible、disabled、busy、aria-invalid；disabled/busy opacity.4

## 输入、输出与状态

variant,size,asChild,loading,loadingIcon,disabled及HTML button事件

## 反馈与生命周期

loading同时disabled/aria-busy；asChild不插入loading子节点

## 框架无关迁移

保留焦点可见态与业务busy禁用；Slot只接单节点，不直接照搬到RN

## 最小用法（说明性片段，未编译）

```
<Button loading={saving} onClick={save}>Save</Button>
```

## 限制

以默认小尺寸作为移动触摸标准

## 源码

- [`packages/ui/src/components/primitives/button.tsx:8` — `const buttonVariants`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/button.tsx#L8)
