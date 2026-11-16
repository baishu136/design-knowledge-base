# typography

共享定义heading/body字体Inter；weight400/500/700；body12/14/16/18px对应rem=.75/.875/1/1.125，heading20/24/32/40/48/60。实际Button默认text-[13px]属于组件密度，不应把它覆盖成body-md。CJK字体fallback与实际字体安装/加载未实机验证。代码组件单独拥有monospace栈；本轮未逐个追溯。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/styles/tokens/typography.css:8` — `--cs-font-family-heading`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/styles/tokens/typography.css#L8)
- [`packages/ui/src/components/primitives/button.tsx:8` — `const buttonVariants`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/button.tsx#L8)
