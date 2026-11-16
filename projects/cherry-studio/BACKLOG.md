# 覆盖范围与后续任务

状态：首轮核心系统完成建档；不是全量细读完成。全仓词法候选扫描共1130条命中，非test/fixture/stories命中672条；同一动画可有多个命中，import也可能命中，禁止把这两个数当动画数量。

| 优先级 | 任务 | 验收条件 |
|---|---|---|
| P1 | 运行验证 | Electron验证Dialog/SelectorShell快速切换、嵌套portal、焦点恢复和PageSidebar resize |
| P1 | 性能验证 | 多栏width重排、虚拟列表动态目标、120Hz固定50帧时长差异 |
| P2 | 更多动画 | BrowserCursorAnimation、迁移confetti、locate/search闪烁、Skeleton、SortableList、右面板独立条目 |
| P2 | 无障碍覆盖 | 逐消费者核对shimmer/RAF reduced-motion，不以局部规则代表全仓 |

检索[候选清单](references/animation-discovery.json)，按path与categories去重后挑选。每增加一个条目必须真实阅读实现、绑定固定Commit、补sources和许可证；发现不存在某类型不创建占位动画。当前未建立录屏/截图目录，因为没有真实运行素材。
