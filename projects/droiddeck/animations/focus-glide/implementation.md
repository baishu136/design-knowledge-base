# 实现原理

go写目标/弹簧参数和startAt；单帧协程将dt=min(frameDelta,.1)/max(scale,.01)，用h<=.004秒半隐式Euler：u+=(-k*(x-target)-2*zeta*sqrt(k)*u)*h，x+=u*h。保留vel数组，目标改变不排队。初入先长出3dp再收边。非连续按键且距离>360dp走droplet：90ms收成6dp半径点、220..380ms飞行，在progress>=.78改为弹簧展开；不是所有移动都走此分支。

## 生命周期与快速触发

collectLatest替换观察任务；jobs数组分别取消边/圆角/solid/求解器任务。hidden或Motion.scale=0取消并snap；源或窗口失效不读取detach布局。bounds追踪450ms后至少稳定120ms或达到2s停止轮询。

## 框架无关行为

输入：glide.current/moves/hidden变化，窗口中的焦点或hot对象切换

状态从 `{"edges": "current rect", "velocity": "retained per edge"}` 到 `{"edges": "focused control bounds", "velocity": 0}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

可见焦点与手柄导航是核心；scale0仍显示正确最终焦点，不是完全去除ring。跨View则回退静态border。没有TalkBack/大字体实测。

## 性能（静态分析，无 FPS 或内存实测）

drawWithContent重绘局部ring，避免改变目标组件布局；四轨4ms子步在极低scale下步数会增多，尤其dt cap在除scale之前。多层Job、窗口坐标跟踪和离屏内容仍有开销；没有FPS/CPU测量。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:189` — `private fun Modifier.focusGlideOverlay`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L189)
- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:120` — `internal fun Modifier.glideBorder`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L120)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
