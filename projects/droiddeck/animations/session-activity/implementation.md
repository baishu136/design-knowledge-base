# 实现原理

res/anim set组合translate与alpha；sink只有translate，不补造退出fade。SessionActivity在没有可用Flood return目标等分支下使用sink；FrontEndActivity引用rise。它是Android传统View/Activity动画，不是Compose Motion.tw控制的同一个时钟。

## 生命周期与快速触发

生命周期与窗口过渡由Android处理；再入、系统手势返回和动画关闭需设备验证。

## 框架无关行为

输入：Activity overridePendingTransition调用

状态从 `{"enter_translateY": "100%p", "enter_alpha": 0.6, "exit_translateY": 0}` 到 `{"enter_translateY": 0, "enter_alpha": 1, "exit_translateY": "100%p"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

XML没有自建Reduce Motion分支；不把Motion.scale对Compose的处理自动套进这些系统动画。

## 性能（静态分析，无 FPS 或内存实测）

Activity层窗口变换较适合系统合成，但承载Surface/会话渲染的兼容性与内存不可从XML判断。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/res/anim/session_rise.xml:2` — `<set`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/res/anim/session_rise.xml#L2)
- [`app/src/main/res/anim/session_sink.xml:2` — `<set`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/res/anim/session_sink.xml#L2)
- [`app/src/main/java/com/droiddeck/launcher/SessionActivity.kt:6289` — `overridePendingTransition(R.anim.session_hold, R.anim.session_sink)`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/SessionActivity.kt#L6289)
- [`app/src/main/java/com/droiddeck/launcher/FrontEndActivity.kt:769` — `R.anim.session_rise`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/FrontEndActivity.kt#L769)
