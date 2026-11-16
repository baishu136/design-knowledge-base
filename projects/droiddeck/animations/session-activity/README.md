# 会话Activity上下交接

ID：`droiddeck.animation.session-activity` · source-verified · 原项目未运行

进入从父高100%向上到0并alpha.6→1；退出向父高100%下移。

适用：启动器和远端会话Activity的切换

不适用：复制成普通Compose局部卡片的变换规范

- [结构化规格](spec.json)
- [原理、状态机与迁移](implementation.md)
- [固定版本源码](source-reference.md)

参数为 null 的字段不可补成框架默认数值。没有实录预览。
