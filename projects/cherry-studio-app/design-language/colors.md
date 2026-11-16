# colors

调色板→Shadcn角色→Cherry产品语义→生成native.css→Uniwind class/useThemeColor。tokens.json对生成文件light/dark声明保留原始值和解析后表达式。#f5f5f5浅背景、card为background-100；primary随green-900主题变档。灰阶不单调，不能按数字大小推断亮度。HeroUI的muted/accent/accent-foreground是保留桥接名，不能直接当移动公共工具类。

发现文档与实现不同步：shadcn.css注释说“mobile app has no sidebar”，但本Commit的DrawerLayout实际调用useThemeColor(['background','sidebar','sidebar-border','scrim'])，并渲染appShell/sidebar。此处以消费者实现为准；不能沿用该注释声称Sidebar未使用。这是源码冲突记录，不是本库对原项目的修复。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`packages/design-tokens/src/styles/native.css:105` — `@variant light`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/design-tokens/src/styles/native.css#L105)
- [`packages/design-tokens/src/styles/shadcn.css:64` — `--sidebar`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/design-tokens/src/styles/shadcn.css#L64)
- [`src/app/(drawer)/_layout.tsx:40` — `export default`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/app/(drawer)/_layout.tsx#L40)
- [`DESIGN.md:194` — `## Motion`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/DESIGN.md#L194)
