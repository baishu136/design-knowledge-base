from build import *
import xml.etree.ElementTree as ET

MCORE='presentation-core/src/main/java/tachiyomi/presentation/core/'
MAPP='app/src/main/java/eu/kanade/presentation/'
UI='packages/ui/src/'
MUI='packages/ui/src/'
FE='src/frontend/'
DESK='src/renderer/'

m=project('mihon','source-repositories/mihon','https://github.com/mihonapp/mihon','4823ba69ca65fa707fb89406f3a4c43c9e0053dd','0.21.3',['Android'],['Kotlin','Jetpack Compose','Material3 Expressive','Voyager','Android Views'],
 '以书库与沉浸阅读为中心：Material 语义配色、多套主题和 AMOLED 覆盖；内容密集的列表/网格与可隐藏阅读工具栏共存。阅读器仍包含 Android View 路径，不能将项目整体视为纯 Compose。',
 {'ui':[MCORE+'components',MAPP,'app/src/main/java/eu/kanade/tachiyomi/ui/reader'],'themes':['presentation-core/src/main/res/values','presentation-core/src/main/res/values-night',MAPP+'theme'],'motion':[MCORE+'components',MAPP+'util/Navigator.kt']})
m['license']='Apache-2.0'
ms=lambda path,symbol,needle=None:source(m,path,symbol,needle)
theme=ms(MAPP+'theme/TachiyomiTheme.kt','BaseTachiyomiTheme')
basecolor=ms(MAPP+'theme/colorscheme/BaseColorScheme.kt','getColorScheme')
pad=ms(MCORE+'components/material/Constants.kt','class Padding')
typ=ms(MCORE+'theme/Typography.kt','Typography.header')
sheet=ms(MCORE+'components/AdaptiveSheet.kt','fun AdaptiveSheet')
bars=ms(MAPP+'reader/appbars/ReaderAppBars.kt','fun ReaderAppBars')
fast=ms(MCORE+'components/VerticalFastScroller.kt','val alpha = remember')
progress=ms(MCORE+'components/CircularProgressIndicator.kt','fun CombinedCircularProgressIndicator')
elevation=ms(MCORE+'util/Elevation.kt','animateElevation')
nav=ms(MAPP+'util/Navigator.kt','DefaultNavigatorScreenTransition')
twopanel=ms(MCORE+'components/TwoPanelBox.kt','fun TwoPanelBox')
collapsible=ms(MCORE+'components/CollapsibleBox.kt','fun CollapsibleBox')
display=ms('app/src/main/java/eu/kanade/tachiyomi/util/system/DisplayExtensions.kt','TABLET_UI_REQUIRED_SCREEN_WIDTH_DP')
for name,value in [('extraSmall',4),('small',8),('medium',16),('large',24),('extraLarge',32)]: token(m,'padding.'+name,value,'dp','MaterialTheme.padding 共享间距',pad)
for name,value in [('DISABLED_ALPHA',.38),('SECONDARY_ALPHA',.78)]:token(m,name,value,'ratio','禁用/次级内容透明度',pad)
token(m,'sheet.maxWidth',460,'dp','面板最大宽度',sheet)
token(m,'twoPanel.firstWidthMax',450,'dp','双栏起始列上限',twopanel)
token(m,'tablet.smallestWidth',720,'dp','Configuration.smallestScreenWidthDp 判定；可被项目配置覆盖',display)
for folder,mode in [('values','light'),('values-night','dark')]:
 path=f'presentation-core/src/main/res/{folder}/colors_tachiyomi.xml'
 for color in ET.fromstring(text_file(m['root'],path)).findall('color'):
  ref=ms(path,color.attrib['name']);token(m,color.attrib['name'],color.text,'hex','默认 Tachiyomi 预设；不是 MONET 动态色',ref,mode)
for name,value in [('surfaceContainer','#0C0C0C'),('surfaceContainerHigh','#131313'),('surfaceContainerHighest','#1B1B1B')]:token(m,'amoled.'+name,value,'hex','非 MONET 的 AMOLED 表面覆盖',basecolor,'amoled')
doc(m,'design-language/overview.md','''源码事实：TachiyomiTheme 按 AppTheme / 系统深浅色 / AMOLED 选择 ColorScheme，交给 MaterialExpressiveTheme；不是一套固定蓝色覆盖所有用户。Typography.header 从 bodyMedium 派生，以 onSurfaceVariant 和 SemiBold 建立组标题。

分析：其辨识度来自封面内容优先、Material 语义层次和可退出的阅读控制层。复现时保留 surface/onSurface 配对、书库状态与阅读内容的分层；可以调整主题色，不应把默认预设蓝当作品牌强制色。''',[theme,typ,basecolor])
doc(m,'design-language/colors.md','''tokens.json 收录默认 Tachiyomi 预设的日夜配对；XML 注释中的 Key colors 是配色生成种子，不等于 primary 实际值。浅色 primary=#0058CA。MONET 走 MonetColorScheme；AMOLED 先把背景/表面变黑、前景变白，再按主题条件覆盖容器灰阶。不要仅反转 RGB，也不要将依赖生成色当作固定 Token。未做设备壁纸动态色与对比度实测。''',[theme,basecolor,ms('presentation-core/src/main/res/values/colors_tachiyomi.xml','tachiyomi_primary')])
doc(m,'design-language/typography.md','''主主题没有传入自建 Typography 数值表，而是使用 MaterialExpressiveTheme 默认；本轮未把依赖默认字号伪写成项目定义。可确认的组标题为 bodyMedium.copy(color=onSurfaceVariant,fontWeight=SemiBold)。sp 会受 Android 字体缩放影响；移植时保留角色与缩放能力，不能把 dp 间距当成字号。''',[theme,typ])
doc(m,'design-language/spacing.md','''共享 Padding 为 4/8/16/24/32 dp。CollapsibleBox 标题行另用水平24、垂直12 dp；这是局部几何，不是额外全局刻度。TwoPanelBox 扣除左右 Insets 后，起始列=min(可用宽/2,450dp)，末列使用余量。''',[pad,collapsible,twopanel])
doc(m,'design-language/materials.md','''AdaptiveSheet 使用 shapes.extraLarge 和 surfaceContainerHigh；具体圆角由 Material 主题提供，本轮不补默认 dp。阅读工具栏取 surfaceColorAtElevation(3dp)，暗色 alpha=.9，浅色=.95。这里是色彩叠加，不是已证实的实时背景模糊。''',[sheet,bars])
doc(m,'design-language/icons.md','''本轮组件可确认使用 mihon.icons.materialsymbols.MaterialSymbols.Rounded 的上下箭头；CollapsibleBox 的装饰箭头 contentDescription=null，父级文字与点击负责语义。不能从这一处推断全仓图标全为同一套；阅读器及其他业务资源另在全仓清单中。''',[collapsible])
doc(m,'design-language/layout.md','''720dp smallestScreenWidthDp 是平板 UI 门槛，不是浏览器 viewport media query；Configuration 可受项目覆盖策略影响。手机 AdaptiveSheet 底部对齐并可拖，平板居中且最大460dp、不可滑动关闭。TwoPanelBox 只分配两列，不负责自己判断断点。

```mermaid
flowchart TD
 Theme[TachiyomiTheme] --> Screen[Voyager Screen]
 Screen --> Compact[手机 单栏/底部面板]
 Screen --> Wide[平板 双栏/居中面板]
 Reader[ReaderAppBars] --> Top[顶栏 上方滑出]
 Reader --> Nav[章节导航 横向或左右纵向]
 Reader --> Bottom[底栏 下方滑出]
```

列表与网格通过 Lazy 组件组织；FastScroller 在 placement 阶段读位置，减少滚动触发整组重组。尺寸旋转、极大字体与边到边 Insets 未实机验证。''',[display,sheet,twopanel,fast,bars])
doc(m,'architecture/overview.md','''presentation-core 放跨页面基础组件和主题扩展；app 的 eu/kanade/presentation 放具体功能的 Compose UI、导航包装；ui/reader 仍有传统 View 阅读器。domain/data/source-api/source-local 是数据和来源层，不应直接复制进通用组件。Navigator 的 saveableState 包住屏幕内容，返回由 BackHandler 分发。

迁移优先抽出颜色角色、几何公式和状态机，再替换 Voyager、Injekt/DI、业务 preferences；保留这些私有依赖会使“最小示例”无法独立使用。''',[nav,theme,sheet])
doc(m,'interactions/overview.md','''面板输入 enableImplicitDismiss 控制返回/手势入口；手机在隐藏锚点 settledValue=1 后通知 dismiss。平板分支 targetAlpha=0 后立即调用 onDismissRequest，调用方若卸载，淡出不一定完整可见，不能宣称两端都有完整350ms退出。快滚条只有可见且列表不在滚动时装配拖拽；拖拽越界值限制在轨道内。''',[sheet,fast])
animation(m,'adaptive-sheet','自适应面板锚点进出','gesture-sheet',[sheet],effect='手机从全高隐藏锚点滑至0；平板透明度0→1。',trigger='进入组合；返回/背景点击；纵向拖拽释放',start={'phone_offset':'containerHeight','tablet_alpha':0},end={'phone_offset':0,'tablet_alpha':1},timing={'duration_ms':350,'delay_ms':None,'easing':{'name':'tween default','parameters':None},'spring':None,'repeat':False},properties={'translateY':['containerHeight',0],'opacity':[0,1],'dismiss_threshold_dp':56},mechanism='AnchoredDraggableState 初始1，容器测量后建0@0与1@height两个锚点；LaunchedEffect animateTo(0)。nested scroll 在向上预滚动/向下后滚动消费位移，fling settle 使用 sheetAnimationSpec。平板 animateFloatAsState 只驱动 alpha。',interrupt='手机 observe settledValue，drop首值后只有到1才通知；协程随组合离开取消。平板关闭回调立即执行，没有等待 alpha=0 的门闩。',accessibility='BackHandler 及系统 Dialog 由包装层参与；本文件未显式读取减少动态效果。依赖/系统动画比例未验证。',performance='手机 offset 在布局 placement 阶段更新；可避免每帧重测整个内容，但仍需处理位置更新。大内容组合和嵌套滚动成本取决于内容。',use='带长内容与嵌套滚动的自适应选项面板',avoid='需要三档吸附点或能保证退出完成后卸载的场景，应另加状态机',gesture='UserInput delta→dispatchRawDelta；释放后settle；56dp位置阈值。速度阈值来自依赖，未知。')
animation(m,'reader-bars','沉浸阅读控制层','visibility',[bars],effect='顶栏上滑、底栏下滑、纵向导航向所在侧滑出，同时透明度变化。',trigger='visible Boolean',start={'visible':False,'offset':'±elementSize','alpha':0},end={'visible':True,'offset':0,'alpha':1},timing={'duration_ms':{'slide':200,'fade':150},'delay_ms':None,'easing':{'name':'tween default','parameters':None},'spring':None},properties={'translateY':'±height→0','translateX':'±width→0 (vertical chapter navigator)','opacity':[0,1]},mechanism='三处 AnimatedVisibility 共享 visible，将 slide 与 fade 用 + 并行组合。纵向导航按左右选择 LocalLayoutDirection，水平导航放到底部。',interrupt='AnimatedVisibility 负责过渡内容保留；反向触发由 Compose Transition 接管。实际快速连击视觉和生命周期未运行。',accessibility='此组件没有单独 Reduce Motion 分支；不要把隐藏状态仅改为alpha而留下可聚焦控件。',performance='slide/fade 不改变漫画图片本身；控制层透明表面仍产生叠绘。避免迁移时把整张超大图片参与动画。',use='阅读器、看图器的临时控制层',avoid='需要持续可见的重要错误或播放状态')
animation(m,'fast-scroller','快滚条显隐与拖动','scroll',[fast],effect='滚动显现、停留2秒、按平台时长淡出。',trigger='scrolled SharedFlow；拖动thumb',start={'alpha':0},end={'scrolling_alpha':1,'idle_alpha':0},timing={'duration_ms':None,'duration_source':'ViewConfiguration.getScrollBarFadeDuration()','delay_ms':2000,'sample_ms':100,'easing':{'name':'tween default','parameters':None}},properties={'opacity':[1,0],'thumb_length_dp':48,'thumb_thickness_dp':12,'radius_dp':6},mechanism='DROP_OLDEST 容量1事件流经sample(.1.seconds)，collectLatest 取消上次等待/淡出；允许显示时snapTo(1)，delay(2.seconds) 后animateTo(0)。graphicsLayer读取alpha，placement更新thumb位置。',interrupt='collectLatest 用新事件替换旧淡出任务；remember Animatable 保留当前值。LaunchedEffect 离开组合时取消。',accessibility='源码设置 systemGestureExclusion 仅在必要时启用；thumb拖动键盘与无障碍替代路径仍需专项审查。',performance='在placement读取scroll state的注释和代码可确认；sample限制事件处理，不表示以10FPS绘制。拖动scrollTo可能触发Lazy内容加载。',use='超长书库列表/网格',avoid='不能估算总滚动范围的无界内容或仅靠细条提供唯一导航',gesture='拖动累计delta并coerceIn轨道；scrollTo对应比例；释放后显隐仍由事件流管理。')
animation(m,'combined-progress','持续旋转的确定进度','loading',[progress],effect='未知进度与确定进度交叉淡入；确定进度圆环也持续旋转。',trigger='progress()==0f 分支；progress 数值更新',start={'progress':0,'mode':'indeterminate'},end={'progress':'>0','mode':'determinate rotating'},timing={'duration_ms':{'rotation':2000,'progress':None,'crossfade':None},'delay_ms':None,'easing':{'rotation':'LinearEasing','progress':'ProgressIndicatorDefaults.ProgressAnimationSpec'},'repeat':'rotation infinite restart'},properties={'rotate_degrees':[0,360],'progress':'animated target'},mechanism='AnimatedContent以progress()==0f为target；确定分支 rememberInfiniteTransition 旋转，animateFloatAsState 平滑进度。源码注释明确持续旋转是为了表达未卡住。',interrupt='切换模式由AnimatedContent保留过渡内容；旋转随确定分支组合生命周期。0同时承担未知进度含义，不能直接当真实0%确定进度。',accessibility='由Material进度组件提供基础语义；未发现本组件额外减少动态效果分支。',performance='一个旋转层+进度绘制，无需布局几何逐帧改变；大量列表行同时使用会增加持续绘制。',use='下载/解析中仍有工作进行的状态',avoid='必须将0%和未知进度区分的业务，需独立mode输入')
animation(m,'button-elevation','交互驱动的按钮高度过渡','feedback',[elevation,ms(MCORE+'components/material/Button.kt','val animatable = remember')],effect='根据press/hover/focus/drag改变 elevation；并非缩放。',trigger='Interaction流的前后态',start={'elevation':'from interaction target'},end={'elevation':'to interaction target'},timing={'duration_ms':{'incoming':120,'press_or_focus_outgoing':150,'hover_outgoing':120},'delay_ms':None,'easing':{'incoming':'FastOutSlowInEasing (依赖数值未追溯)','outgoing_cubic':[.4,0,.6,1]},'spring':None},properties={'elevation_dp':'由ButtonElevation状态决定，工具函数不固定端点'},mechanism='animateElevation 根据 to 优先、否则 from 选 TweenSpec；两者都无时 snapTo。默认交互进入120ms、离开150ms，hover离开120ms。原文件是Compose M3复制代码且保留AOSP版权。',interrupt='Animatable.animateTo 的协程取消与新目标协作；不能建立每次press排队的时间轴。',accessibility='同时处理FocusInteraction；disabled/未知态snap，无局部Reduce Motion判断。',performance='阴影高度改变可能增加渲染负担；不是单纯transform，需目标设备实测。',use='有层次阴影的按钮',avoid='扁平工具栏中的所有按钮统一抬高')
animation(m,'shared-axis-navigation','页面共享轴过渡','navigation',[nav],effect='Material shared axis X 表达向前/返回；不是共享元素封面过渡。',trigger='navigator.lastItem/lastEvent',start={'screen':'previous'},end={'screen':'lastItem'},timing={'duration_ms':None,'delay_ms':None,'easing':None,'spring':None,'source':'soup.compose.material.motion.animation.materialSharedAxisX'},properties={'slide_distance':'rememberSlideDistance() 依赖返回值；本轮未知'},mechanism='DefaultNavigatorScreenTransition 把非Pop视为forward；ScreenTransition用AnimatedContent和navigator.saveableState保存过渡屏幕状态。数字时长与距离委托composeMaterialMotion，不能套用本库其他fade参数。',interrupt='AnimatedContent与Voyager saveableState协作；BackHandler enabled=canPop。依赖在快速连续push/pop时的策略需运行验证。',accessibility='系统/依赖运动缩放与屏幕焦点恢复尚未运行核实。',performance='过渡期可能共存两个复杂屏幕；图片与列表资源需关注释放时机。',use='有明确层级的页面进入/返回',avoid='将shared axis误用为具有同一封面ID的共享元素动画')
component(m,'adaptive-sheet','AdaptiveSheet',[sheet],use='手机底部面板/平板居中面板',structure='Dialog包装→全屏Box→Surface→content',parameters='maxWidth460dp；extraLarge形状；surfaceContainerHigh；平板垂直padding16dp',states='open、dragging、settling、dismissed；无hover状态定义',api='isTabletUi、enableImplicitDismiss、onDismissRequest、modifier、content',behavior='见adaptive-sheet动画；平板关闭直接回调',migration='把两种呈现规则和dismiss生命周期分离；Insets由目标平台负责',example='AdaptiveSheet(isTabletUi=false, enableImplicitDismiss=true, onDismissRequest={ open=false }) { Text("Options") }',avoid='精确多档高度控制',related=['mihon.animation.adaptive-sheet'])
component(m,'collapsible-box','CollapsibleBox',[collapsible],use='设置/说明组的渐进披露',structure='Column→可点击Row(Text+Spacer+Icon)→AnimatedVisibility(content)',parameters='标题行px24dp/py12dp；header=bodyMedium+SemiBold',states='内部remember expanded初始false；箭头直接替换并无旋转插值',api='heading:String，content:@Composable；无对外expanded/onChange',behavior='AnimatedVisibility默认参数，本轮不填依赖默认时长',migration='抽象expanded Boolean；如要外部控制，应改编为受控组件并标注adapted',example='CollapsibleBox(heading="More") { Text("Details") }',avoid='必须跨页面持久化展开状态而不另设状态提升')
component(m,'two-panel','TwoPanelBox',[twopanel],use='大屏主从信息并列',structure='BoxWithConstraints→TopStart Box + TopEnd Box',parameters='可用宽扣除Insets；首列不超过450dp，末列余量；无内建断点',states='宽度变化重算；无拖拽或动画',api='startContent、endContent、modifier、contentWindowInsets',behavior='布局方向感知start/end；不是固定left/right',migration='available=W-insets；a=min(available/2,450dp)；b=available-a',example='TwoPanelBox(startContent={ Text("Info") }, endContent={ Text("Chapters") })',avoid='窄屏自动变单栏；调用方先判断')
component(m,'combined-progress','CombinedCircularProgressIndicator',[progress],use='下载等任务进度反馈',structure='AnimatedContent→未知Material环/旋转确定Material环',parameters='rotation2000ms；progress=0作为未知分支',states='未知、确定、进度变化；无hover/pressed/focus定义',api='progress:()->Float、modifier；不发业务完成事件',behavior='动画与任务生命周期独立；达到1不自动卸载',migration='将mode与progress分开更适合通用库；这是迁移建议而非原实现',example='CombinedCircularProgressIndicator(progress={ 0.65f })',avoid='要求0%确定进度明确可见的场景',related=['mihon.animation.combined-progress'])

a=project('cherry-studio-app','source-repositories/cherry-studio-app-e6d157d2ea60','https://github.com/CherryHQ/cherry-studio-app','e6d157d2ea604ef65d38ca14e88ba92de706ad8a','0.5.5',['iOS','Android'],['TypeScript','React Native 0.88.1','Expo 58','Reanimated 4.7.1','Gesture Handler','Skia','Uniwind'],
 '移动端中性优先、绿色动作强调、红色仅作品牌；移动自有Vercel/Geist Token，并不继续镜像桌面数值。CherryUI统一跨平台组件外壳，局部原生适配和可中断动效。',
 {'ui':[MUI+'components',FE+'components',FE+'features'],'themes':['packages/design-tokens/src/styles',FE+'styles/global.css'],'motion':[MUI+'motion.ts',MUI+'components/menu',MUI+'components/loading']})
ar=lambda path,symbol,needle=None:source(a,path,symbol,needle)
adesign=ar('DESIGN.md','## Motion')
amotion=ar(MUI+'motion.ts','export const easing')
menumotion=ar(MUI+'components/menu/menu-motion.ts','export const menuOpenMotion')
menuhook=ar(MUI+'components/menu/use-menu-motion.ts','export function useMenuMotion')
menupanel=ar(MUI+'components/menu/menu-panel.tsx','export function MenuPanel')
menucontent=ar(MUI+'components/menu/menu-content.tsx','export function MenuContent')
button=ar(MUI+'components/button/button.tsx','const rootBaseStyles')
switch=ar(MUI+'components/switch/switch-control/switch-control.tsx','export function SwitchControl')
asheet=ar(MUI+'components/bottom-sheet/bottom-sheet.tsx','export function BottomSheet(props')
texts=ar(MUI+'components/text-animation/text-animation.tsx','function RotatingPhrase')
effortpath=FE+'features/chat/components/ChatInput/effortSlider/'
effort=ar(effortpath+'hooks/useEffortSliderGesture.ts','export function useEffortSliderGesture')
effortconst=ar(effortpath+'utils/constants.ts','export const effortSliderSnapTiming')
zoom=ar(FE+'components/ArtifactPreview/components/ArtifactImageViewer/ZoomableImage.tsx','export function ZoomableImage')
loader=ar(MUI+'components/loading/image-generation-loader.tsx','function useLoaderClock')
shader=ar(MUI+'components/loading/image-generation-loader-effect.ts','const IMAGE_GENERATION_LOADER_SKSL')
atyp=ar(MUI+'utils/typography-scale.ts','const sizeSequence')
astyles=ar(FE+'styles/global.css','@import')
anav=ar('src/app/(drawer)/_layout.tsx','export default')
for name,n in [('fast',200),('base',250),('slow',350)]:token(a,'motion.duration.'+name,n,'ms','动效时长词汇，不要求每组件统一时长',amotion)
token(a,'motion.spring.settle',{'damping':31.5,'mass':1,'stiffness':248},'reanimated-physics','精确停靠',amotion)
for name,n in [('xs',(13,18)),('sm',(14,20)),('base',(16,24)),('lg',(18,28)),('xl',(20,26)),('2xl',(24,32)),('3xl',(32,40)),('4xl',(40,48)),('5xl',(48,56)),('6xl',(60,60)),('7xl',(72,72)),('8xl',(96,96)),('9xl',(128,128))]:token(a,'typography.'+name,{'fontSize':n[0],'lineHeight':n[1]},'RN logical point','step=0；用户step1/2会向后移档并封顶',atyp)
doc(a,'design-language/overview.md','''官方 DESIGN.md 明确中性优先、可读性优先、主题平价以及先用文字/间距建立层级。primary 为随主题变档的green-900，control-active为固定绿色开关轨道，brand=#ff5757仅为品牌。这三者不能合并成“Cherry红色主题”。

分析：视觉识别来自连续中性表面、紧凑文字与少量绿色强调。重现时保留动作色/品牌色分离、组间留白优先于卡片框；业务内容可以自由变化。mobile Token 已fork，不能套桌面数值。''',[adesign,ar('packages/design-tokens/src/styles/product.css','--control-active')])
doc(a,'design-language/colors.md','''调色板→Shadcn角色→Cherry产品语义→生成native.css→Uniwind class/useThemeColor。tokens.json 对生成文件的light/dark声明保留原始值和解析后的变量表达式。#f5f5f5浅背景、card为background-100；深色background随palette。scrim、border-subtle/strong/selected区分层级。灰阶不单调，不能按数字大小推断亮度。HeroUI保留muted/accent/accent-foreground名称，不可把桥接变量误当移动组件公共API。sidebar变量是契约占位，shadcn注释说明未被界面消费；不据此建立Sidebar组件。''',[ar('packages/design-tokens/src/styles/native.css','@variant light'),ar('packages/design-tokens/src/styles/shadcn.css','HeroUI' if 'HeroUI' in text_file(a['root'],'packages/design-tokens/src/styles/shadcn.css') else '--sidebar'),adesign])
doc(a,'design-language/typography.md','''13档sizeSequence从13/18到128/128；step=1/2将每个语义档移到后续值，超过末档封顶。Typography Token为默认step=0，不表示运行时锁定。移动typography.css没有自定义字体族时沿原生/宿主配置；本轮不把桌面Inter继承为移动字体。bold=600见native.css。按钮label默认font-medium、text-base。''',[atyp,button,ar('packages/design-tokens/src/styles/native.css','--font-weight-bold')])
doc(a,'design-language/spacing.md','''DESIGN.md规定采用Tailwind默认4/8/12/16/20/24/32/40/48/64刻度。按钮default水平px-4、垂直py-2.5，icon size-5；这是类值，RN端需由Uniwind转换。radius基础8px，rounded-xl=1.4倍=11.2，rounded-4xl=2.6倍=20.8；不要误用旧桌面圆角。BottomSheet的32圆角是当前源码局部常量，与文档“不得numeric borderRadius”的统一要求存在偏差，本库并列记录而不私自修复。''',[adesign,button,asheet,ar('packages/design-tokens/src/styles/native.css','--radius-xl')])
doc(a,'design-language/materials.md','''菜单MenuPanel用popover表面、2点blur随progress衰减，另有容器宽高插值；不只是合成层scale。图片生成Loader用单Skia Shader绘制珠光、光带和细纹，适配表面亮度；静止态uStatic把效果alpha置0，保留中性底。BottomSheet用原生presentation和scrim token，不推测其内部弹簧。''',[menupanel,menucontent,shader,loader,asheet])
doc(a,'design-language/icons.md','''本轮Button/Menu/BottomSheet均从@cherrystudio/app-icons使用单色图标。按钮按尺寸档指定size-4/5/6，Menu分组勾选与项目图标size-5。装饰图标与控件可访问标签分离；框架迁移时保留颜色继承与文字语义，不能仅带图标路径。未搬运商标图像。''',[button,menucontent,asheet])
doc(a,'design-language/layout.md','''src/app由Expo Router管理分组路由，(drawer)的命名是路由/宿主结构，不意味着存在传统桌面Sidebar。菜单根据窗口、safe area、anchor测量决定opensAbove/top/left，首帧等待panelHeight>0后播放。BottomSheet最大宽720，availableHeight=windowHeight-insets.top-12；compact/medium/large/full分别.4/.6/.8/1倍。多档面板保留吸附高度，键盘只压缩body；单档可跟随键盘内容高度。

```mermaid
flowchart TD
 Router[Expo Router] --> Feature[frontend/features]
 Feature --> UI[CherryUI public components]
 UI --> Native[平台原生适配]
 UI --> Token[Uniwind语义Token]
 Menu[测量anchor与panel] --> Progress[shared progress]
 Progress --> Shell[外壳宽高/位置]
 Progress --> Panel[内容透明度/位移/缩放/blur]
```

未记录统一横屏断点：当前取到的是组件约束而非全应用响应式规范。''',[anav,menucontent,asheet])
doc(a,'architecture/overview.md','''packages/design-tokens拥有颜色来源与生成校验；packages/ui拥有公开组件/动效词汇；src/frontend/features负责业务，shared与backend不应被复制进独立UI。平台同名文件.ios/.android提供native适配；例如Android spinner用ActivityIndicator以避免持续Fabric提交，iOS开关另有原生实现。根入口需要自定义development client，不能承诺Expo Go即可运行。''',[amotion,astyles,ar(MUI+'components/loading/spinner/spinner-control/spinner-control.android.tsx','export function SpinnerControl'),ar(MUI+'components/switch/switch-control/switch-control.ios.tsx','export function SwitchControl')])
doc(a,'interactions/overview.md','''Menu打开须完成测量；关闭立即pointerEvents=none及隐藏无障碍子树，但保留绘制至动画结束。Android键盘改变锚点时关闭菜单。ZoomableImage在1倍时禁用pan，避免抢导航；pinch/pan同时而doubleTap与其Race。开关Android/Web是items-start/end直接切换，不能宣称自定义spring。项目gesture arbitration文档自称设计目标，不应当作所有组件均已实现的事实。''',[menuhook,menupanel,menucontent,zoom,switch,adesign])
animation(a,'menu-panel','可中断展开菜单','presence',[amotion,menumotion,menuhook,menupanel,menucontent],effect='32点外壳展开至测量尺寸；内容右移40→0、.97→1、blur2→0，并淡入。',trigger='isOpen且isMeasured；关闭请求',start={'progress':0,'size':[32,32],'opacity':0},end={'progress':1,'size':'measured','opacity':1},timing={'duration_ms':{'open':350,'close':250},'delay_ms':None,'easing':{'open_cubic':[.34,1.25,.64,1],'close_cubic':[.22,1,.36,1]},'spring':None},properties={'container_width':[32,'menuWidth'],'container_height':[32,'visibleHeight'],'translateX':[40,0],'scale':[.97,1],'blur':[2,0],'opacity':'panel=p; container=min(4p,1)'},mechanism='一个shared progress连接容器几何与内容轨道。打开使用y控制点1.25的超调Bezier，关闭用settle。外壳向上展开时top随animatedHeight变化，以锚边保持视觉连接。不要把声明的menuFadeMotion200ms误记为这个useMenuMotion的独立淡入轨道。',interrupt='cleanup cancelAnimation并使旧finishExit失效；完成回调仅finished为真时runOnJS卸载。未完成退出重开从当前progress继续。',accessibility='useReducedMotion打开直接1，关闭duration0；关闭时立即移除交互和可访问子树。',performance='width/height会触发布局；blur可能增加离屏成本。panel固定内容宽、测量变化阈值>1减少回写抖动，但不等于零布局开销。',use='短列表锚定操作菜单',avoid='大面积多层实时blur或尚未测量即打开的面板')
animation(a,'rotating-text','短语弹簧切换','text',[amotion,texts],effect='短语上下8点位移和淡入淡出；方向可反转。',trigger='active phrase / direction / measured / still',start={'translateY':'±8','opacity':0},end={'translateY':0,'opacity':1},timing={'duration_ms':{'enter_fade':200,'exit_fade':120,'spring':None},'delay_ms':{'enter_fade':60},'easing':{'fade_cubic':[.22,1,.36,1]},'spring':{'damping':31.5,'mass':1,'stiffness':248}},properties={'translateY':'enterFrom→0→-enterFrom','opacity':[0,1]},mechanism='独立translateY spring和opacity timing；新短语若完全不可见则重置入场边，否则保持当前位置再设目标；测量层保证尺寸。弹簧时长未显式指定，420ms只能作为源码注释中的近似，不记为固定duration。',interrupt='每次effect先cancelAnimation两轨；源码注释称保留position/velocity，但显式取消后的速度连续性未运行确认，不保证C1连续。',accessibility='useReducedMotion或isEnabled=false走still；非active短语屏蔽无障碍后代。',performance='transform/opacity适合局部复合；同时挂载多个短语与测量文本有额外内存/排版成本。',use='生成状态、短状态文案',avoid='长篇正文持续滚动或依靠动画表达唯一业务状态')
animation(a,'effort-slider','离散滑杆磁吸','gesture',[effort,effortconst],effect='拖动跟手并靠近档位磁吸；释放200ms无回弹吸附。',trigger='Pan minDistance0；programmatic value change由组件处理',start={'position':'current fraction'},end={'position':'nearest stop fraction'},timing={'duration_ms':200,'delay_ms':None,'easing':{'name':'Easing.out(Easing.cubic)','formula':'1-(1-t)^3'},'spring':None},properties={'position_fraction':[0,1],'magnet_radius':'0.5 × adjacent stop gap'},mechanism='trackXToFraction先归一化；magnetize改变视觉position；nearestStopIndex变化时才runOnJS(onCommit)。onFinalize选最近档位，按reducedMotion立即赋值或withTiming。',interrupt='onFinalize包括取消路径；disabled禁用gesture。连续拖动用shared values更新，不为每帧建立JS状态；外部值同步仍需组件协作。',accessibility='reducedMotion参数直接跳最终值；手势hook本身不提供屏幕阅读器adjustable action，不能单独用作完整可访问slider。',performance='UI worklet负责每帧，JS仅跨档commit。大量档位或昂贵onCommit仍需限流/分离副作用。',use='少量离散模型推理档位',avoid='连续精确数值输入或密集档位不应保留同一磁吸范围',gesture='begin/update seek；finalize吸附；跨档commit去重。')
animation(a,'image-zoom','图片捏合/双击缩放','gesture',[zoom],effect='居中变换；双击以触点偏移为目标缩至2.5倍，再双击复位。',trigger='Pinch、Pan、doubleTap Race',start={'scale':1,'translate':[0,0]},end={'doubleTapScale':2.5,'releaseScaleRange':[1,4]},timing={'duration_ms':None,'delay_ms':None,'easing':None,'spring':None,'source':'withTiming 未显式传配置'},properties={'scale':'pinch更新仅下限1；释放才限制最大4','translate_clamp':'±dimension*(scale-1)/2','image_transition_ms':120},mechanism='savedScale/savedX/Y作手势基准；双击用-(event-center)*(2.5-1)并clamp。translateX、translateY在scale之前；普通pan更新不clamp，结束才限制。pinch没有围绕focal point重建变换。',interrupt='复位完成回调finished后onZoomChange(false)；scale shared值会被新withTiming或手势直接写入。手势中断及saved值竞态尚未运行。',accessibility='本文件未显式Reduce Motion；图片有accessibilityLabel，但放大/复位的替代按钮需产品层提供。',performance='变换不重新布局图片；大图decode、original分辨率、纹理占用仍可能造成卡顿。原图模式cachePolicy=disk且关闭downscale。',use='附件图片预览',avoid='地图式焦点稳定缩放或医学/像素精确图像工具需增强数学模型',gesture='1倍pan disabled；Pinch+Pan Simultaneous；doubleTap与其Race。')
animation(a,'native-bottom-sheet','原生底部面板高度跟随','gesture-sheet',[asheet],effect='原生面板在detent之间移动，JS外壳跟随native position更新可见高度。',trigger='open/index改变、拖动、键盘出现',start={'index':0},end={'index':'openIndex based on sizes'},timing={'duration_ms':None,'delay_ms':None,'easing':None,'spring':None,'source':'@swmansion/react-native-bottom-sheet programmatic/native behavior'},properties={'ratios':{'compact':.4,'medium':.6,'large':.8,'full':1},'top_inset':12,'max_width':720,'top_corner_radius':32,'keyboard_gap':12},mechanism='detent由availableCardHeight和size/sizes/height计算；useEvent worklet接收native position，visibleCardStyle.height=clamp(position,minCardHeight,cardHeight)。多档保留选中高度，键盘压缩body。',interrupt='React state同步open与openIndex；hasNotifiedCloseRef防重复回调。底层native中断/速度阈值未追溯，不补spring参数。',accessibility='BackHandler与overlay navigation包装负责关闭；依赖native Reduce Motion与焦点恢复需设备验证。',performance='原生拖动+UI worklet减少JS往返，但height跟随涉及内容布局，长列表、键盘和footer需专项测量。',use='跨iOS/Android统一选项面板外壳',avoid='完全脱离native provider的浏览器直接复制')
animation(a,'foil-loader','图片生成珠光 Shader','shader',[loader,shader],effect='珠光底上白色光带斜向扫过，显露光谱细纹与闪点，每2.4秒循环。',trigger='active && AppState.active && !reducedMotion',start={'time':0,'uStatic':0},end={'time':'mod1200 seconds; effect cycle2.4','uStatic_when_inactive':1},timing={'duration_ms':2400,'delay_ms':None,'easing':{'formula':'mix(cycle, cycle²*(3-2cycle),0.5)'},'repeat':'continuous when active','spring':None},properties={'default_size':208,'frame_delta_cap_ms':64,'clock_wrap_seconds':1200,'shader_uniforms':['uResolution','uTime','uStatic','uSurfaceColor']},mechanism='useFrameCallback在UI线程累加实际delta并限制64ms；uniforms由derived value传给一个Rect的SkRuntimeEffect。shader把周期映射到斜向光带，presence在周期两端衰减掩盖重启；底色亮度调节深浅主题效果。编译结果缓存于模块级cachedEffect。',interrupt='active=false时setActive(false)并time=0；重新开始从起点。AppState和reduceMotionChanged订阅在卸载移除，frame cleanup关闭。',accessibility='初始useReducedMotion+动态AccessibilityInfo事件；减少动态时uStatic=1将shader输出alpha置0，仍保留进度语义与中性底。',performance='单shader减少节点，但每像素cos/exp/hash仍有GPU填充率成本；面积、DPR和并发卡片放大成本。缓存编译不代表像素计算缓存。低端设备可采用中性静态降级（原实现已有inactive/static路径）；无GPU时间或FPS实测。',use='图片生成占位的单卡反馈',avoid='无限滚动里大量并发全尺寸Shader或必须给出确定完成百分比')
component(a,'button','CherryUI Button',[button],use='动作按钮与文字/图标动作',structure='Pressable→变体/尺寸Context→Label、可选icon/Spinner',parameters='default gap2 px4 py2.5 text-base；rounded/pill；default前景底/背景字，中性而非绿色',states='active opacity.8；disabled opacity.4；loading禁用及spinner；无自定义按压spring',api='variant、size、shape、icon、loading和Pressable事件；Label子组件',behavior='loading与disabled参与阻止提交；accessibilityRole=button',migration='保留业务busy/disabled与视觉态一致；不要移植源码内私有cn/Spinner路径',example='<Button onPress={save}><Button.Label>Save</Button.Label></Button>',avoid='需要纯Web hover状态全等复现，需平台适配')
component(a,'switch','SwitchControl（Android/Web）',[switch],use='布尔偏好控制',structure='Pressable track→描边thumb外壳→白色内芯',parameters='default44×24、thumb20；lg48×28、thumb24；sm36×20、thumb16；hitSlop8',states='value切items-start/end与control-active/border-selected；disabled.opacity40；无插值动画',api='value受控、onValueChange(!value)、disabled、size及accessibilityLabel',behavior='accessibilityRole=switch；checked/disabled同步',migration='UI控件几何与父行的触摸目标分离；iOS另走平台文件，不能混作一份源码',example='<SwitchControl value={enabled} onValueChange={setEnabled} accessibilityLabel="Enabled" />',avoid='把小轨道当唯一完整触摸目标且不保留hitSlop')
component(a,'menu','MenuContent / MenuPanel',[menucontent,menupanel,menuhook],use='锚定操作、分组菜单及勾选项',structure='MenuOverlay→Animated外壳→MenuSurface→Animated内容→ScrollView→MenuRow',parameters='preferredWidth208、maxHeight480；初始32×32；padding2 gap.5；行图标size5',states='未测量、打开、关闭保留、卸载；关闭禁止pointerEvents/无障碍后代',api='anchor,isOpen,items,onClose,onClosed；MenuItem的checked/disabled/destructive及onPress',behavior='Android键盘变动关闭旧锚定菜单；layout高差>1才更新',migration='分离测量、定位、生命周期与渲染轨道；首次height=0时不启动',example='<MenuContent anchor={anchor} isOpen={open} items={items} onClose={close} onClosed={afterClose} />',avoid='不受控的全屏内容或长列表里每项都加blur',related=['cherry-studio-app.animation.menu-panel'])
component(a,'bottom-sheet','CherryUI BottomSheet',[asheet],use='统一移动面板壳',structure='BottomSheetProvider→ModalBottomSheet→header/body/footer',parameters='maxWidth720；topRadius32；topInset12；sizes compact/medium/large/full',states='closed/open/resizable/keyboard；dismissible决定关闭能力和handle',api='open,onClose；height/size/sizes互斥联合；title,footer,avoidKeyboard,onSizeChange',behavior='保留native position；close回调去重；多档键盘不更改snap points',migration='保留互斥尺寸API和safe-area模型；换框架需换native provider',example='<BottomSheet open={open} onClose={close} size="medium" title="Options">{content}</BottomSheet>',avoid='直接复制到DOM却假定native动画参数仍有效',related=['cherry-studio-app.animation.native-bottom-sheet'])

d=project('cherry-studio','source-repositories/cherry-studio-c3263227592a','https://github.com/CherryHQ/cherry-studio','c3263227592ad14313da2b4153bf88502c466454','2.2.2',['Windows','macOS','Linux'],['TypeScript','React 19','Electron 45','Tailwind CSS 4','Radix UI','Motion React'],
 '内容优先的多栏AI工作台：中性应用外壳、表面色分层、可调整导航与资源栏；共享Shadcn语义桥接内部cs-* providers，支持运行时主题输入。',
 {'ui':['packages/ui/src/components',DESK+'components',DESK+'pages'],'themes':['packages/ui/src/styles',DESK+'components/ThemeProvider.tsx'],'motion':[DESK+'assets/styles/animation.css',DESK+'components/chat/shell',DESK+'components/chat/messages/list/useSmoothScrollAnimation.ts']})
dr=lambda path,symbol,needle=None:source(d,path,symbol,needle)
ddesign=dr('DESIGN.md','## 1. Design direction')
dt=dr(DESK+'components/ThemeProvider.tsx','export const ThemeProvider')
dpane=dr(DESK+'components/chat/shell/PageSidebar.tsx','export function PageSidebar')
dpanet=dr(DESK+'components/chat/shell/paneLayout.ts','export const CHAT_SHELL_TRANSITION')
dbutton=dr(UI+'components/primitives/button.tsx','const buttonVariants')
dialog=dr(UI+'components/primitives/dialog.tsx','function DialogContent(')
dscroll=dr(DESK+'components/chat/messages/list/useSmoothScrollAnimation.ts','export function useSmoothScrollAnimation')
dcss=DESK+'assets/styles/animation.css'
dock=dr(DESK+'components/chat/motion/composerDockMotion.ts','export function useComposerDockMotionTransition')
sidebar=dr(DESK+'components/Sidebar/constants.ts','export function getSidebarLayout')
doc(d,'design-language/overview.md','''DESIGN.md明确content-first、neutral-first和语义化共享层。surface色承担深度，静态容器不普遍依赖强阴影；导航区与对话、文档、代码内容分层。Button默认黑白中性动作，primary是可配置主题强调，不是每个按钮的底色。

分析：高信息密度通过可调多栏与收纳实现，不只是缩小字号。迁移时必须保留中心内容的可读宽度、侧栏折叠/调整与键盘操作；可替换业务导航项，不应整体复制IPC/数据服务。''',[ddesign,dbutton,sidebar,dpanet])
doc(d,'design-language/colors.md','''primitive→内部cs-* providers→theme-input→Shadcn公开角色→product→theme.css适配。tokens.json按root/.dark解析颜色链，保留变量表达式，不能把运行时useUserTheme输入当固定常量。浅色background=cs-white，foreground=oklch(.213 0 0)，sidebar=oklch(.9672 0 0)；dark来源分别覆盖而非反相。ThemeProvider从已加载偏好推导首帧，之后监听native主题，避免先提交OS错误主题的一帧。''',[dr(UI+'styles/tokens/colors/providers.css','--cs-background'),dr(UI+'styles/shadcn.css','--primary'),dt])
doc(d,'design-language/typography.md','''共享定义heading/body字体Inter；weight400/500/700；body12/14/16/18px对应rem=.75/.875/1/1.125，heading20/24/32/40/48/60。实际Button默认text-[13px]属于组件密度，不应把它覆盖成body-md。CJK字体fallback与实际字体安装/加载未实机验证。代码组件单独拥有monospace栈；本轮未逐个追溯。''',[dr(UI+'styles/tokens/typography.css','--cs-font-family-heading'),dbutton])
doc(d,'design-language/spacing.md','''spacing.css从4px(.25rem)到112px(7rem)提供16档；与Tailwind类共同使用，不把这些档位解释为严格全仓8点网格。cs-radius-md=.5rem，cs-radius-lg=.625rem，Shadcn --radius引用后者；适配后的rounded-*须读取theme.css，不能仅按cs-radius名称猜最终圆角。导航栏按钮30px盒/18px图标，默认按钮min-height30px/13px字，体现桌面密度。''',[dr(UI+'styles/tokens/spacing.css','--cs-size-5xs'),dr(UI+'styles/tokens/radius.css','--cs-radius-lg'),dbutton])
doc(d,'design-language/materials.md','''官方层级为background地面、card内容、popover短暂浮层、sidebar导航区。Dialog overlay黑50%、z80；content bg-card/shadow-xl/rounded-3xl且no-drag避免Electron标题栏拖拽吞点击。文本shimmer通过background-clip:text与background-position，不是Shader；will-change不能保证零重绘。''',[ddesign,dialog,dr(dcss,'.animation-shimmer {')])
doc(d,'design-language/icons.md','''Button使用lucide-react Loader，未显式尺寸的svg默认size4，icon-navbar强制18px；同角色图标继承currentColor。默认动作单色与品牌/状态图标分开；Sidebar头像可用图片、emoji或首字母，这不是把emoji当动作图标的规范。''',[dbutton,ddesign,dr(DESK+'components/Sidebar/primitives.tsx','export function UserAvatar')])
doc(d,'design-language/layout.md','''应用Sidebar宽<20隐藏、<120图标、否则full；图标标准50，max280。50~120的拖动预览可连续显示，但持久化归一为50。聊天资源栏默认240、min200/max360；窄宽自动收纳阈值540属于资源栏策略，不是全站断点；右侧inspector最小255且上限未固定。PageSidebar首次打开后保留children，关闭inert+aria-hidden，减少状态重置。

```mermaid
flowchart LR
 AppNav[应用导航] --> Resources[会话/资源列表]
 Resources --> Center[中心对话/文档]
 Center --> Inspector[右侧Inspector]
```

响应式是中心可用空间与面板宽度协商，不能照搬手机bottom tabs。具体resize hook、键盘splitter行为见源码，触屏与多DPI未运行。''',[sidebar,dpanet,dpane])
doc(d,'architecture/overview.md','''Electron main拥有系统服务、窗口和数据能力；renderer组合页面；packages/ui拥有框架共享primitives与主题契约；shared承载跨进程类型。ThemeProvider通过IPC读取native主题，并使用preference hook；组件迁移应替换宿主状态，而不是引入整个Electron主进程。

动画有三条实现路径：Tailwind/CSS data-state用于Radix presence；Motion React用于多栏宽度；自定义RAF用于明确阅读导航。不同路径的时钟与生命周期不相同，不抽成一个无差别“300ms动画”函数。''',[dt,dialog,dpane,dscroll])
doc(d,'interactions/overview.md','''Button loading同时disabled与aria-busy，busy视觉opacity.4；Dialog通过KeyboardLayer管理关闭后的焦点与嵌套portal，保留Content为Portal直接子节点以让Radix Presence接收ref。PageSidebar折叠后inert阻止隐藏内容被键盘访问。显式平滑滚动必须由调用方在用户中断时cancel；流式追随边缘是instant，不能对每个token排队smooth-scroll。''',[dbutton,dialog,dpane,dscroll])
animation(d,'resource-pane','资源栏宽度展开','layout',[dpane,dpanet],effect='侧栏width0→目标宽并淡入，拖动时即时跟随。',trigger='open Boolean；isResizing',start={'width':0,'opacity':0},end={'width':'resolvedWidth','opacity':1},timing={'duration_ms':300,'delay_ms':None,'easing':{'name':'Motion easeInOut','parameters':None},'while_resizing_ms':0,'spring':None},properties={'width':'0 ↔ var(--assistants-width)/override','opacity':[0,1]},mechanism='AnimatePresence initial=false；motion.div animate依据open。hasOpened让首次打开后的children继续保留；closed态width0/opacity0而不是每次重挂载。isResizing直接transition duration0。',interrupt='Motion新目标接管当前值；React保留树维持列表状态。关闭inert/aria-hidden即刻变化，不等待视觉结束。',accessibility='有键盘splitter props；本组件未直接useReducedMotion，本轮不保证宿主全局覆盖。',performance='width动画必须重排相邻主内容，文本折行/虚拟列表测量可能昂贵；暂停复杂编辑器resize工作或缩短过渡是目标项目优化建议，非原实现已完成。',use='桌面主从面板',avoid='大量复杂子树每帧全布局或手势期间仍加缓动')
animation(d,'dialog','Dialog内容与遮罩','presence',[dialog],effect='遮罩淡入220ms，内容淡入并自下方进入260ms；两者退出200ms。',trigger='Radix data-state open/closed',start={'overlay_alpha':0,'content_alpha':0,'content_translateY':'bottom-4'},end={'overlay_alpha':.5,'content_alpha':1,'content_translateY':0},timing={'duration_ms':{'overlay_open':220,'content_open':260,'close':200},'delay_ms':None,'easing':{'open_cubic':[.16,1,.3,1],'close_cubic':[.4,0,1,1]},'spring':None},properties={'opacity':[0,1],'translateY':'directional时bottom-4→0；fade-scale分支当前没有显式scale类'},mechanism='Tailwind动画工具由data-state驱动；Content必须为Portal直接子元素，否则Radix Presence拿不到DOM ref就可能过早卸载。motion=fade-scale在本版本只关闭directional类，不能凭名称写出scale(.95)。',interrupt='Radix presence延迟卸载；KeyboardLayer释放跟焦点恢复协作。Imperative host卸载延迟另外定义，不能等同CSS时长。',accessibility='motion-reduce:animate-none；保留Dialog焦点和Escape行为需Radix/KeyboardLayer协作，不等于复制CSS即可实现模态框。',performance='opacity/translate适合局部复合；shadow-xl与大内容合成层增加开销。无实际层树或帧时间数据。',use='桌面模态确认/设置',avoid='将淡入CSS当成已实现focus trap的完整Dialog')
animation(d,'selector-shell','方向感知选择浮层','presence',[dr(dcss,'@keyframes animation-selector-shell-panel-enter')],effect='按浮层所在侧偏移半rem并从.95放大，外层同步fade；关闭缩小。',trigger='data-selector-shell-content的data-state和data-side',start={'scale':.95,'offset':'±.5rem','alpha':0},end={'scale':1,'offset':0,'alpha':1},timing={'duration_ms':{'open':150,'close':120},'delay_ms':None,'easing':{'outer_open':'ease-out','panel_open_cubic':[.16,1,.3,1],'close':'ease-in'},'spring':None},properties={'scale':[.95,1],'translate':'side maps to enter-x/y','opacity':[0,1]},mechanism='外层只负责透明度，直接子.animation-selector-shell-panel负责translate/scale，避免不同animation覆盖同一个transform。transform-origin用Radix Popover计算变量。',interrupt='CSS data-state切换；Presence的具体上层组件在本条规格中没有展开，不能保证快速切换无跳变。',accessibility='prefers-reduced-motion下外层/面板同时animation:none及transform:none；键盘导航由选择组件负责。',performance='transform/opacity为主；避免把尺寸计算放入每帧JS，锚点定位仍有布局测量。',use='model/provider选择器壳的出现',avoid='不同side改为同一方向而破坏触发点空间关系')
animation(d,'composer-dock','输入框归位反馈','transition',[dr(dcss,'@keyframes animation-chat-composer-dock-down'),dock],effect='home→docked输入框向下18px、scale.985→1、opacity.98→1。',trigger='previousPlacement=home且placement=docked',start={'translateY':-18,'scale':.985,'opacity':.98},end={'translateY':0,'scale':1,'opacity':1},timing={'duration_ms':220,'delay_ms':None,'cleanup_delay_ms':280,'easing':{'cubic':[.16,1,.3,1]},'spring':None},properties={'translateY':[-18,0],'scale':[.985,1],'opacity':[.98,1],'transform_origin':'center bottom'},mechanism='useLayoutEffect比较前后placement，只标记home-to-docked；属性函数添加CSS class；useEffect在280ms后清标记。220ms绘制时长与280ms清理窗口应分开。',interrupt='effect cleanup清timer；反向placement直接清transition，不播放相反动画。',accessibility='prefers-reduced-motion时取消动画与transform。',performance='只变transform/opacity，但布局位置本身由业务先改变，本动画并非FLIP测量任意距离。',use='首次对话后输入框回到固定位置的因果提示',avoid='泛化为任意两坐标之间共享元素过渡')
animation(d,'smooth-scroll','可取消的阅读定位滚动','scroll',[dscroll],effect='显式导航平滑追近每帧重新采样的目标偏移，最后吸附准确位置。',trigger='controller.scrollTo(getTargetOffset,options)',start={'offset':'current scrollTop'},end={'offset':'latest getTargetOffset()'},timing={'duration_ms':None,'frames':50,'delay_ms':None,'easing':{'formula':'1-2^(-10*t)'},'refresh_rate_dependent':True,'spring':None},properties={'scrollTop':'start + (liveTarget-start)*ease(frame/frames)'},mechanism='每次请求取消旧RAF，不排队；固定startOffset，对动态target每帧求值。frame>=frames时再取一次target并精确写入；完成仅正常终止回调。不是dt驱动，60Hz约833ms仅为理论换算，120Hz约417ms，不是FPS实测。',interrupt='cancel取消RAF清animating；unmount cleanup；DOM消失停止；用户输入中断需调用方主动cancel。',accessibility='hook没有读取prefers-reduced-motion，调用方应决定直接跳转；这是迁移建议。',performance='每帧scrollTop写入可导致滚动/虚拟列表更新；getTargetOffset若读取昂贵DOM几何会引起同步布局。高刷新屏幕时长会变，应在需要恒定节奏时改为时间驱动并标注adapted。',use='明确跳至某条消息',avoid='流式每token自动追随；原注释明确live-edge采用instant')
animation(d,'text-shimmer','文字流光等待态','loading',[dr(dcss,'@keyframes animation-shimmer')],effect='前景色渐变背景在裁成文字的区域移动，连续3秒循环。',trigger='animation-shimmer class attached',start={'backgroundPosition':'200% 0'},end={'backgroundPosition':'-200% 0'},timing={'duration_ms':3000,'delay_ms':None,'easing':{'name':'linear'},'repeat':'infinite'},properties={'background_size':'200% 100%','background_clip':'text','color':'transparent'},mechanism='渐变中间foreground、两端foreground25%透明混合；移动background-position而非文字几何。will-change声明提示优化，并不保证GPU复合。',interrupt='类移除停止CSS动画；再次附加通常重启。没有自定义相位保存。',accessibility='本CSS中没有对shimmer选择器的reduce-motion覆盖；不能因为同文件其他类有覆盖就泛化。透明文字在forced-colors/打印下需检查。',performance='background-position/clip:text可能逐帧paint；长文本或多行大量实例比小图标旋转更昂贵。没有基准数据。',use='短等待文案',avoid='长篇可读正文或低功耗界面持续常驻')
animation(d,'heatmap-entry','用量格子入场','entrance',[dr(dcss,'@keyframes animation-usage-heatmap-cell-enter')],effect='格子从.7倍透明进入至正常尺寸。',trigger='animation-usage-heatmap-cell-enter class attached',start={'scale':.7,'opacity':0},end={'scale':1,'opacity':1},timing={'duration_ms':520,'delay_ms':None,'easing':{'cubic':[.22,1,.36,1]},'spring':None},properties={'scale':[.7,1],'opacity':[0,1]},mechanism='本条提取CSS基础轨道。调用点可能额外设置animationDelay；本轮没有将业务错峰公式确认为项目全局规范。',interrupt='由CSS生命周期控制，非弹簧；重加类是否重播取决于DOM/浏览器样式刷新。',accessibility='prefers-reduced-motion时transform:none/animation:none。',performance='单格transform/opacity较轻，大量独立格子仍可能提高图层与调度成本；逐个will-change不是免费优化。',use='稀疏统计格子的首次出现',avoid='每次hover或每次数据轮询重播全部格子')
component(d,'button','Shadcn Button',[dbutton],use='桌面工具栏和表单动作',structure='button或Radix Slot→可选Loader+children',parameters='default min-h7.5/13px；navbar30px/18px图标；default黑白中性；shadow-xs',states='hover、focus-visible、disabled、busy、aria-invalid；disabled/busy opacity.4',api='variant,size,asChild,loading,loadingIcon,disabled及HTML button事件',behavior='loading同时disabled/aria-busy；asChild不插入loading子节点',migration='保留焦点可见态与业务busy禁用；Slot只接单节点，不直接照搬到RN',example='<Button loading={saving} onClick={save}>Save</Button>',avoid='以默认小尺寸作为移动触摸标准')
component(d,'dialog','Radix Dialog',[dialog],use='模态窗口与嵌套交互层',structure='KeyboardLayerRoot→Radix Root→Portal→Overlay与Content直接子节点→PortalContainerProvider',parameters='overlay黑50%/z80；content p6/gap4/bg-card/rounded3xl；size sm/default/lg/xl',states='open/closed/forceMount；closeOnOverlayClick可禁用',api='open/defaultOpen/onOpenChange；DialogContent motion,size,closeLabel,showCloseButton',behavior='Presence保留退出；焦点恢复后释放KeyboardLayer；嵌套tooltip portal跟层级',migration='先实现modal/focus/escape/portal，再加动画；no-drag是Electron专属适配',example='<Dialog><DialogTrigger>Open</DialogTrigger><DialogContent><DialogTitle>Options</DialogTitle></DialogContent></Dialog>',avoid='仅拷贝class忽略Radix与KeyboardLayer',related=['cherry-studio.animation.dialog'])
component(d,'resource-pane','PageSidebar',[dpane,dpanet],use='聊天资源/会话列表栏',structure='AnimatePresence→motion.div→裁切content和外侧resize handle',parameters='默认240/min200/max360；可用宽阈值540；motion300ms',states='未打开、打开、收起保留、resizing；收起inert',api='open,width,children,onPaneCollapse,onResizingChange',behavior='拖动duration0；键盘splitter调用setPaneWidth；首次打开后保留树',migration='保留可用宽协商、持久化和隐藏焦点策略；DOM惯性不能映射为alpha0',example='<PageSidebar open={open} onPaneCollapse={collapse}>{list}</PageSidebar>',avoid='把此组件当整应用Sidebar；两者宽度阈值不同',related=['cherry-studio.animation.resource-pane'])
component(d,'sidebar-width-policy','应用Sidebar宽度策略',[sidebar],use='导航栏hidden/icon/full三态',structure='纯策略函数：layout判定、显示宽、持久化宽分开',parameters='hidden<20；full>=120；icon50；max280；50~120为瞬态',states='拖动预览可中间宽；保存时收束到50',api='getSidebarLayout、getSidebarDisplayWidth、normalizeSidebarWidth',behavior='策略本身无动画；拖动组件负责输入/提交',migration='把连续预览和离散提交拆开，避免保存尴尬中间宽度',example='normalizeSidebarWidth(90) // 50\ngetSidebarDisplayWidth(90) // 90',avoid='误把120当所有窗口响应式断点')

aside=ar(FE+'appShell/sidebar/resolveSidebarColumn.ts','export function resolveSidebarColumn')
asideconst=ar(FE+'utils/constants.ts','export const appSidebar')
doc(a,'design-language/colors.md','''调色板→Shadcn角色→Cherry产品语义→生成native.css→Uniwind class/useThemeColor。tokens.json对生成文件light/dark声明保留原始值和解析后表达式。#f5f5f5浅背景、card为background-100；primary随green-900主题变档。灰阶不单调，不能按数字大小推断亮度。HeroUI的muted/accent/accent-foreground是保留桥接名，不能直接当移动公共工具类。

发现文档与实现不同步：shadcn.css注释说“mobile app has no sidebar”，但本Commit的DrawerLayout实际调用useThemeColor(['background','sidebar','sidebar-border','scrim'])，并渲染appShell/sidebar。此处以消费者实现为准；不能沿用该注释声称Sidebar未使用。这是源码冲突记录，不是本库对原项目的修复。''',[ar('packages/design-tokens/src/styles/native.css','@variant light'),ar('packages/design-tokens/src/styles/shadcn.css','--sidebar'),anav,adesign])
doc(a,'design-language/layout.md','''Expo Router的DrawerLayout实际承载Sidebar。窗口列策略分overlay/collapsed/yielded/permanent：窄窗overlay；文件面板占左列时yielded；折叠屏竖向分隔可按fold末端决定permanent宽；用户collapse在这些条件之后判断。不要把路由分组名或过时Token注释当作不存在Sidebar的证据。

overlay宽=min(400,windowWidth-64)，保留64点聊天条作为上下文和关闭入口；swipeActivationDistance20用来让表格/代码横向滚动先认领手势，swipe只在overlay且chatFocused启用。permanent与front切换保留内容树。

BottomSheet最大宽720；availableHeight=windowHeight-insets.top-12；compact/medium/large/full=.4/.6/.8/1。菜单首次测量panelHeight>0才播放，定位考虑safe area与空间。多档面板保留吸附高度，键盘压缩body。

```mermaid
flowchart TD
 Router[Expo DrawerLayout] --> Column{SidebarColumn策略}
 Column --> Overlay[窄窗front drawer]
 Column --> Permanent[宽窗/折叠区 permanent]
 Column --> Yielded[文件面板占列时让位]
 Router --> Feature[frontend/features]
 Feature --> UI[CherryUI组件]
 UI --> Native[平台适配与Token]
```

全应用isWide阈值和FoldRegion平台检测仍需进一步建档，不把400或720推成全局断点。''',[anav,aside,asideconst,menucontent,asheet])
doc(a,'design-language/typography.md','''默认13档sizeSequence从13/18到128/128；step=1/2将每个语义档向后移并封顶，tokens.json保留step0值。官方typography.css明确正文走各平台系统字体；等宽字体在global.css为GeistMono-Regular（RN接受单字体名）。font-bold被覆写为600，与font-semibold同重，这是明确定义而非误差。''',[atyp,ar('packages/design-tokens/src/styles/tokens/typography.css','--font-weight-bold'),ar(FE+'styles/global.css','--font-mono')])
component(a,'sidebar-column','自适应Sidebar列策略',[aside,asideconst,anav],use='手机抽屉、宽窗常驻列与折叠屏布局',structure='DrawerLayout→SidebarColumnProvider→resolveSidebarColumn→Drawer front/permanent',parameters='overlay最大400点且保留64点场景；手势水平激活20；header40/dock44',states='overlay、permanent、collapsed、yielded；fold可覆盖用户collapsed保证内容不跨铰链',api='isWide,isCollapsed,isPaneInColumn,fold,insets,windowWidth；输出kind/width/foldGap；toggle动作open/hide/show',behavior='文件pane占列优先让位；折叠区优先于普通collapsed；只有overlay+chatFocused启用swipe',migration='保留布局决策优先级；Drawer动画由平台导航库负责，不补原生spring',example='resolveSidebarColumn({isWide:false,isCollapsed:false,isPaneInColumn:false,content:"sidebar",windowWidth:390,insetLeft:0,insetRight:0,fold:null}) // overlay',avoid='将fold/insets硬编码成普通Web断点')

def css_tokens(p, paths, native=False):
    """Extract declarations + resolve aliases, without inventing browser computed values."""
    modes={'light':{},'dark':{}}
    records=[]
    for path in paths:
        content=text_file(p['root'],path)
        # Replacing comments with spaces preserves offsets and line numbers.
        clean=re.sub(r'/\*.*?\*/',lambda m:re.sub(r'[^\n]',' ',m.group()),content,flags=re.S)
        if native:
            blocks=[(q.group(1),q.start(2),q.group(2)) for q in re.finditer(r'@variant\s+(light|dark)\s*\{([^{}]*)\}',clean)]
        else:
            blocks=[]
            for q in re.finditer(r'(:root|\.dark)\s*\{([^{}]*)\}',clean):blocks.append(('dark' if q.group(1)=='.dark' else 'light',q.start(2),q.group(2)))
        for theme,offset,body in blocks:
            for v in re.finditer(r'(--[\w-]+)\s*:\s*([^;]+);',body):
                name,value=v.group(1),v.group(2).strip()
                line=clean[:offset+v.start()].count('\n')+1
                ref=dict(path=path,symbol=name,line=line,commit=p['commit'],sha256=hashlib.sha256((p['root']/path).read_bytes()).hexdigest(),url=f"{p['repo']}/blob/{p['commit']}/{path}#L{line}")
                p['sources'][path+'#'+theme+'#'+name]=ref
                modes[theme][name]=value;records.append((theme,name,value,ref))
    for mode,name,value,ref in records:
        env={**modes['light'],**(modes['dark'] if mode=='dark' else {})}
        def resolve(v,seen=()):
            def sub(match):
                key=match.group(1)
                return resolve(env[key],seen+(key,)) if key in env and key not in seen else match.group()
            return re.sub(r'var\((--[\w-]+)\)',sub,v)
        unit='CSS variable/expression'
        if value.startswith('#'):unit='hex color'
        elif value.startswith('oklch('):unit='OKLCH color'
        elif re.fullmatch(r'[\d.]+rem',value):unit='rem'
        elif re.fullmatch(r'[\d.]+px',value):unit='px'
        elif re.fullmatch(r'[\d.]+',value):unit='unitless'
        token(p,name,value,unit,'原始声明；颜色/间距/形状按变量命名检索；不是每条都被组件消费',ref,mode)
        p['tokens'][-1]['resolved_expression']=resolve(value,(name,))
        p['tokens'][-1]['computed_runtime_value']=None
        p['tokens'][-1]['definition_scope']=('@variant '+mode) if native else ('.dark' if mode=='dark' else ':root (inherited in dark unless overridden)')
        effective={}
        for target_mode in ['light','dark']:
            env={**modes['light'],**(modes['dark'] if target_mode=='dark' else {})}
            effective[target_mode]=resolve(env.get(name,value),(name,))
        p['tokens'][-1]['effective_theme_expressions']=effective
    # Dark mode also inherits unchanged root values; avoid duplicating the entire inventory.
    p['token_inheritance']='dark未覆盖的声明继承root；resolved_expression为静态别名替换，不评估calc/color-mix，也不考虑运行时custom CSS。'

selectorconsumer=dr(DESK+'components/SelectorShell.tsx','const SELECTOR_CONTENT_POSITION_CLASS')
shimmerconsumer=dr(DESK+'components/chat/messages/blocks/PlaceholderShimmerText.tsx','export function PlaceholderShimmerText')
for slug,spec,_ in d['animations']:
    if slug=='text-shimmer':
        spec['sources'].append(shimmerconsumer)
        spec['accessibility']='CSS基础类没有通用reduce-motion覆盖；PlaceholderShimmerText消费者另加motion-reduce:!animate-none。SessionItem/FileTree等其他消费者需分别检查，不能泛化为全部覆盖或全部缺失。forced-colors/打印未实测。'
    if slug=='selector-shell':
        spec['sources'].append(selectorconsumer)
        spec['interruption']='CSS data-state切换；SelectorShell声明destroy/lazy-keep两种挂载策略并用useExitPresence保留退出。lazy-keep仅建议高频列表，具体快速连击/焦点恢复未运行。'
css_tokens(a,['packages/design-tokens/src/styles/native.css'],native=True)
native='packages/design-tokens/src/styles/native.css'
for name,value in re.findall(r'(--radius-[\w-]+|--font-weight-bold)\s*:\s*([^;]+);',text_file(a['root'],native)):
    token(a,name,value,'CSS expression','生成适配层的共享形状/字重；保留rem、px和calc而不假设设备像素',ar(native,name),'all')
css_tokens(d,[UI+'styles/tokens/colors/primitive.css',UI+'styles/tokens/colors/status-legacy.css',UI+'styles/tokens/colors/providers.css',UI+'styles/tokens/spacing.css',UI+'styles/tokens/radius.css',UI+'styles/tokens/typography.css',UI+'styles/theme-input.css',UI+'styles/shadcn.css',UI+'styles/product.css'])
manifests=[finish_project(p) for p in PROJECTS.values()]
dump('references-build-summary.json',manifests)
print(json.dumps([{p['id']:{'components':len(p['components']),'animations':len(p['animations']),'tokens':len(p['tokens'])}} for p in PROJECTS.values()],ensure_ascii=False))
