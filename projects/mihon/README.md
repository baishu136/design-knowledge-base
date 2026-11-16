# mihon

以书库与沉浸阅读为中心：Material 语义配色、多套主题和 AMOLED 覆盖；内容密集的列表/网格与可隐藏阅读工具栏共存。阅读器仍包含 Android View 路径，不能将项目整体视为纯 Compose。

分析版本：0.21.3 / main / `4823ba69ca65fa707fb89406f3a4c43c9e0053dd`。1188 个文本源文件参与全仓候选扫描；202 条词法命中不等于 202 个动画。

## 阅读导航

1. [设计语言](design-language/overview.md) → [Token](design-language/tokens.json) → [布局](design-language/layout.md)
2. 按需选组件或动画，然后读取同目录 spec.json。
3. [架构](architecture/overview.md) · [交互](interactions/overview.md) · [许可证](LICENSE-NOTES.md)
4. [覆盖范围与待办](BACKLOG.md) · [来源索引](references/source-map.json)

## 组件

- [AdaptiveSheet](components/adaptive-sheet/README.md)
- [CollapsibleBox](components/collapsible-box/README.md)
- [TwoPanelBox](components/two-panel/README.md)
- [CombinedCircularProgressIndicator](components/combined-progress/README.md)

## 动画

- [自适应面板锚点进出](animations/adaptive-sheet/README.md)
- [沉浸阅读控制层](animations/reader-bars/README.md)
- [快滚条显隐与拖动](animations/fast-scroller/README.md)
- [持续旋转的确定进度](animations/combined-progress/README.md)
- [交互驱动的按钮高度过渡](animations/button-elevation/README.md)
- [页面共享轴过渡](animations/shared-axis-navigation/README.md)

## 完成边界

核心资料可检索；原项目未构建、未运行、未录屏。完整候选清单在 references/animation-discovery.json；业务页面、依赖默认值和设备行为仍需后续深化。不要将“源码确认”理解为“运行效果确认”。
