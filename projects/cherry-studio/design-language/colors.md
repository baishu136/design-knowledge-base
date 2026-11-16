# colors

primitive→内部cs-* providers→theme-input→Shadcn公开角色→product→theme.css适配。tokens.json按root/.dark解析颜色链，保留变量表达式，不能把运行时useUserTheme输入当固定常量。浅色background=cs-white，foreground=oklch(.213 0 0)，sidebar=oklch(.9672 0 0)；dark来源分别覆盖而非反相。ThemeProvider从已加载偏好推导首帧，之后监听native主题，避免先提交OS错误主题的一帧。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/ui/src/styles/tokens/colors/providers.css:23` — `--cs-background`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/styles/tokens/colors/providers.css#L23)
- [`packages/ui/src/styles/shadcn.css:19` — `--primary`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/packages/ui/src/styles/shadcn.css#L19)
- [`src/renderer/components/ThemeProvider.tsx:28` — `export const ThemeProvider`](https://github.com/CherryHQ/cherry-studio/blob/c3263227592ad14313da2b4153bf88502c466454/src/renderer/components/ThemeProvider.tsx#L28)
