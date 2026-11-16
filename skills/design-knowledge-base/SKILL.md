---
name: design-knowledge-base
description: "按需检索本地设计知识库，学习和迁移 Cherry Studio Mobile、Mihon、Cherry Studio Desktop、DroidDeck 的设计语言、组件、手势、焦点和动画实现。用于从已有源码分析中选方案、对比项目风格、提取主题 Token、按规格复用动效；一般 UI 任务仅在需要参考这套知识库时使用。"
---

# 设计知识库

从已有的固定源码分析中定位可用知识，再适配用户当前项目。知识库与技能分开存放；本技能不内置整份知识库，也不在检索时自动下载、安装依赖或执行原项目。

## 找到资料

使用技能目录内的 `scripts/kb.py`。命令均可从任意目录执行；下面的脚本路径相对**本技能目录**，实际执行时替换为已读到的绝对路径。

```text
python scripts/kb.py locate
python scripts/kb.py search focus --project droiddeck --type animation --limit 4
python scripts/kb.py resolve droiddeck.animation.focus-glide
python scripts/kb.py tokens --project cherry-studio-app --name primary --theme dark --limit 6
```

定位优先级：`--kb-root` → 环境变量 `DESIGN_KNOWLEDGE_BASE` → 本技能的 `config.local.json` 中 `kb_root` → 技能所在知识库 → 当前目录及父目录中的知识库。显式路径失效时报告错误，不悄悄换库。

本机安装可使用 `config.local.json` 绑定位置；它属于本机配置，不写进公开仓库。移动知识库后更新该配置，或传 `--kb-root`。无匹配时先减少关键词或取消平台过滤，必要时看项目 BACKLOG 与候选清单；不要凭空补出资源。

## 按需阅读与实现

1. 从 `locate` 返回的 `AGENTS.md` 了解资料约定。用 `search` 筛选平台、项目、类型；不要加载整个索引、Token 表和候选源码清单。查询用少量关键词或稳定资源 ID，例如 `focus`、`sheet`、`menu`、`reader`、`shader`。
2. 对选定 ID 用 `resolve` 获得绝对路径。先读项目 `manifest.json`、`design-language/overview.md`，再读目标资源的 README 与 `spec.json`。遇到配色需求，用 `tokens` 只取相关角色。
3. 从 `example_paths` 定位示例，并读同目录 `example.json`，确认它实际覆盖的子集、依赖、差异和验证范围。没有示例时可按行为规格实现，不声称原库提供了完整移植代码。
4. 对关键参数和边界回溯 `sources` 的固定 Commit 链接或本地快照。`source-map.json` 用于查哈希；`animation-discovery.json` 只是词法候选，不等于确认过的动画。
5. 根据当前框架重建输入、状态、轨道、中断、退出保留、焦点与手势竞争；保留用户项目架构。主题值与动效参数始终归属于原项目，不将不同项目的数值混成某个项目的官方规范。
6. 引用或改编前读项目 `LICENSE-NOTES.md`。Cherry 两项目标 AGPL-3.0，Mihon 标 Apache-2.0，DroidDeck 标 GPL-3.0；最终以目标资源和上游文件为准，不能互相替代。保留必要来源、署名和修改说明。

## 选择线索

- 触摸菜单的测量、反向触发与退出保留：`cherry-studio-app.animation.menu-panel`。
- 沉浸阅读控制层：`mihon.animation.reader-bars`；长书库滚动反馈：`mihon.animation.fast-scroller`。
- 桌面可调整资源栏：`cherry-studio.component.resource-pane` + `cherry-studio.animation.resource-pane`；模态焦点与退出：`cherry-studio.animation.dialog`。
- 手柄焦点、多边弹簧和场景交接：`droiddeck.animation.focus-glide`、`droiddeck.animation.launch-flood`、`droiddeck.animation.lift-sheet`。
- 跨项目选择：读取 `shared/comparisons/projects.md`，再回到各自规格，避免把比较结论当官方 Token。

这些 ID 是导航线索；实际可用项目和覆盖范围以当前索引为准。

## 证据与交付

- `null` 是未确认参数，不能补成 0 或凭印象填框架默认值。`inferred` 是分析推断，不是作者声明。
- `source-verified` 只证明读过源码。`runtime-verified` 必须连同 `runtime_scope` 阅读；Node 数值内核通过不等于 Compose/RN/DOM 视觉或设备验证。
- Token 的 `value` 可能是 CSS 引用或公式；`resolved_expression` / `effective_theme_expressions` 也不是浏览器实测 computed style。DroidDeck 等项目的命名预设不能统一强套 light/dark。
- 实现后按实际范围检查快速重触发、取消、卸载、焦点恢复、Reduce Motion、低性能设备；缺少运行条件时明确未验证，不填写虚构 FPS。
- 交付说明所用资源 ID、固定版本来源、迁移差异、许可证与实际验证范围。用户只要查阅时直接答复资料；用户要开发时继续完成其授权的实现。

用户要求新增或更新知识库时，按根目录 `MAINTENANCE.md` 更新作者数据、来源、规格、索引和变更记录，保留旧资源 ID。检索或使用本技能本身不额外授权修改原始源码、发布远端变更或安装软件。
