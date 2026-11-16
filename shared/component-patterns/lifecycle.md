# 可迁移组件的边界

从三项目提炼（inferred）的组件合同：视觉参数 + 输入状态 + 事件输出 + 生命周期 + 平台能力。仅复制颜色、圆角、CSS类不是完整迁移。

- Button：busy必须阻止重复提交并提供语义；不同平台尺寸可不同。Mobile没有通用按压spring，Desktop有hover/focus，不能强行视为同一动画组件。
- Overlay：区分open（业务意图）、retained（退出绘制）、interactive（能否操作）。Mobile菜单用完成回调保留；Desktop使用Radix Presence。Mihon平板关闭立即回调，不能自动继承完整退出保证。
- Sidebar：连续拖动预览与持久化提交可不同。Desktop50~120宽预览保存为50；Mobile侧列的yielded/permanent还依赖文件面板和折叠区域，不是同一阈值体系。
- Progress：未知进度和确定0%应分别建模；Mihon源码用0分支是具体设计，迁移可改为显式mode并标adapted。

来源：[Mobile组件](../../projects/cherry-studio-app/README.md)、[Mihon组件](../../projects/mihon/README.md)、[Desktop组件](../../projects/cherry-studio/README.md)。
