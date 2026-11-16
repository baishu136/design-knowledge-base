# overview

DESIGN.md明确content-first、neutral-first和语义化共享层。surface色承担深度，静态容器不普遍依赖强阴影；导航区与对话、文档、代码内容分层。Button默认黑白中性动作，primary是可配置主题强调，不是每个按钮的底色。

分析：高信息密度通过可调多栏与收纳实现，不只是缩小字号。迁移时必须保留中心内容的可读宽度、侧栏折叠/调整与键盘操作；可替换业务导航项，不应整体复制IPC/数据服务。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`DESIGN.md:22` — `## 1. Design direction`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/DESIGN.md#L22)
- [`packages/ui/src/components/primitives/button.tsx:8` — `const buttonVariants`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/button.tsx#L8)
- [`src/renderer/components/Sidebar/constants.ts:9` — `export function getSidebarLayout`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/Sidebar/constants.ts#L9)
- [`src/renderer/components/chat/shell/paneLayout.ts:5` — `export const CHAT_SHELL_TRANSITION`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/paneLayout.ts#L5)
