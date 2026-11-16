# 四边覆盖状态控制器移植示例

分类：adapted，来源https://github.com/Droid-Deck/DroidDeck @ `f65e7a3d436bee56f32626dc3536708d12e43162`。许可证：GPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[LaunchEdges.kt](LaunchEdges.kt)。规格：[../spec.json](../spec.json)。

## 使用条件

已有Android Compose BOM2024.02.00宿主；调用rememberLaunchEdges返回四边进度，自行绘制和处理业务启动。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

无Canvas/Logo/遮罩/触摸门闩；boolean reached改为Compose状态；geometry变化可重启动画；仅布尔reducedMotion，不含Motion.ms的系统scale读取。

## 验证

仅人工静态检查；未编译、未运行。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
