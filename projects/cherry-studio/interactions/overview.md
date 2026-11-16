# overview

Button loading同时disabled与aria-busy，busy视觉opacity.4；Dialog通过KeyboardLayer管理关闭后的焦点与嵌套portal，保留Content为Portal直接子节点以让Radix Presence接收ref。PageSidebar折叠后inert阻止隐藏内容被键盘访问。显式平滑滚动必须由调用方在用户中断时cancel；流式追随边缘是instant，不能对每个token排队smooth-scroll。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/components/primitives/button.tsx:8` — `const buttonVariants`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/button.tsx#L8)
- [`packages/ui/src/components/primitives/dialog.tsx:87` — `function DialogContent(`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/dialog.tsx#L87)
- [`src/renderer/components/chat/shell/PageSidebar.tsx:28` — `export function PageSidebar`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/shell/PageSidebar.tsx#L28)
- [`src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts:58` — `export function useSmoothScrollAnimation`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/chat/messages/list/useSmoothScrollAnimation.ts#L58)
