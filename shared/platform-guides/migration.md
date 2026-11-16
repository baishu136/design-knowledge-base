# 平台迁移与验证

| 来源机制 | 可复用内容 | 必须重建的边界 |
|---|---|---|
| Reanimated | progress映射、Bezier、取消协议 | worklet/JS桥、native thread、测量、可访问树 |
| Compose |状态机、Insets规则、轨道并行 | remember/LaunchedEffect生命周期、dp/sp、Material动态色 |
| CSS/Motion |关键帧、data-state、origin | DOM focus/inert、Radix presence、Electron drag区 |
| Skia | shader方程、uniform含义、时钟条件 |目标GPU/shader语言、DPR、色彩空间、编译缓存 |

移植前核对target framework的spring求解参数、默认动画缩放和单位。不得假设RN point=CSS px=Android dp在所有DPI下物理相同。不要仅将width改成transform便宣称完全相同：width影响相邻布局，scale只缩放画面。

本轮环境有Node和JDK17，但未确认Android SDK/ADB、iOS开发环境及原生依赖。没有安装三项目依赖，也没有执行其prepare/postinstall。原生与Electron整应用运行留待受控宿主；按真实设备验证键盘、大字体、旋转、触屏/鼠标、高刷新与减少动态。

性能测量模板：设备/OS/刷新率/DPR + source commit +内容规模+手势步骤+工具及采样窗口+帧时间/丢帧/GPU/内存数据。静态风险只能标inferred，禁止把理论833ms换算当FPS测试。
