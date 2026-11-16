# PageSidebar

`cherry-studio.component.resource-pane` · source-verified · runtime unverified

## 用途

聊天资源/会话列表栏

## 结构

AnimatePresence→motion.div→裁切content和外侧resize handle

## 参数

默认240/min200/max360；可用宽阈值540；motion300ms

## 交互状态

未打开、打开、收起保留、resizing；收起inert

## 输入、输出与状态

open,width,children,onPaneCollapse,onResizingChange

## 反馈与生命周期

拖动duration0；键盘splitter调用setPaneWidth；首次打开后保留树

## 框架无关迁移

保留可用宽协商、持久化和隐藏焦点策略；DOM惯性不能映射为alpha0

## 最小用法（说明性片段，未编译）

```
<PageSidebar open={open} onPaneCollapse={collapse}>{list}</PageSidebar>
```

## 限制

把此组件当整应用Sidebar；两者宽度阈值不同

## 源码

- [`src/renderer/components/chat/shell/PageSidebar.tsx:28` — `export function PageSidebar`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/PageSidebar.tsx#L28)
- [`src/renderer/components/chat/shell/paneLayout.ts:5` — `export const CHAT_SHELL_TRANSITION`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/paneLayout.ts#L5)
