# 实现原理

useFrameCallback在UI线程累加实际delta并限制64ms；uniforms由derived value传给一个Rect的SkRuntimeEffect。shader把周期映射到斜向光带，presence在周期两端衰减掩盖重启；底色亮度调节深浅主题效果。编译结果缓存于模块级cachedEffect。

## 生命周期与快速触发

active=false时setActive(false)并time=0；重新开始从起点。AppState和reduceMotionChanged订阅在卸载移除，frame cleanup关闭。

## 框架无关行为

输入：active && AppState.active && !reducedMotion

状态从 `{"time": 0, "uStatic": 0}` 到 `{"time": "mod1200 seconds; effect cycle2.4", "uStatic_when_inactive": 1}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：本实现没有直接手势轨道；通过状态驱动。

## 无障碍

初始useReducedMotion+动态AccessibilityInfo事件；减少动态时uStatic=1将shader输出alpha置0，仍保留进度语义与中性底。

## 性能（静态分析，无 FPS 或内存实测）

单shader减少节点，但每像素cos/exp/hash仍有GPU填充率成本；面积、DPR和并发卡片放大成本。缓存编译不代表像素计算缓存。低端设备可采用中性静态降级（原实现已有inactive/static路径）；无GPU时间或FPS实测。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`packages/ui/src/components/loading/image-generation-loader.tsx:106` — `function useLoaderClock`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/loading/image-generation-loader.tsx#L106)
- [`packages/ui/src/components/loading/image-generation-loader-effect.ts:3` — `const IMAGE_GENERATION_LOADER_SKSL`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/packages/ui/src/components/loading/image-generation-loader-effect.ts#L3)
