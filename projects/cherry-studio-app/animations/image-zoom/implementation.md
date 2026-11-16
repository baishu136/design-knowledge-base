# 实现原理

savedScale/savedX/Y作手势基准；双击用-(event-center)*(2.5-1)并clamp。translateX、translateY在scale之前；普通pan更新不clamp，结束才限制。pinch没有围绕focal point重建变换。

## 生命周期与快速触发

复位完成回调finished后onZoomChange(false)；scale shared值会被新withTiming或手势直接写入。手势中断及saved值竞态尚未运行。

## 框架无关行为

输入：Pinch、Pan、doubleTap Race

状态从 `{"scale": 1, "translate": [0, 0]}` 到 `{"doubleTapScale": 2.5, "releaseScaleRange": [1, 4]}`。

以 spec.json 的 properties 与 timing 建立轨道；null 参数必须追溯依赖或由目标项目单独决策，并标注 adapted。业务状态先提交；退出中的节点只保留绘制，不继续接收旧业务动作。

手势：1倍pan disabled；Pinch+Pan Simultaneous；doubleTap与其Race。

## 无障碍

本文件未显式Reduce Motion；图片有accessibilityLabel，但放大/复位的替代按钮需产品层提供。

## 性能（静态分析，无 FPS 或内存实测）

变换不重新布局图片；大图decode、original分辨率、纹理占用仍可能造成卡顿。原图模式cachePolicy=disk且关闭downscale。

## 迁移边界

保留输入、输出与中断语义，再选择目标框架的动画 API。不要把一个框架的 spring 参数直接视为另一个求解器的同等节奏。原始属性的布局/绘制成本不能由“GPU 加速”概括。

- [`src/frontend/components/ArtifactPreview/components/ArtifactImageViewer/ZoomableImage.tsx:17` — `export function ZoomableImage`](https://github.com/CherryHQ/cherry-studio-app/blob/e6d157d2ea604ef65d38ca14e88ba92de706ad8a/src/frontend/components/ArtifactPreview/components/ArtifactImageViewer/ZoomableImage.tsx#L17)
