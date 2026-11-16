# 3度量化RGB时钟移植示例

分类：adapted，来源https://github.com/Droid-Deck/DroidDeck @ `f65e7a3d436bee56f32626dc3536708d12e43162`。许可证：GPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[HueCycle.kt](HueCycle.kt)。规格：[../spec.json](../spec.json)。

## 使用条件

已有Compose animation/runtime宿主；HueCycle(speed=3,reducedMotion=false){ hue -> updatePalette(hue) }。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

不包含ThemeColors对比度生成；caller传reducedMotion；回调只在量化档改变时发出；静止不发新颜色。

## 验证

仅人工静态检查；未编译、未运行。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
