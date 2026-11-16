# CollapsibleBox

`mihon.component.collapsible-box` · source-verified · runtime unverified

## 用途

设置/说明组的渐进披露

## 结构

Column→可点击Row(Text+Spacer+Icon)→AnimatedVisibility(content)

## 参数

标题行px24dp/py12dp；header=bodyMedium+SemiBold

## 交互状态

内部remember expanded初始false；箭头直接替换并无旋转插值

## 输入、输出与状态

heading:String，content:@Composable；无对外expanded/onChange

## 反馈与生命周期

AnimatedVisibility默认参数，本轮不填依赖默认时长

## 框架无关迁移

抽象expanded Boolean；如要外部控制，应改编为受控组件并标注adapted

## 最小用法（说明性片段，未编译）

```
CollapsibleBox(heading="More") { Text("Details") }
```

## 限制

必须跨页面持久化展开状态而不另设状态提升

## 源码

- [`presentation-core/src/main/java/tachiyomi/presentation/core/components/CollapsibleBox.kt:26` — `fun CollapsibleBox`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/java/tachiyomi/presentation/core/components/CollapsibleBox.kt#L26)
