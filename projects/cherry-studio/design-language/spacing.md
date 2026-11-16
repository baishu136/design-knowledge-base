# spacing

spacing.css从4px(.25rem)到112px(7rem)提供16档；与Tailwind类共同使用，不把这些档位解释为严格全仓8点网格。cs-radius-md=.5rem，cs-radius-lg=.625rem，Shadcn --radius引用后者；适配后的rounded-*须读取theme.css，不能仅按cs-radius名称猜最终圆角。导航栏按钮30px盒/18px图标，默认按钮min-height30px/13px字，体现桌面密度。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/styles/tokens/spacing.css:7` — `--cs-size-5xs`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/styles/tokens/spacing.css#L7)
- [`packages/ui/src/styles/tokens/radius.css:13` — `--cs-radius-lg`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/styles/tokens/radius.css#L13)
- [`packages/ui/src/components/primitives/button.tsx:8` — `const buttonVariants`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/components/primitives/button.tsx#L8)
