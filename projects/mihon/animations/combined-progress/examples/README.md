# 确定进度持续旋转移植示例

分类：adapted，来源https://github.com/mihonapp/mihon @ `4823ba69ca65fa707fb89406f3a4c43c9e0053dd`。许可证：Apache-2.0；作者署名和修改说明在文件头；完整上游许可在项目references/UPSTREAM-LICENSE.txt。

入口：[RotatingProgress.kt](RotatingProgress.kt)。规格：[../spec.json](../spec.json)。

## 使用条件

Compose animation/runtime/ui与Material3；MaterialTheme内调用RotatingProgress(.5f,false)。本库不包含完整宿主工程、lockfile或平台SDK。原生片段没有编译验证；不可称作已验证可运行App。

## 与原实现的差异

不含未知态交叉淡入；加入显式reducedMotion。

## 验证

仅人工静态检查；未编译、未运行。

检查可访问语义、背景/前景Token、快速反向触发和父级卸载。示例不替代完整产品组件。
