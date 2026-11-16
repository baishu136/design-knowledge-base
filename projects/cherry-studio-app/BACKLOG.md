# 覆盖范围与后续任务

状态：首轮核心系统完成建档；不是全量细读完成。全仓词法候选扫描共534条命中，非test/fixture/stories命中406条；同一动画可有多个命中，import也可能命中，禁止把这两个数当动画数量。

| 优先级 | 任务 | 验收条件 |
|---|---|---|
| P1 | 原生运行 | 自定义Expo development client验证菜单反向触发、native sheet键盘和image zoom中断 |
| P1 | 性能验证 | Skia Shader在低端Android、后台、Reduce Motion动态切换下测量 |
| P1 | 侧栏补全 | WindowFoldRegion/isWide检测、drawer依赖内部动画与手势竞争实机验证 |
| P2 | 更多动画 | LogoDraw、WelcomeIntro、PaintingFocusCanvas、dot-matrix、ExpandedAnswer、composer overlay逐条建档 |
| P2 | 文档差异 | 跟踪上游sidebar过时注释和BottomSheet数字圆角与DESIGN规则的偏差 |

检索[候选清单](references/animation-discovery.json)，按path与categories去重后挑选。每增加一个条目必须真实阅读实现、绑定固定Commit、补sources和许可证；发现不存在某类型不创建占位动画。当前未建立录屏/截图目录，因为没有真实运行素材。
