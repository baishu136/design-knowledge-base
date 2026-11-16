# 保留速度的单边弹簧数值内核移植示例

分类：adapted，来源https://github.com/Droid-Deck/DroidDeck @ `f65e7a3d436bee56f32626dc3536708d12e43162`。许可证：GPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[spring.mjs](spring.mjs)。规格：[../spec.json](../spec.json)。

## 使用条件

Node标准ES module；node tools/check-droiddeck.mjs；不编译Compose也不测帧率。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

单边模型，不含四边延迟、droplet、窗口焦点、Job生命周期；禁用motion由helper显式snap，另夹住负delta。

## 验证

已用Node执行数值/生命周期断言；没有渲染原框架。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
