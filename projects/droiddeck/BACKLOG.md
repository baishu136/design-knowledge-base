# 覆盖范围与后续任务

状态：首轮核心系统完成建档；不是全量细读完成。全仓词法候选扫描共1458条命中，非test/fixture/stories命中1316条；同一动画可有多个命中，import也可能命中，禁止把这两个数当动画数量。

| 优先级 | 任务 | 验收条件 |
|---|---|---|
| P1 | Android运行 | 验证控制器连按、远距droplet、跨Popup焦点、Motion开关与系统scale |
| P1 | 手势/交接 | LiftHero与DropSheet仲裁、ON_STOP恢复、PageFlood目标消失、LaunchFlood覆盖回调与Surface切换 |
| P1 | 性能测量 | 低scale数值步数、Offscreen封面、RGB主题校正重组和后台循环；不以模拟时钟数据代替FPS |
| P2 | 更多动画 | DropSheet、Iris、Hop、GlideWindows、Flights、Store下载、底屏与AgentPet逐项细读 |
| P2 | 未覆盖边界 | 子模块与Steam/KDE外部界面不计原生组件；依赖默认Typography/Shape常量及全量图标消费者继续核实 |

检索[候选清单](references/animation-discovery.json)，按path与categories去重后挑选。每增加一个条目必须真实阅读实现、绑定固定Commit、补sources和许可证；发现不存在某类型不创建占位动画。当前未建立录屏/截图目录，因为没有真实运行素材。
