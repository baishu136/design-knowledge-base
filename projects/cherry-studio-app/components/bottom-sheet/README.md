# CherryUI BottomSheet

`cherry-studio-app.component.bottom-sheet` · source-verified · runtime unverified

## 用途

统一移动面板壳

## 结构

BottomSheetProvider→ModalBottomSheet→header/body/footer

## 参数

maxWidth720；topRadius32；topInset12；sizes compact/medium/large/full

## 交互状态

closed/open/resizable/keyboard；dismissible决定关闭能力和handle

## 输入、输出与状态

open,onClose；height/size/sizes互斥联合；title,footer,avoidKeyboard,onSizeChange

## 反馈与生命周期

保留native position；close回调去重；多档键盘不更改snap points

## 框架无关迁移

保留互斥尺寸API和safe-area模型；换框架需换native provider

## 最小用法（说明性片段，未编译）

```
<BottomSheet open={open} onClose={close} size="medium" title="Options">{content}</BottomSheet>
```

## 限制

直接复制到DOM却假定native动画参数仍有效

## 源码

- [`packages/ui/src/components/bottom-sheet/bottom-sheet.tsx:113` — `export function BottomSheet(props`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/bottom-sheet/bottom-sheet.tsx#L113)
