# 项目设计语言与迁移选择

本表是基于各项目固定版本的**分析总结**，不是多项目共享的官方设计规范。每列必须回到相应项目，不合并Token。

| 维度 | Cherry Mobile | Mihon | Cherry Desktop |
|---|---|---|---|
| 密度 | 触摸尺度与连续中性表面，局部紧凑文案 | 书库密集、阅读页沉浸 | 紧凑工具栏与多栏并排 |
| 导航 | Expo Drawer，宽窗列与文件pane让位 | Voyager与Material共享轴，传统View阅读器并存 | 应用Sidebar、资源栏、右侧Inspector |
| 主题 | mobile-owned Geist palette→语义→Uniwind | 主题预设/Monet/AMOLED→Material ColorScheme | cs providers→Shadcn→产品语义→Tailwind；运行时输入 |
| 动画节奏 | 菜单350/250ms；文本spring31.5/1/248 | 面板350ms；工具栏slide200/fade150 | 面板300ms；Dialog260/200ms；selector150/120ms |
| 反馈 | 默认按钮opacity；Android/Web switch直接状态切换 | 交互elevation、Material反馈 | hover/focus-visible/busy；键盘splitter |
| 动画组织 | shared value + worklet；原生presentation；Skia | Compose动画/协程；平台View绘制 | CSS presence、Motion、RAF三路径 |
| 性能手段 | loader后台停帧、shader缓存；Android native spinner | placement读滚动、collectLatest取消旧任务 | 拖动取消缓动、显式定位RAF可取消 |
| 主要风险 | 菜单宽高+blur、Shader填充率、原图纹理 | 多屏组合、嵌套滚动、图片解码 | width重排、背景流光重绘、帧数时长依赖刷新率 |
| 迁移难度（分析） | 原生sheet/Skia高，状态轨道中 | 颜色角色中，View阅读器与平台手势高 | CSS轨道低，Radix焦点/宿主IPC中高 |

选择：阅读内容使用Mihon的临时控制层；移动操作浮层参考Cherry Mobile的测量/退出门闩；桌面高密度信息工具参考Desktop的宽度协商与焦点策略。需要减少动态时先保留业务状态与导航能力，再缩短/取消轨道。

来源：[Mobile概述](../../projects/cherry-studio-app/design-language/overview.md)、[Mihon概述](../../projects/mihon/design-language/overview.md)、[Desktop概述](../../projects/cherry-studio/design-language/overview.md)及各自动画spec。以上性能只属静态风险，无测量排序。

## DroidDeck 对照

| 维度 | DroidDeck | 与现有项目的区别/选择 |
|---|---|---|
| 风格/密度 | 游戏内容、鲜明动作渐变与手柄焦点；含浅色预设 | 相比Cherry中性动作更突出；不是全应用都黑底 |
| 导航 | side/bottom由调用方选择，另有双屏会话 | 比Mihon更多控制器焦点/跨窗口策略；不可仅凭600dp归类 |
| 主题架构 | Palette→darkColorScheme映射；动态HSV与对比度校正 | 相比Mihon的Material/Monet，更多自有动态算法；构造名不表示只能深色 |
| 动画节奏 | 不同物理弹簧、多边延迟、内容错峰 | 不套用Mobile350ms菜单或Desktop300ms面板作为通用时长 |
| 缓动 | Motion.tw(.2,.8,.2,1)；FocusGlide手写数值积分 | Compose spring参数为dampingRatio，而RN物理damping不是同单位 |
| 交互反馈 | 按压.955/hot1.02、窗口级滑移ring、A/B/LB/RB | 手柄密集界面优先参考DroidDeck；触摸阅读控制优先Mihon |
| 抽象方式 | FocusGlideHost/Window、Motion、SharedMotion和Hero状态层 | 不同于Radix Presence的DOM生命周期；跨窗口坐标必须匹配 |
| 性能策略 | 4ms积分子步、Path复用、RGB3度量化 | 数值稳定措施不等于GPU/FPS指标；CardDetailHost显式Offscreen有成本 |
| 迁移难度 | 参数/数学模型中，窗口焦点与会话交接高 | 最先抽单边弹簧与覆盖回调，后接目标框架输入和焦点生命周期 |
| 许可 | GPL-3.0 | 不与Cherry的AGPL或Mihon的Apache标签混用 |

来源：[DroidDeck概述](../../projects/droiddeck/design-language/overview.md)、[焦点环](../../projects/droiddeck/animations/focus-glide/spec.json)、[布局](../../projects/droiddeck/design-language/layout.md)、[主题](../../projects/droiddeck/design-language/colors.md)。
