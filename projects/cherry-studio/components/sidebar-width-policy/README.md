# 应用Sidebar宽度策略

`cherry-studio.component.sidebar-width-policy` · source-verified · runtime unverified

## 用途

导航栏hidden/icon/full三态

## 结构

纯策略函数：layout判定、显示宽、持久化宽分开

## 参数

hidden<20；full>=120；icon50；max280；50~120为瞬态

## 交互状态

拖动预览可中间宽；保存时收束到50

## 输入、输出与状态

getSidebarLayout、getSidebarDisplayWidth、normalizeSidebarWidth

## 反馈与生命周期

策略本身无动画；拖动组件负责输入/提交

## 框架无关迁移

把连续预览和离散提交拆开，避免保存尴尬中间宽度

## 最小用法（说明性片段，未编译）

```
normalizeSidebarWidth(90) // 50
getSidebarDisplayWidth(90) // 90
```

## 限制

误把120当所有窗口响应式断点

## 源码

- [`src/renderer/components/Sidebar/constants.ts:9` — `export function getSidebarLayout`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/Sidebar/constants.ts#L9)
