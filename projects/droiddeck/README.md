# droiddeck

面向触摸、鼠标与手柄焦点的游戏启动器：深色分层底、双强调色渐变、可滑移焦点环、按钮原点扩张与场景升降面板；另有White Red浅色、True Black和动态RGB主题。分析对象为Android启动器UI，不将所承载的Steam/KDE桌面认作自身组件。

分析版本：0.7.1 / main / `f65e7a3d436bee56f32626dc3536708d12e43162`。2112 个文本源文件参与全仓候选扫描；1458 条词法命中不等于 1458 个动画。

## 阅读导航

1. [设计语言](design-language/overview.md) → [Token](design-language/tokens.json) → [布局](design-language/layout.md)
2. 按需选组件或动画，然后读取同目录 spec.json。
3. [架构](architecture/overview.md) · [交互](interactions/overview.md) · [许可证](LICENSE-NOTES.md)
4. [覆盖范围与待办](BACKLOG.md) · [来源索引](references/source-map.json)

## 组件

- [PrimaryButton](components/primary-button/README.md)
- [FocusGlideHost与glideBorder](components/focus-host/README.md)
- [TabStrip与BumperKey](components/tab-strip/README.md)
- [LiftHero](components/lift-hero/README.md)
- [CardDetailHost](components/card-detail-host/README.md)
- [ColorPickerDialog](components/color-picker/README.md)
- [LauncherLayout与AppScale](components/launcher-layout/README.md)

## 动画

- [保留速度的焦点环追随](animations/focus-glide/README.md)
- [标签选中背景的先后缘弹性](animations/chip-glide/README.md)
- [按钮四边扩张到启动场景](animations/launch-flood/README.md)
- [卡片至详情容器过渡](animations/page-flood/README.md)
- [主按钮按压与高亮光晕](animations/button-press/README.md)
- [场景升降面板与内容错峰](animations/lift-sheet/README.md)
- [量化更新的动态RGB主题](animations/inner-gamer/README.md)
- [品牌形变旋转加载器](animations/logo-throbber/README.md)
- [会话Activity上下交接](animations/session-activity/README.md)

## 完成边界

核心资料可检索；原项目未构建、未运行、未录屏。完整候选清单在 references/animation-discovery.json；业务页面、依赖默认值和设备行为仍需后续深化。不要将“源码确认”理解为“运行效果确认”。
