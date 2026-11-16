# Shader时钟与周期数值模型移植示例

分类：adapted，来源https://github.com/CherryHQ/cherry-studio-app @ `e6d157d2ea604ef65d38ca14e88ba92de706ad8a`。许可证：AGPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[clock.mjs](clock.mjs)。规格：[../spec.json](../spec.json)。

## 使用条件

Node标准ES module，无第三方依赖；由tools/check-examples.mjs执行，或import advanceClock/phaseAt。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

没有渲染Shader；额外限制负delta为0，不代表原文件有该条件。

## 验证

已用Node执行数值/生命周期断言；没有渲染原框架。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
