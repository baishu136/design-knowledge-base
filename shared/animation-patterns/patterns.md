# 动画模式检索与取舍

| 模式 | 项目证据 | 状态与成本 | 迁移注意 |
|---|---|---|---|
| 可中断presence | [Mobile menu](../../projects/cherry-studio-app/animations/menu-panel/README.md)、[Desktop dialog](../../projects/cherry-studio/animations/dialog/README.md) | 关闭先禁交互，绘制保留至exit；blur/尺寸不一定便宜 | 不只写opacity0；要取消旧回调和恢复焦点 |
| 位移+fade并行 | [Mihon reader bars](../../projects/mihon/animations/reader-bars/README.md)、[Desktop selector](../../projects/cherry-studio/animations/selector-shell/README.md) | 轨道时长可不同；小内容较适合合成 | 结束状态与生命周期一致，不强求统一时长 |
| 精确吸附 | [Mobile slider](../../projects/cherry-studio-app/animations/effort-slider/README.md)、[Mobile text spring](../../projects/cherry-studio-app/animations/rotating-text/README.md) | 前者200ms ease-out，后者物理spring | 都能“停靠”但模型不同；不把参数平均成通用spring |
| 手势sheet | [Mihon sheet](../../projects/mihon/animations/adaptive-sheet/README.md)、[Mobile native sheet](../../projects/cherry-studio-app/animations/native-bottom-sheet/README.md) | 锚点/嵌套滚动与native detent差异 | 原生内部参数未知时保持未知；优先迁移状态和门槛 |
| 持续等待 | [Mihon progress](../../projects/mihon/animations/combined-progress/README.md)、[Mobile Shader](../../projects/cherry-studio-app/animations/foil-loader/README.md)、[Desktop shimmer](../../projects/cherry-studio/animations/text-shimmer/README.md) | 分别旋转、每像素GPU、文字背景paint | 后台/不可见停止；语义busy不依赖动画；不伪称都是GPU廉价 |
| 可取消滚动 | [Desktop RAF](../../projects/cherry-studio/animations/smooth-scroll/README.md)、[Mihon thumb](../../projects/mihon/animations/fast-scroller/README.md) | 一个移动内容，一个显示滚动导航；不可直接替换 | 明确用户中断与目标变化，不排队 |

共享轴是页面层级运动，不是共享元素ID过渡。v0.1三项目范围没有确认可建档的共享封面或歌词播放器动画；新增项目须重新按证据判断。

DroidDeck补充：[PageFlood](../../projects/droiddeck/animations/page-flood/README.md)确实将同一已记录卡片原点/封面Painter过渡到详情，是自定义容器/封面连续性实现，不是Compose SharedTransitionLayout。先前“三项目没有已确认共享封面”结论仅适用于v0.1范围。

| 新模式 | 证据 | 保留规则 |
|---|---|---|
| 保留速度的多边焦点 | [FocusGlide](../../projects/droiddeck/animations/focus-glide/README.md) | leading/trailing参数、重定向速度、窗口坐标与scale0最终焦点 |
| 覆盖即交接 | [LaunchFlood](../../projects/droiddeck/animations/launch-flood/README.md) | onCovered在四边首次触达后通知，不等待spring稳定；输入门闩只限交接 |
| 多轨面板错峰 | [LiftHero](../../projects/droiddeck/animations/lift-sheet/README.md) | 普通open55ms错峰与拖后35ms分开，手势阈值含起始态滞回 |
| 主题色量化 | [Inner Gamer](../../projects/droiddeck/animations/inner-gamer/README.md) | 3度状态量化不等于每帧时钟停止，对比度校正与动画并行 |

建议的框架无关协议（本库分析）：输入intent、currentVisualState、reducedMotion、geometry；输出visualTracks、interactiveState、completion/cancel；业务状态不要依赖动画结束才能正确。参数从目标项目规格选，不从本表抽取统一默认值。
