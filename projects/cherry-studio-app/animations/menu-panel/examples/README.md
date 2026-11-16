# 菜单内容透明度和变换移植示例

分类：adapted，来源https://github.com/CherryHQ/cherry-studio-app @ `e6d157d2ea604ef65d38ca14e88ba92de706ad8a`。许可证：AGPL-3.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[MenuSurface.tsx](MenuSurface.tsx)。规格：[../spec.json](../spec.json)。

## 使用条件

已有React Native/Reanimated4开发客户端，正确配置worklets；MenuSurface open={open}包内容。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

不含测量/宽高/blur/portal/focus；只复现内容轨道。

## 验证

仅人工静态检查；未编译、未运行。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
