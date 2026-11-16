# 语义层次与主题边界

三个项目都把语义角色与基础色分离，但实现不等价。Cherry Desktop运行时输入可以覆写主题强调；Mobile分离固定control-active与随主题primary；Mihon可动态生成Monet色，并有AMOLED覆盖。

通用提炼（inferred）：先定义角色和成对前景，再选调色板；布局分组先靠间距、对齐、文字层级，浮层再使用阴影或scrim。移植必须保留禁用、危险、选中与焦点的非颜色线索。

不适用：把CSS背景透明混合结果直接转换成固定Android hex，或把一个主题的数值覆盖所有深色/动态主题。CSS color-mix和OKLCH尚需目标渲染能力及对比度实测。

来源：[Mobile颜色](../../projects/cherry-studio-app/design-language/colors.md)、[Mihon颜色](../../projects/mihon/design-language/colors.md)、[Desktop颜色](../../projects/cherry-studio/design-language/colors.md)。
