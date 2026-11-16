# colors

tokens.json 收录默认 Tachiyomi 预设的日夜配对；XML 注释中的 Key colors 是配色生成种子，不等于 primary 实际值。浅色 primary=#0058CA。MONET 走 MonetColorScheme；AMOLED 先把背景/表面变黑、前景变白，再按主题条件覆盖容器灰阶。不要仅反转 RGB，也不要将依赖生成色当作固定 Token。未做设备壁纸动态色与对比度实测。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt:37` — `BaseTachiyomiTheme`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/theme/TachiyomiTheme.kt#L37)
- [`app/src/main/java/eu/kanade/presentation/theme/colorscheme/BaseColorScheme.kt:17` — `getColorScheme`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/app/src/main/java/eu/kanade/presentation/theme/colorscheme/BaseColorScheme.kt#L17)
- [`presentation-core/src/main/res/values/colors_tachiyomi.xml:13` — `tachiyomi_primary`](https://github.com/mihonapp/mihon/blob/4823ba69ca65fa707fb89406f3a4c43c9e0053dd/presentation-core/src/main/res/values/colors_tachiyomi.xml#L13)
