# cherry-studio

内容优先的多栏AI工作台：中性应用外壳、表面色分层、可调整导航与资源栏；共享Shadcn语义桥接内部cs-* providers，支持运行时主题输入。

分析版本：2.2.2 / main / `c3263227592ad14313da2b4153bf88502c466454`。9949 个文本源文件参与全仓候选扫描；1130 条词法命中不等于 1130 个动画。

## 阅读导航

1. [设计语言](design-language/overview.md) → [Token](design-language/tokens.json) → [布局](design-language/layout.md)
2. 按需选组件或动画，然后读取同目录 spec.json。
3. [架构](architecture/overview.md) · [交互](interactions/overview.md) · [许可证](LICENSE-NOTES.md)
4. [覆盖范围与待办](BACKLOG.md) · [来源索引](references/source-map.json)

## 组件

- [Shadcn Button](components/button/README.md)
- [Radix Dialog](components/dialog/README.md)
- [PageSidebar](components/resource-pane/README.md)
- [应用Sidebar宽度策略](components/sidebar-width-policy/README.md)

## 动画

- [资源栏宽度展开](animations/resource-pane/README.md)
- [Dialog内容与遮罩](animations/dialog/README.md)
- [方向感知选择浮层](animations/selector-shell/README.md)
- [输入框归位反馈](animations/composer-dock/README.md)
- [可取消的阅读定位滚动](animations/smooth-scroll/README.md)
- [文字流光等待态](animations/text-shimmer/README.md)
- [用量格子入场](animations/heatmap-entry/README.md)

## 完成边界

核心资料可检索；原项目未构建、未运行、未录屏。完整候选清单在 references/animation-discovery.json；业务页面、依赖默认值和设备行为仍需后续深化。不要将“源码确认”理解为“运行效果确认”。
