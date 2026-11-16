# 覆盖范围与后续任务

状态：首轮核心系统完成建档；不是全量细读完成。全仓词法候选扫描共202条命中，非test/fixture/stories命中202条；同一动画可有多个命中，import也可能命中，禁止把这两个数当动画数量。

| 优先级 | 任务 | 验收条件 |
|---|---|---|
| P1 | 依赖默认值 | materialSharedAxisX/rememberSlideDistance、MaterialExpressiveTheme字体/shape和ProgressAnimationSpec逐版本回溯 |
| P1 | 运行验证 | Android设备测试sheet嵌套滚动、返回、旋转和AMOLED/Monet |
| P2 | 更多动画 | MangaInfoHeader展开、下载指示、ReaderNavigationOverlay、AnimatedVector XML逐个建档 |
| P2 | 传统阅读器 | pager/webtoon View动画、图片解码和资源释放路径深读 |

检索[候选清单](references/animation-discovery.json)，按path与categories去重后挑选。每增加一个条目必须真实阅读实现、绑定固定Commit、补sources和许可证；发现不存在某类型不创建占位动画。当前未建立录屏/截图目录，因为没有真实运行素材。
