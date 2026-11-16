# 实现原理

DefaultNavigatorScreenTransition 把非Pop视为forward；ScreenTransition用AnimatedContent和navigator.saveableState保存过渡屏幕状态。数字时长与距离委托composeMaterialMotion，不能套用本库其他fade参数。

## 生命周期与快速触发

AnimatedContent与Voyager saveableState协作；BackHandler enabled=canPop。依赖在快速连续push/pop时的策略需运行验证。

## 框架无关行为

输入：navigator.lastItem/lastEvent

状态从 `{"screen": "previous"}` 到 `{"screen": "lastItem"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

系统/依赖运动缩放与屏幕焦点恢复尚未运行核实。

## 性能（静态分析，无 FPS 或内存实测）

过渡期可能共存两个复杂屏幕；图片与列表资源需关注释放时机。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/eu/kanade/presentation/util/Navigator.kt:39` — `DefaultNavigatorScreenTransition`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/util/Navigator.kt#L39)
