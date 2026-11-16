# 多项目设计知识库

这是基于固定源码快照的设计与动效工程资产。每个项目独立保留规则；跨项目总结不会回写或混合原始Token。当前交付是**核心系统与高价值动画首轮建库**，不是全仓每一个页面/动画的逐项审计完成声明。

## 入口

1. Agent先读 [CATALOG.json](CATALOG.json)，按平台、关键词和资源类型筛选。
2. 按 [AGENTS.md](AGENTS.md) 按需读取项目概述、组件或动画规格。
3. 人类可从下列项目导航进入；横向选择看 [对比](shared/comparisons/projects.md)。

| 项目 | 分析版本 | 组件 | 动画 | 核心特征 |
|---|---|---:|---:|---|
| [Cherry Mobile](projects/cherry-studio-app/README.md) | 0.5.5 / e6d157d2ea60 | 5 | 6 | 移动自有Token、可中断菜单、手势与Shader |
| [Mihon](projects/mihon/README.md) | 0.21.3 / 4823ba69ca65 | 4 | 6 | Material主题、沉浸阅读、嵌套滚动面板 |
| [Cherry Desktop](projects/cherry-studio/README.md) | 2.2.2 / c3263227592a | 4 | 7 | 多栏工作台、Radix生命周期、可取消滚动 |

7组移植示例中，2个框架无关JavaScript内核经过Node执行验证；4组原生组件片段和1组React/CSS片段未编译或运行。没有原项目实机预览、FPS、GPU耗时或内存数据。详见 [执行报告](EXECUTION-REPORT.md) 和 [验证报告](VALIDATION.md)。

## 资料层次与可信度

- 原始层：外部source-repositories的固定源码快照、完整许可证、每条资源的source-reference与SHA256。
- 规格层：设计语言、tokens.json、组件与动画spec.json；事实source-verified，意图解释标“分析”。
- 移植层：examples明确标adapted、覆盖子集和差异；通过数值内核验证不等于视觉验证。

tokens.json保留CSS变量表达式及静态别名替换，不伪称浏览器computed style；Material依赖默认值没有追溯时保留未知。

## 维护

数据作者入口是tools/author.py；tools/build.py只写本知识库，绝不执行上游构建/安装。修改生成文档前先修改作者数据，避免下次重建覆盖手工改动。新增资源的来源与状态在结构化文件中保存。更新版本按 [维护流程](MAINTENANCE.md)。

```powershell
python design-knowledge-base/tools/author.py
node design-knowledge-base/tools/check-examples.mjs
python design-knowledge-base/tools/publish.py
python design-knowledge-base/tools/validate.py
```

上述命令从本工作区根目录执行，或对脚本使用绝对路径。不得把acquire.py当作日常更新按钮：它下载新快照且不执行差异审查。
