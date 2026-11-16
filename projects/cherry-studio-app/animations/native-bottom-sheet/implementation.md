# 实现原理

detent由availableCardHeight和size/sizes/height计算；useEvent worklet接收native position，visibleCardStyle.height=clamp(position,minCardHeight,cardHeight)。多档保留选中高度，键盘压缩body。

## 生命周期与快速触发

React state同步open与openIndex；hasNotifiedCloseRef防重复回调。底层native中断/速度阈值未追溯，不补spring参数。

## 框架无关行为

输入：open/index改变、拖动、键盘出现

状态从 `{"index": 0}` 到 `{"index": "openIndex based on sizes"}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

BackHandler与overlay navigation包装负责关闭；依赖native Reduce Motion与焦点恢复需设备验证。

## 性能（静态分析，无 FPS 或内存实测）

原生拖动+UI worklet减少JS往返，但height跟随涉及内容布局，长列表、键盘和footer需专项测量。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`packages/ui/src/components/bottom-sheet/bottom-sheet.tsx:113` — `export function BottomSheet(props`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/bottom-sheet/bottom-sheet.tsx#L113)
