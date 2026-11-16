# Radix Dialog

`cherry-studio.component.dialog` · source-verified · runtime unverified

## 用途

模态窗口与嵌套交互层

## 结构

KeyboardLayerRoot→Radix Root→Portal→Overlay与Content直接子节点→PortalContainerProvider

## 参数

overlay黑50%/z80；content p6/gap4/bg-card/rounded3xl；size sm/default/lg/xl

## 交互状态

open/closed/forceMount；closeOnOverlayClick可禁用

## 输入、输出与状态

open/defaultOpen/onOpenChange；DialogContent motion,size,closeLabel,showCloseButton

## 反馈与生命周期

Presence保留退出；焦点恢复后释放KeyboardLayer；嵌套tooltip portal跟层级

## 框架无关迁移

先实现modal/focus/escape/portal，再加动画；no-drag是Electron专属适配

## 最小用法（说明性片段，未编译）

```
<Dialog><DialogTrigger>Open</DialogTrigger><DialogContent><DialogTitle>Options</DialogTitle></DialogContent></Dialog>
```

## 限制

仅拷贝class忽略Radix与KeyboardLayer

## 源码

- [`packages/ui/src/components/primitives/dialog.tsx:87` — `function DialogContent(`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/dialog.tsx#L87)
