# cherry-studio-app

移动端中性优先、绿色动作强调、红色仅作品牌；移动自有Vercel/Geist Token，并不继续镜像桌面数值。CherryUI统一跨平台组件外壳，局部原生适配和可中断动效。

分析版本：0.5.5 / main / `e6d157d2ea604ef65d38ca14e88ba92de706ad8a`。3703 个文本源文件参与全仓候选扫描；534 条词法命中不等于 534 个动画。

## 阅读导航

1. [设计语言](design-language/overview.md) → [Token](design-language/tokens.json) → [布局](design-language/layout.md)
2. 按需选组件或动画，然后读取同目录 spec.json。
3. [架构](architecture/overview.md) · [交互](interactions/overview.md) · [许可证](LICENSE-NOTES.md)
4. [覆盖范围与待办](BACKLOG.md) · [来源索引](references/source-map.json)

## 组件

- [CherryUI Button](components/button/README.md)
- [SwitchControl（Android/Web）](components/switch/README.md)
- [MenuContent / MenuPanel](components/menu/README.md)
- [CherryUI BottomSheet](components/bottom-sheet/README.md)
- [自适应Sidebar列策略](components/sidebar-column/README.md)

## 动画

- [可中断展开菜单](animations/menu-panel/README.md)
- [短语弹簧切换](animations/rotating-text/README.md)
- [离散滑杆磁吸](animations/effort-slider/README.md)
- [图片捏合/双击缩放](animations/image-zoom/README.md)
- [原生底部面板高度跟随](animations/native-bottom-sheet/README.md)
- [图片生成珠光 Shader](animations/foil-loader/README.md)

## 完成边界

核心资料可检索；原项目未构建、未运行、未录屏。完整候选清单在 references/animation-discovery.json；业务页面、依赖默认值和设备行为仍需后续深化。不要将“源码确认”理解为“运行效果确认”。
