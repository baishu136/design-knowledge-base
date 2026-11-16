# 自适应Sidebar列策略

`cherry-studio-app.component.sidebar-column` · source-verified · runtime unverified

## 用途

手机抽屉、宽窗常驻列与折叠屏布局

## 结构

DrawerLayout→SidebarColumnProvider→resolveSidebarColumn→Drawer front/permanent

## 参数

overlay最大400点且保留64点场景；手势水平激活20；header40/dock44

## 交互状态

overlay、permanent、collapsed、yielded；fold可覆盖用户collapsed保证内容不跨铰链

## 输入、输出与状态

isWide,isCollapsed,isPaneInColumn,fold,insets,windowWidth；输出kind/width/foldGap；toggle动作open/hide/show

## 反馈与生命周期

文件pane占列优先让位；折叠区优先于普通collapsed；只有overlay+chatFocused启用swipe

## 框架无关迁移

保留布局决策优先级；Drawer动画由平台导航库负责，不补原生spring

## 最小用法（说明性片段，未编译）

```
resolveSidebarColumn({isWide:false,isCollapsed:false,isPaneInColumn:false,content:"sidebar",windowWidth:390,insetLeft:0,insetRight:0,fold:null}) // overlay
```

## 限制

将fold/insets硬编码成普通Web断点

## 源码

- [`src/frontend/appShell/sidebar/resolveSidebarColumn.ts:48` — `export function resolveSidebarColumn`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/appShell/sidebar/resolveSidebarColumn.ts#L48)
- [`src/frontend/utils/constants.ts:58` — `export const appSidebar`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/utils/constants.ts#L58)
- [`src/app/(drawer)/_layout.tsx:40` — `export default`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/app/(drawer)/_layout.tsx#L40)
