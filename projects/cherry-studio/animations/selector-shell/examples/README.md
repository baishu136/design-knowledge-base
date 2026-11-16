# 浮层fade与scale双轨移植示例

分类：adapted，来源https://github.com/CherryHQ/cherry-studio @ `c3263227592ad14313da2b4153bf88502c466454`。许可证：AGPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[SelectorPanel.tsx](SelectorPanel.tsx)。规格：[../spec.json](../spec.json)。

## 使用条件

已有React19/TypeScript/CSS宿主；import SelectorPanel；不要在open=false立刻卸载。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

仅bottom方向；origin固定top center；父级保留退出120ms且负责焦点；非完整Popover。

## 验证

仅人工静态检查；未编译、未运行。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
