# 实现原理

三处 AnimatedVisibility 共享 visible，将 slide 与 fade 用 + 并行组合。纵向导航按左右选择 LocalLayoutDirection，水平导航放到底部。

## 生命周期与快速触发

AnimatedVisibility 负责过渡内容保留；反向触发由 Compose Transition 接管。实际快速连击视觉和生命周期未运行。

## 框架无关行为

输入：visible Boolean

状态从 `{"visible": false, "offset": "±elementSize", "alpha": 0}` 到 `{"visible": true, "offset": 0, "alpha": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

此组件没有单独 Reduce Motion 分支；不要把隐藏状态仅改为alpha而留下可聚焦控件。

## 性能（静态分析，无 FPS 或内存实测）

slide/fade 不改变漫画图片本身；控制层透明表面仍产生叠绘。避免迁移时把整张超大图片参与动画。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt:46` — `fun ReaderAppBars`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt#L46)
