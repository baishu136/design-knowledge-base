# CombinedCircularProgressIndicator

`mihon.component.combined-progress` · source-verified · runtime unverified

## 用途

下载等任务进度反馈

## 结构

AnimatedContent→未知Material环/旋转确定Material环

## 参数

rotation2000ms；progress=0作为未知分支

## 交互状态

未知、确定、进度变化；无hover/pressed/focus定义

## 输入、输出与状态

progress:()->Float、modifier；不发业务完成事件

## 反馈与生命周期

动画与任务生命周期独立；达到1不自动卸载

## 框架无关迁移

将mode与progress分开更适合通用库；这是迁移建议而非原实现

## 最小用法（说明性片段，未编译）

```
CombinedCircularProgressIndicator(progress={ 0.65f })
```

## 限制

要求0%确定进度明确可见的场景

## 源码

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/CircularProgressIndicator.kt:40` — `fun CombinedCircularProgressIndicator`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/CircularProgressIndicator.kt#L40)
