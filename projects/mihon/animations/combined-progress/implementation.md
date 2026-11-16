# 实现原理

AnimatedContent以progress()==0f为target；确定分支 rememberInfiniteTransition 旋转，animateFloatAsState 平滑进度。源码注释明确持续旋转是为了表达未卡住。

## 生命周期与快速触发

切换模式由AnimatedContent保留过渡内容；旋转随确定分支组合生命周期。0同时承担未知进度含义，不能直接当真实0%确定进度。

## 框架无关行为

输入：progress()==0f 分支；progress 数值更新

状态从 `{"progress": 0, "mode": "indeterminate"}` 到 `{"progress": ">0", "mode": "determinate rotating"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

由Material进度组件提供基础语义；未发现本组件额外减少动态效果分支。

## 性能（静态分析，无 FPS 或内存实测）

一个旋转层+进度绘制，无需布局几何逐帧改变；大量列表行同时使用会增加持续绘制。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/CircularProgressIndicator.kt:40` — `fun CombinedCircularProgressIndicator`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/CircularProgressIndicator.kt#L40)
