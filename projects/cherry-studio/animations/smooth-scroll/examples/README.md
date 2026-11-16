# 取消/替换/动态目标的滚动控制器移植示例

分类：adapted，来源https://github.com/CherryHQ/cherry-studio @ `c3263227592ad14313da2b4153bf88502c466454`。许可证：AGPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[controller.mjs](controller.mjs)。规格：[../spec.json](../spec.json)。

## 使用条件

浏览器import并注入requestAnimationFrame/cancelAnimationFrame；挂wheel/touchstart时cancel，卸载dispose；Node测试注入虚拟scheduler。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

从React hook改为getNode和dispose；没有用户事件监听与Reduce Motion集成。

## 验证

已用Node执行数值/生命周期断言；没有渲染原框架。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
