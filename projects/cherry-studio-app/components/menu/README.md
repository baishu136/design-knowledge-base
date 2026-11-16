# MenuContent / MenuPanel

`cherry-studio-app.component.menu` · source-verified · runtime unverified

## 用途

锚定操作、分组菜单及勾选项

## 结构

MenuOverlay→Animated外壳→MenuSurface→Animated内容→ScrollView→MenuRow

## 参数

preferredWidth208、maxHeight480；初始32×32；padding2 gap.5；行图标size5

## 交互状态

未测量、打开、关闭保留、卸载；关闭禁止pointerEvents/无障碍后代

## 输入、输出与状态

anchor,isOpen,items,onClose,onClosed；MenuItem的checked/disabled/destructive及onPress

## 反馈与生命周期

Android键盘变动关闭旧锚定菜单；layout高差>1才更新

## 框架无关迁移

分离测量、定位、生命周期与渲染轨道；首次height=0时不启动

## 最小用法（说明性片段，未编译）

```
<MenuContent anchor={anchor} isOpen={open} items={items} onClose={close} onClosed={afterClose} />
```

## 限制

不受控的全屏内容或长列表里每项都加blur

## 源码

- [`packages/ui/src/components/menu/menu-content.tsx:19` — `export function MenuContent`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-content.tsx#L19)
- [`packages/ui/src/components/menu/menu-panel.tsx:16` — `export function MenuPanel`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/menu-panel.tsx#L16)
- [`packages/ui/src/components/menu/use-menu-motion.ts:13` — `export function useMenuMotion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/menu/use-menu-motion.ts#L13)
