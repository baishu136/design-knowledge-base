# 实现原理

常规open先pull到24、sink；120ms后lift/ride，piece_i延迟380+i*55后220ms进入。拖动直接snap相关轨，松手按速度±600dp/s优先，再用起始态不同的.3/.7阈值吸附；拖动后的piece错峰为35ms，不能与普通open的55ms混用。launching进入fold/foldTop另一分支。

## 生命周期与快速触发

dragJob可取消；dragSettled阻止open效果重播并保留拖后焦点恢复。ON_STOP清open/shown/launching并注销observer。onDragCancel以0速度settle；后台返回和外部launch交接需实机验证。

## 框架无关行为

输入：open/launching或纵向drag/nested scroll

状态从 `{"lift": 0, "ride": 0, "sink": 0, "pieces": 0}` 到 `{"lift": 1, "ride": 1, "sink": 1, "pieces": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：用户拖动、rows nested scroll和速度tracker协作；手势方向与drop面板仲裁，解除时按状态和阈值吸附。

## 无障碍

触摸/Keyboard模式分别处理焦点，open后延迟请求tab/指定控件，close恢复play；BackHandler仅open且非launching启用。手柄导航与读屏未同等验证。

## 性能（静态分析，无 FPS 或内存实测）

多Animatable+12个piece、多层Canvas path和背景层；手势follow每次scope.launch snap多轨，密集输入需关注任务频率和大内容绘制。无时帧测量。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt:176` — `internal fun LiftHero`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/LiftSheet.kt#L176)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
