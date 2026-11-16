# 实现原理

有onto时最多等300ms取目标并校验可见交叠，四轨spring到目标，内容在各轨>=.9后淡入；普通扩张按distance错峰，四轨>=.995后内容显现。drawTile用cover缩放Painter并clip圆角，尺寸非正跳过。CardDetailHost gridScale480ms、fade320ms+delay80，关闭保留PAGE_RETURN_MS900×scale，配合回流。

## 生命周期与快速触发

effect由size-ready/leaving/sinks驱动；离开或DisposableEffect恢复glide.hidden。关闭open变null后保留旧shown；再开取消原delay。900ms是保留窗口，不是spring精确时长。

## 框架无关行为

输入：CardDetailHost open变化与PageOrigin/StoresMotion mark

状态从 `{"edges": [0, 0, 0, 0], "tile_alpha": 1, "content_alpha": 0}` 到 `{"edges": [1, 1, 1, 1], "tile_alpha": 0, "content_alpha": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

覆盖详情时grid禁止focus enter、详情focus exit受步骤状态约束；Motion0由snap/延迟缩零处理，未运行验证竞态。

## 性能（静态分析，无 FPS 或内存实测）

CardDetailHost使用Offscreen和DstIn做滚动顶端渐隐；大幅封面放大与双内容树存活增加GPU填充/纹理/内存成本，不能称为零布局共享元素。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt:80` — `internal fun PageFlood`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/PageFlood.kt#L80)
- [`app/src/main/java/com/droiddeck/launcher/ui/CardDetailHost.kt:60` — `internal fun CardDetailHost`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/CardDetailHost.kt#L60)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
