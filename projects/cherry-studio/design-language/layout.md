# layout

应用Sidebar宽<20隐藏、<120图标、否则full；图标标准50，max280。50~120的拖动预览可连续显示，但持久化归一为50。聊天资源栏默认240、min200/max360；窄宽自动收纳阈值540属于资源栏策略，不是全站断点；右侧inspector最小255且上限未固定。PageSidebar首次打开后保留children，关闭inert+aria-hidden，减少状态重置。

```mermaid
flowchart LR
 AppNav[应用导航] --> Resources[会话/资源列表]
 Resources --> Center[中心对话/文档]
 Center --> Inspector[右侧Inspector]
```

响应式是中心可用空间与面板宽度协商，不能照搬手机bottom tabs。具体resize hook、键盘splitter行为见源码，触屏与多DPI未运行。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`src/renderer/components/Sidebar/constants.ts:9` — `export function getSidebarLayout`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/Sidebar/constants.ts#L9)
- [`src/renderer/components/chat/shell/paneLayout.ts:5` — `export const CHAT_SHELL_TRANSITION`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/paneLayout.ts#L5)
- [`src/renderer/components/chat/shell/PageSidebar.tsx:28` — `export function PageSidebar`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/PageSidebar.tsx#L28)
