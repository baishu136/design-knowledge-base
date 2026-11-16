"""Source-backed DroidDeck analysis. No upstream source is modified or executed."""
from build import *

UI='app/src/main/java/com/droiddeck/launcher/ui/'
SHA='f65e7a3d436bee56f32626dc3536708d12e43162'

def build_project():
    p=project('droiddeck','source-repositories/droiddeck-'+SHA[:12],
        'https://github.com/Droid-Deck/DroidDeck',SHA,'0.7.1',['Android'],
        ['Kotlin 2.1.0','Jetpack Compose BOM 2024.02.00','Material3','Compose Canvas','Android View Animation','Coil 2.6.0'],
        '面向触摸、鼠标与手柄焦点的游戏启动器：深色分层底、双强调色渐变、可滑移焦点环、按钮原点扩张与场景升降面板；另有White Red浅色、True Black和动态RGB主题。分析对象为Android启动器UI，不将所承载的Steam/KDE桌面认作自身组件。',
        {'ui':[UI,'app/src/main/java/com/droiddeck/launcher/FrontEndActivity.kt'],
         'themes':[UI+'Theme.kt',UI+'ThemeColors.kt',UI+'AppScale.kt'],
         'motion':[UI+'FrontEndScreen.kt',UI+'FocusGlide.kt',UI+'SharedMotion.kt',UI+'LiftSheet.kt',UI+'PageFlood.kt',UI+'LaunchFlood.kt','app/src/main/res/anim']})
    p['license']='GPL-3.0'
    s=lambda f,sym:source(p,UI+f,sym)
    theme=s('Theme.kt','fun DroidDeckTheme')
    colors=s('ThemeColors.kt','internal object ThemeColors')
    motion=s('FrontEndScreen.kt','internal object Motion')
    focus=s('FocusGlide.kt','private fun Modifier.focusGlideOverlay')
    focusmod=s('FocusGlide.kt','internal fun Modifier.glideBorder')
    chip=s('SharedMotion.kt','internal fun BoxScope.ChipGlide')
    flood=s('LaunchFlood.kt','internal fun LaunchFlood')
    page=s('PageFlood.kt','internal fun PageFlood')
    card=s('CardDetailHost.kt','internal fun CardDetailHost')
    lift=s('LiftSheet.kt','internal fun LiftHero')
    widget=s('FrontEndWidgets.kt','internal fun PrimaryButton')
    text=s('FrontEndWidgets.kt','internal fun Title')
    layout=s('Layout.kt','internal fun LauncherLayout')
    scale=s('AppScale.kt','internal fun scaledAppDensity')
    tabs=s('SettingsWidgets.kt','internal fun TabStrip')
    picker=s('ColorPickerDialog.kt','internal fun ColorPickerDialog')
    throbber=s('Throbber.kt','internal fun LogoThrobber')
    rgb=s('Theme.kt','private fun InnerGamerCycle')
    rise=source(p,'app/src/main/res/anim/session_rise.xml','<set')
    sink=source(p,'app/src/main/res/anim/session_sink.xml','<set')
    activity=source(p,'app/src/main/java/com/droiddeck/launcher/SessionActivity.kt','overridePendingTransition(R.anim.session_hold, R.anim.session_sink)')
    sessionLaunch=source(p,'app/src/main/java/com/droiddeck/launcher/FrontEndActivity.kt','R.anim.session_rise')
    themeDoc=source(p,'docs/development/themes.md','# Themes')
    gradle=source(p,'app/build.gradle','versionName "0.7.1"')
    # Literal palette blocks only. Generated/dynamic colours are kept as formulas, not fabricated samples.
    theme_text=text_file(p['root'],UI+'Theme.kt')
    for block in re.finditer(r'Palette\(\s*(GRAPHITE|PAPER|ICON_BLUE|ELECTRIC|WHITE_RED),([\s\S]*?)\n\s*\),',theme_text):
        name=block.group(1).lower()
        for val in re.finditer(r'(\w+)\s*=\s*Color\((0x[0-9A-Fa-f]+)\)',block.group(2)):
            role,raw=val.groups(); needle=val.group(0)
            # Exact occurrence inside this block, since white/green values recur in other themes.
            offset=block.start(2)+val.start()
            ref=dict(path=UI+'Theme.kt',symbol=f'Themes.{name}.{role}',line=theme_text[:offset].count('\n')+1,commit=SHA,
                sha256=hashlib.sha256((p['root']/(UI+'Theme.kt')).read_bytes()).hexdigest(),url=f"{p['repo']}/blob/{SHA}/{UI}Theme.kt#L{theme_text[:offset].count(chr(10))+1}")
            p['sources'][name+'.'+role]=ref
            token(p,role,'#'+raw[2:].upper(),'ARGB hex',f'Themes.{name}的显式调色板角色；不是系统夜间模式自动反转',ref,name)
    for name,value,unit,use,ref in [
        ('palette.error','#FFFF8A80','ARGB hex','Palette构造器默认错误色',s('Theme.kt','val good: Color, val error:')),
        ('motion.ease',[.2,.8,.2,1],'cubic-bezier','Motion.tw默认曲线',motion),
        ('focus.fill',.14,'ratio','glide默认填充',focus),
        ('focus.lead',{'dampingRatio':.62,'stiffness':700},'spring ratio/stiffness','移动方向前缘',focus),
        ('focus.trail',{'dampingRatio':.78,'stiffness':360},'spring ratio/stiffness','尾缘，基础延后30ms',focus),
        ('focus.follow',{'dampingRatio':1,'stiffness':2400},'spring ratio/stiffness','布局目标继续移动时跟随',focus),
        ('focus.integrationSubstep',4,'ms','手工弹簧积分最大子步',focus),
        ('layout.narrowThreshold',600,'configuration dp','isNarrowScreen严格小于600',layout),
        ('layout.narrowPaneWidth',520,'dp','NarrowPaneWidth常量；不等同屏幕断点',layout),
        ('shape.control',12,'dp','Shape12',motion),
        ('shape.sheet',18,'dp','LiftSheet SheetCorner',lift),
        ('sheet.inset',12,'dp','LiftSheet左右inset',lift),
        ('button.minHeight',48,'dp','非compact/非pill最小高',widget),
        ('button.compactMinHeight',44,'dp','compact最小高',widget),
        ('button.pillMinHeight',40,'dp','pill最小高',widget),
        ('button.scalePressed',.955,'ratio','按压目标',widget),
        ('button.scaleHot',1.02,'ratio','hover/focus hot目标',widget),
        ('text.title',26,'sp','Title组件',text),
        ('text.lede',13,'sp','Lede组件',text),
        ('text.eyebrow',12,'sp','章节标题',text),
        ('text.eyebrowTracking',1.5,'sp','章节标题字距',text),
        ('theme.rgbHueStep',3,'degrees','将整应用主题状态按3度量化更新',rgb),
        ('theme.gradientMinimumContrast',4.5,'ratio','渐变onPrimary算法阈值，不是全界面合规结论',colors),
        ('theme.gradientSamples',33,'samples','0..32采样点，额外.02对比度余量',colors),
    ]: token(p,name,value,unit,use,ref)
    token(p,'gradient.background.hsv',{'saturation':.5,'brightness':.045,'hue':'first corrected accent hue','saturationStrength':'clamp(primarySaturation/.35,0,1)'},'HSV formula','由ThemeColors.palette生成，不填固定hex',colors,'gradient')
    token(p,'theme.rgbCycle','30000 / clamp(speed,1,10)','ms formula','默认speed3即基础周期10000ms；系统动画比例另影响实际时钟',rgb,'inner_gamer')
    token(p,'app.scaleOptions',[75,85,100,115,125,150],'percent','LocalDensity及Configuration一起缩放，保留系统fontScale',source(p,'app/src/main/java/com/droiddeck/launcher/core/AppUiPrefs.kt','val scales'))

    doc(p,'design-language/overview.md','''源码与官方themes.md：Palette定义五层表面/边界、两级文本、primary/primary2/onPrimary/signal/good/error。主动作按钮使用渐变；焦点通过独立覆盖层滑移，手柄输入并非触摸反馈的附属物。

分析：辨识度来自深色层次、鲜明动作渐变、焦点的空间连续性以及按钮扩张成下一场景的因果关系。复现应保留焦点可见性、手柄/触摸双路径和主题配对；游戏封面、Steam商标及Linux桌面不是可随意迁移的原生UI资产。不要简化为“全局蓝黑Steam风”。''',[theme,themeDoc,widget,focus])
    doc(p,'design-language/colors.md','''固定预设含Graphite、Paper、Icon Blue、Electric和White Red；Paper实际是黑底白强调，不能按名称当作浅主题。White Red才是明确浅底红强调。DroidDeckTheme始终调用darkColorScheme映射Palette，即便Palette是浅色；不能从构造函数名推断最终背景。

Gradient通过readable把亮度过低的输入提升；inkFor在深墨#03111F/白之间按两端最差对比度选择，再fitTo和0..32渐变采样修正，目标4.5并留.02余量。该算法不是全部文字、边界和系统控件已通过无障碍认证的证据。True Black另由函数生成纯黑surface，动态主题须保留参数，未在tokens.json伪造一组不变颜色。Inner Gamer在色环上转动，经同一校正算法生成整组角色。''',[theme,colors,rgb])
    doc(p,'design-language/typography.md','''Theme中的ContentDirected由Material Typography默认角色派生，只改TextDirection.Content，不是完整自建字体字号表。局部实际组件：Title26sp Bold，Lede/Note13sp；章节标题12sp SemiBold，字距1.5sp；PrimaryButton large17/普通15/compact12sp、字距.5sp。这里只将这些局部值标为组件Token，不宣称全仓统一13/26刻度。

AppScale把Density乘用户百分比但保留fontScale，同时反向调整Configuration中的screenWidthDp等；字号和断点判断因此都受appScale影响。FittedLabel测量单行标签并以.5sp减小，最低10sp；长字符串适配与大字体可读性需实机检查，不能默认所有文本都自适应。''',[theme,text,widget,scale])
    doc(p,'design-language/spacing.md','''核心形状Shape12=12dp、Shape14=14dp、Shape16=16dp；面板SheetCorner18dp、左右SheetInset12dp。TabStrip外框12dp、内tab9dp、内层padding3dp、条间gap6dp。局部Button有复杂start/end/top/bottom参数，并非全仓8点网格。

LauncherLayout先测量导航，再扣除其宽或高以及1dp分隔线，内容拿到剩余固定Constraints。600dp为isNarrowScreen门槛；520dp为NarrowPaneWidth常量，两者不可互换。''',[motion,widget,tabs,lift,layout])
    doc(p,'design-language/materials.md','''表面层次主要用background/surface/surfaceVariant和line/line2。PrimaryButton用primary→primary2渐变，hot时阴影elevation目标14dp，rest6dp，并将ambient/spot颜色设signal；这是阴影变化，不只是scale的合成成本。

LiftHero用Canvas Path绘制曲边与rim、黑色.42遮罩，背景按1-.05*sink缩放；PageFlood用圆角路径clip封面并按cover比例缩放图像。CardDetailHost明确创建Offscreen图层用于顶部DstIn渐隐。这些效果不能笼统称作“模糊玻璃”或假设全部零重绘。''',[widget,lift,page,card])
    doc(p,'design-language/icons.md','''启动器使用Compose Material Icons，PrimaryButton接受ImageVector，可选图标尺寸普通17dp/large20dp且contentDescription=null（同一按钮已有文字）。设置导航的LB/RB是44dp触摸区内的文字键帽，提供contentDescription且不再进入普通焦点序列。LogoThrobber的品牌形状是Canvas路径，并非可无署名复用的通用加载图标；本库只记录行为，不搬运商标图像。''',[widget,tabs,throbber])
    doc(p,'design-language/layout.md','''底栏/侧栏由LauncherLayout(bottomNavigation)的调用方选择；isNarrowScreen<600用于若干紧凑内容和rail标签，不能说所有600dp窗口自动改成同一种导航。FrontEndScreen调用时dualScreen会禁用bottomNavigation；appScale改变用于判断的Configuration，双屏策略还需独立实机验证。

```mermaid
flowchart TD
 Theme[DroidDeckTheme + Palette + AppScale] --> Host[FocusGlideHost]
 Host --> Layout[LauncherLayout]
 Layout --> Rail[侧rail或底部导航]
 Layout --> Content[页面内容与游戏卡片]
 Content --> Detail[CardDetailHost保留退出]
 Detail --> Flood[PageFlood原点/目标矩形]
 Content --> Hero[LiftHero设置面板]
 Hero --> Pieces[分段进入 + 手柄焦点]
```

CardDetailHost把grid留在下面，detail打开时grid降至.95并淡出，关闭保留900ms×Motion.scale。它不是Android通用SharedTransitionLayout，而是记录卡片原点、手绘过渡层和内容树协作。''',[layout,scale,card,page,theme])
    doc(p,'architecture/overview.md','''Android入口和SessionActivity负责运行时/多显示与系统窗口；ui目录组织Compose界面及大量定制运动，core/session保存偏好与业务。UI技术栈由app/build.gradle固定：Compose BOM2024.02.00、Kotlin2.1.0、Java17，minSdk26/target28；README安装推荐Android9+，应与技术构建下限分开记录。

Motion在FrontEndScreen.kt定义而不在独立Motion.kt。tw/sp在scale=0返回snap，非零时保留基础Tween/Spring参数，系统Compose时钟再缩放；手写协程delay使用ms(base)=round(base*scale)。FocusGlide数值求解器则显式按scale调整dt。不要再给tw传入已经ms缩放的duration而双重缩放。

归档没有递归填充MaliBridge/Syncthing子模块；Linux/Steam/KDE等外部界面不属于本轮原生设计系统。未执行Gradle、Rust、Docker、部署和启动脚本。''',[gradle,motion,focus,source(p,'.gitmodules','[submodule')])
    doc(p,'interactions/overview.md','''手柄A确认只处理首次ACTION_DOWN，B/Back返回、LB/RB可切tab；hover/focus共同形成hot，而按压独立。TabStrip对选中项bringIntoView，提供Role.Tab/selectableGroup。焦点滑移层按窗口View身份绑定，弹窗有FocusGlideWindow避免跨窗口错位。

Motion.refresh读取应用animationsEnabled和Android ANIMATOR_DURATION_SCALE；部分入口refresh并不等于所有设置变化立即有监听，本轮未断言热更新。LiftHero在ON_STOP清open/shown/launching；关闭、手势取消和launching有不同路径。LaunchFlood覆盖阶段主动consume全部触摸，是源实现的暂时输入门闩，不应给所有目标UI普遍增加阻塞。

移植时必须分别验证触摸、键盘/手柄和读屏，不把焦点高亮的存在等同所有无障碍任务完成。''',[tabs,motion,lift,flood,focusmod])

    def anim(slug,name,category,refs,**kw):return animation(p,slug,name,category,refs,**kw)
    anim('focus-glide','保留速度的焦点环追随','focus',[focus,focusmod,motion],
        effect='四边分别追逐新控件，前缘先走、尾缘延后；远距离可收成圆点再展开。',trigger='glide.current/moves/hidden变化，窗口中的焦点或hot对象切换',
        start={'edges':'current rect','velocity':'retained per edge'},end={'edges':'focused control bounds','velocity':0},
        timing={'duration_ms':None,'delay_ms':{'trailing_edge':30,'no_source_grace':60},'easing':None,'spring':{'lead':{'dampingRatio':.62,'stiffness':700},'trail':{'dampingRatio':.78,'stiffness':360},'cross':{'dampingRatio':.7,'stiffness':520},'held':{'dampingRatio':.9,'stiffness':900},'follow':{'dampingRatio':1,'stiffness':2400}},'repeat':False},
        properties={'integration_substep_ms':4,'frame_dt_cap_ms':100,'settled_position_px':.3,'settled_speed_px_per_s':3,'repeat_window_ms':180,'far_distance_dp':360,'fill_alpha':.14,'base_width_dp':2,'bounds_tracking_max_ms':2000},
        mechanism='go写目标/弹簧参数和startAt；单帧协程将dt=min(frameDelta,.1)/max(scale,.01)，用h<=.004秒半隐式Euler：u+=(-k*(x-target)-2*zeta*sqrt(k)*u)*h，x+=u*h。保留vel数组，目标改变不排队。初入先长出3dp再收边。非连续按键且距离>360dp走droplet：90ms收成6dp半径点、220..380ms飞行，在progress>=.78改为弹簧展开；不是所有移动都走此分支。',
        interrupt='collectLatest替换观察任务；jobs数组分别取消边/圆角/solid/求解器任务。hidden或Motion.scale=0取消并snap；源或窗口失效不读取detach布局。bounds追踪450ms后至少稳定120ms或达到2s停止轮询。',
        accessibility='可见焦点与手柄导航是核心；scale0仍显示正确最终焦点，不是完全去除ring。跨View则回退静态border。没有TalkBack/大字体实测。',
        performance='drawWithContent重绘局部ring，避免改变目标组件布局；四轨4ms子步在极低scale下步数会增多，尤其dt cap在除scale之前。多层Job、窗口坐标跟踪和离屏内容仍有开销；没有FPS/CPU测量。',
        use='手柄/键盘主导的设置、游戏启动器和TV界面',avoid='无焦点模型的纯触摸页面或未经测量的跨窗口坐标共享')
    anim('chip-glide','标签选中背景的先后缘弹性','selection',[chip,motion],effect='胶囊选中底沿索引方向拉长再收拢；纵横轴可切。',trigger='index、at Rect、visible、Motion.scale',start={'start_end':'previous selection edges'},end={'start_end':'new selection edges','pinch':0},
        timing={'duration_ms':{'show':160,'hide':120},'delay_ms':{'trail':40},'easing':{'tween_cubic':[.2,.8,.2,1]},'spring':{'lead':{'dampingRatio':.62,'stiffness':700},'trail':{'dampingRatio':.78,'stiffness':360},'pinch_reset':{'dampingRatio':.6,'stiffness':500}}},
        properties={'fill_alpha':.16,'outline_alpha':.7,'outline_width_dp':1,'collapsed_radius_dp':6},
        mechanism='同一Canvas画背景；index决定lead/end与trail/start谁先走，尾缘delay40ms后spring。glideShape在pinch=0使用边缘，在pinch=1变到中心±drop。当前ChipGlide只将pinch归0，不能据此宣称每次必有pinch收球阶段。',
        interrupt='LaunchedEffect键改变取消旧协程；初次/同index/无上次或scale0直接snap。看不见或shown<.5先把几何移到目标以避免看见穿越。',
        accessibility='Keyboard输入模式时此ChipGlide本身不显示，交给其他焦点反馈；不能把胶囊背景当唯一可访问选中语义。',performance='Canvas绘制替代每个tab独立布局动画；Rect测量与Compose状态仍需布局消费者配合。',use='短tab/选项chip的触摸选择反馈',avoid='将其直接当键盘焦点环使用')
    anim('launch-flood','按钮四边扩张到启动场景','container-transform',[flood,motion],effect='按钮渐变圆角框按四边距离不同节奏铺满屏幕，背景缩至.96。',trigger='LaunchOrigin取到有效按钮bounds；Canvas测量完成',start={'edge_progress':[0,0,0,0],'from':'button rect'},end={'edge_progress':[1,1,1,1],'covered':True},
        timing={'duration_ms':None,'delay_ms':{'per_edge':'round(180*(1-travel/far))*Motion.scale'},'easing':None,'spring':{'dampingRatio':.48,'stiffness':'lerp(110,190,travel/far)'}},
        properties={'behind_scale':[1,.96],'corner_rest_dp':12,'blob_corner_factor':.42,'origin_ttl_ms':1500,'edge_delay_max_ms':180},
        mechanism='每条边计算到屏幕对应边的travel与lead=travel/far，距离越远延迟越少且stiffness越高。边首次>=1后reached保持covered判定不随回弹反复变化；四边均触达即回调onCovered，不等待所有spring settle。圆角以sin(pi*mean)中间鼓起、渐变两端以mix=min(mean*2,1)向signal合并。',
        interrupt='LaunchedEffect/page生命周期取消；rememberUpdatedState保持回调新鲜。四边reached只在本次记忆状态中保留；重新启动业务需新实例。scale0立即覆盖并通知。',accessibility='VeilRing暂时遮去焦点；覆盖Canvas消费触摸，必须限定在真实启动交接；scale0走snap。',
        performance='每帧Canvas渐变+圆角重绘，目标变化不是系统共享元素。平均进度回调可能增加重组；大屏和背景合成面积需实测。',use='按钮触发不可逆场景交接/启动加载',avoid='无后续场景却吞输入的装饰动画')
    anim('page-flood','卡片至详情容器过渡','container-transform',[page,card,motion],effect='卡片原点手绘扩张到页面或目标Rect，内容在边缘完成后显现。',trigger='CardDetailHost open变化与PageOrigin/StoresMotion mark',start={'edges':[0,0,0,0],'tile_alpha':1,'content_alpha':0},end={'edges':[1,1,1,1],'tile_alpha':0,'content_alpha':1},
        timing={'duration_ms':{'target_content_in':240,'target_tile_out':220,'ordinary_content_in':320,'ordinary_tile_out':360,'exit_content':140,'retention':900},'delay_ms':{'target_lookup_timeout':300,'ordinary_edge_max':150,'ordinary_tile':60},'easing':{'tween_cubic':[.2,.8,.2,1]},'spring':{'ordinary_enter_ratio':.5,'ordinary_enter_stiffness':'lerp(150,260,lead)','target_enter':{'dampingRatio':.85,'stiffness':320}}},
        properties={'ordinary_grid_scale':[1,.95],'content_offset_dp':14,'ordinary_edges_ready':.995,'target_edges_ready':.9,'page_origin_ttl_ms':1000,'offscreen_fade_dp':14},
        mechanism='有onto时最多等300ms取目标并校验可见交叠，四轨spring到目标，内容在各轨>=.9后淡入；普通扩张按distance错峰，四轨>=.995后内容显现。drawTile用cover缩放Painter并clip圆角，尺寸非正跳过。CardDetailHost gridScale480ms、fade320ms+delay80，关闭保留PAGE_RETURN_MS900×scale，配合回流。',
        interrupt='effect由size-ready/leaving/sinks驱动；离开或DisposableEffect恢复glide.hidden。关闭open变null后保留旧shown；再开取消原delay。900ms是保留窗口，不是spring精确时长。',accessibility='覆盖详情时grid禁止focus enter、详情focus exit受步骤状态约束；Motion0由snap/延迟缩零处理，未运行验证竞态。',
        performance='CardDetailHost使用Offscreen和DstIn做滚动顶端渐隐；大幅封面放大与双内容树存活增加GPU填充/纹理/内存成本，不能称为零布局共享元素。',use='有可信原点和身份匹配的卡片详情',avoid='把过期原点或不同窗口坐标直接lerp')
    anim('button-press','主按钮按压与高亮光晕','feedback',[widget,motion],effect='按下缩至.955，hover/focus扩至1.02，阴影rest6→hot14dp。',trigger='InteractionSource pressed与rememberHot且enabled',start={'scale':1,'shadow_dp':6},end={'pressed_scale':.955,'hot_scale':1.02,'hot_shadow_dp':14},
        timing={'duration_ms':{'shadow':300},'delay_ms':None,'easing':{'shadow_cubic':[.2,.8,.2,1]},'spring':{'dampingRatio':.5,'stiffness':'Spring.StiffnessMedium (依赖常量未展开)'}},
        properties={'scale':[1,.955,1.02],'shadow_elevation_dp':[6,14],'disabled_shadow_dp':0},mechanism='animateFloatAsState scale以pressed优先；shadow独立tween。graphicsLayer再clip按钮形状、画渐变、glideBorder；普通按压不必引入整页LaunchFlood，但点击会登记原点供后续使用。',
        interrupt='目标切换由animateFloatAsState接管；enabled时hot才生效，disabled用surfaceVariant渐变及line2边框。LaunchOrigin.flooding匹配此按钮时alpha0避免复制画面叠在原件。',accessibility='Role.Button且enabled控制点击；键盘主动作FocusRequester在组件挂卸时登记计数。scale0不移除焦点语义。',performance='scale通常局部图层，彩色阴影仍可能增加绘制/合成开销；不要按scale成本评估整个效果。',use='游戏启动等高优先级动作',avoid='密集列表每个小按钮都常驻大型彩色阴影')
    anim('lift-sheet','场景升降面板与内容错峰','gesture-sheet',[lift,motion],effect='背景缩至.95，面板升起，启动按钮随动，12段内容分批显现。',trigger='open/launching或纵向drag/nested scroll',start={'lift':0,'ride':0,'sink':0,'pieces':0},end={'lift':1,'ride':1,'sink':1,'pieces':1},
        timing={'duration_ms':{'sink_open':260,'piece_open':220,'piece_exit':90,'sink_exit':300},'delay_ms':{'initial_lift':120,'piece_formula':'120+260+i*55','drag_piece_stagger':35},'easing':{'tween_cubic':[.2,.8,.2,1]},'spring':{'lift_open':{'dampingRatio':.7,'stiffness':380},'lift_exit':{'dampingRatio':1,'stiffness':380},'ride_exit':{'dampingRatio':.55,'stiffness':300}}},
        properties={'pieces':12,'scrim_alpha':.42,'behind_scale':[1,.95],'drag_progress_max':1.04,'flick_threshold_dp_per_s':600,'open_from_closed_threshold':.3,'stay_open_threshold':.7,'sheet_corner_dp':18},
        mechanism='常规open先pull到24、sink；120ms后lift/ride，piece_i延迟380+i*55后220ms进入。拖动直接snap相关轨，松手按速度±600dp/s优先，再用起始态不同的.3/.7阈值吸附；拖动后的piece错峰为35ms，不能与普通open的55ms混用。launching进入fold/foldTop另一分支。',
        interrupt='dragJob可取消；dragSettled阻止open效果重播并保留拖后焦点恢复。ON_STOP清open/shown/launching并注销observer。onDragCancel以0速度settle；后台返回和外部launch交接需实机验证。',accessibility='触摸/Keyboard模式分别处理焦点，open后延迟请求tab/指定控件，close恢复play；BackHandler仅open且非launching启用。手柄导航与读屏未同等验证。',
        performance='多Animatable+12个piece、多层Canvas path和背景层；手势follow每次scope.launch snap多轨，密集输入需关注任务频率和大内容绘制。无时帧测量。',use='全屏游戏Hero的设置/操作层',avoid='普通短确认框或不需要按钮联动的轻量菜单',gesture='用户拖动、rows nested scroll和速度tracker协作；手势方向与drop面板仲裁，解除时按状态和阈值吸附。')
    anim('inner-gamer','量化更新的动态RGB主题','theme-animation',[rgb,colors,motion],effect='primary和secondary沿相差60度色环变化，整应用配色随之更新。',trigger='主题选择inner_gamer，speed1..10，Motion.scale非0',start={'hue':'remembered rgbHue'},end={'hue':'start+360 loop; stored in 3 degree steps'},
        timing={'duration_ms':None,'duration_formula_ms':'30000/clamp(speed,1,10)','delay_ms':None,'easing':{'name':'LinearEasing'},'repeat':'infinite Restart','spring':None},properties={'hue_step_degrees':3,'accent_hue_offset_degrees':60,'default_speed':3,'speed_range':[1,10]},
        mechanism='key(speed)重建周期但起始hue从Themes.rgbHue保留；infiniteTransition线性推进360，stepped=floor((hue%360)/3)*3，再SideEffect写入状态。Palette生成仍执行readable与渐变对比度修正，故实际primary不是未经修正的HSV原值。',
        interrupt='离开主题移除周期组合；app Motion.scale0不建InnerGamerCycle。系统时钟动画比例另生效。代码没有本组件AppState后台监听，不能宣称显式后台停帧。',accessibility='关闭应用/系统动画可静止；动态色仍须维护文字配对。4.5算法覆盖onPrimary渐变样本，不代表其他角色全部合规。',performance='3度量化减少整组palette状态变动次数（每理想周期120个档位），但infiniteTransition仍按帧推进，SideEffect及校正计算不是只跑120帧。',use='明确由用户开启的个性化游戏主题',avoid='信息内容需要稳定语义颜色或低功耗常驻界面')
    anim('logo-throbber','品牌形变旋转加载器','loading',[throbber,motion],effect='Logo左侧形变、双侧绕中心旋转，中央球缩到.8后恢复。',trigger='组合挂载并running且Motion.scale非0',start={'phase':0,'ball_scale':1,'bend':0},end={'phase':'repeat1→0','ball_scale':1,'bend':0},
        timing={'duration_ms':1900,'delay_ms':None,'easing':{'clock':'linear','bend_cubic':[.5,0,.3,1],'turn_cubic':[.65,0,.35,1]},'repeat':'infinite'},
        properties={'rotation_degrees':[0,360],'bend_segments':[0,.1,.24,.76,.9,1],'rotation_interval':[.16,.84],'ball_scale':[1,.8,1]},
        mechanism='单线性loop驱动三组分段函数；bend在.10..24上升、.76..90下降；turn在.16..84做360；ball在.12..30缩小、.70..88恢复。remember缓存Path对象，几何点列表由LogoShape预建，Canvas每帧reset/rebuild path。',
        interrupt='still将绘制p强制0，但rememberInfiniteTransition的建立在still判断之前；仅从running=false不能证明clock停止。离开组合才解除本循环生命周期。',accessibility='Motion.scale0显示静止图案；本Canvas函数自身无progressbar语义参数，使用者需配文字/状态。',performance='缓存Path减少分配，但顶点计算和path绘制仍逐帧发生；不是Shader，不能宣称所有计算在GPU。无实际数据。',use='短时品牌加载反馈',avoid='大量列表实例、唯一无障碍进度反馈或复用Logo为通用无品牌资产')
    anim('session-activity','会话Activity上下交接','navigation',[rise,sink,activity,sessionLaunch],effect='进入从父高100%向上到0并alpha.6→1；退出向父高100%下移。',trigger='Activity overridePendingTransition调用',start={'enter_translateY':'100%p','enter_alpha':.6,'exit_translateY':0},end={'enter_translateY':0,'enter_alpha':1,'exit_translateY':'100%p'},
        timing={'duration_ms':{'enter':380,'exit':320},'delay_ms':None,'easing':{'enter':'@android:interpolator/decelerate_cubic','exit':'@android:interpolator/accelerate_cubic'},'spring':None},properties={'translateY_percent_parent':[100,0,100],'enter_opacity':[.6,1]},
        mechanism='res/anim set组合translate与alpha；sink只有translate，不补造退出fade。SessionActivity在没有可用Flood return目标等分支下使用sink；FrontEndActivity引用rise。它是Android传统View/Activity动画，不是Compose Motion.tw控制的同一个时钟。',interrupt='生命周期与窗口过渡由Android处理；再入、系统手势返回和动画关闭需设备验证。',accessibility='XML没有自建Reduce Motion分支；不把Motion.scale对Compose的处理自动套进这些系统动画。',performance='Activity层窗口变换较适合系统合成，但承载Surface/会话渲染的兼容性与内存不可从XML判断。',use='启动器和远端会话Activity的切换',avoid='复制成普通Compose局部卡片的变换规范')

    def comp(slug,name,refs,**kw):return component(p,slug,name,refs,**kw)
    comp('primary-button','PrimaryButton',[widget,motion],use='手柄/触摸共用的启动主动作',structure='Row+InteractionSource→graphicsLayer→gradient→glideBorder→Icon/Text',parameters='Shape12/pill；minHeight48/compact44/pill40dp；字15/17/12sp；图标17/20dp',states='enabled、pressed、hot、LaunchOrigin.flooding隐藏原按钮；禁用不是单纯alpha降低',api='text,enabled,main,compact,large,icon,fill,onClick；main登记primary FocusRequester',behavior='按压优先scale.955；hot1.02；点击记录bounds供LaunchFlood',migration='把原点登记、焦点模型与视觉动作分层，业务禁用条件不能只传给动画',example='PrimaryButton("Play", main=true, enabled=ready) { launch() }',avoid='依赖私有LocalFrontFocus/LaunchOrigin却声称独立可编译',related=['droiddeck.animation.button-press','droiddeck.animation.launch-flood'])
    comp('focus-host','FocusGlideHost与glideBorder',[focus,focusmod],use='整窗口手柄/键盘焦点提示',structure='Host管理hot来源栈；Modifier登记LayoutCoordinates/Shape；drawWithContent画统一ring',parameters='2dp热边/1dp静边；默认fill.14，focusGlide可设0；远距360dp策略',states='首次、方向移动、连按、远距droplet、布局跟随、hidden、跨窗口回退',api='glideBorder(hot,shape,hotColor,restColor,hotWidth,restWidth,hotFillAlpha)；Host/Window组合边界',behavior='claim/release维护热源；VeilRing遮蔽临时效果，坐标attach校验防读废布局',migration='需要窗口坐标系与焦点生命周期，不能把所有控件的border设为同一位置',example='FocusGlideHost { item(Modifier.focusGlide()) } // 私有项目环境用法',avoid='跨Activity/Popup直接共享同一个View host',related=['droiddeck.animation.focus-glide'])
    comp('tab-strip','TabStrip与BumperKey',[tabs],use='手柄LB/RB与触摸横向tab',structure='Row：可选LB→可滚动SelectableGroup→tabs→RB',parameters='外12dp/内9dp圆角，padding3dp，gap6dp；字compact12/常规14sp，键帽触摸盒44dp',states='on/hot/focused，溢出后tight padding16→10，选中bringIntoView',api='tabs,selected,onSelect,focusRequesters,bumpers,compact',behavior='Role.Tab/selected语义，环绕索引；tab不会由ChipGlide统一动画，本文件使用直接背景+glideBorder',migration='保留可达选中项与空列表约束；不要仅复制LB/RB标签',example='TabStrip(listOf("Games","Setup"),selected,{ selected=it })',avoid='tabs为空却启用模运算bumpers')
    comp('lift-hero','LiftHero',[lift],use='Hero页面的设置/启动复合层',structure='背景/遮罩→Canvas面板壁→tabs与rows→联动play按钮→分段piece',parameters='sheetInset12、corner18、pieces12；sheetTop=max(paneH/6,minAbove+buttonH/2-ride)',states='open/shown/dragging/launching/stopped；DropSheet仲裁',api='key,tabs,onOpen,onPrimary,background,words,button,rows,onOpenChange,drop',behavior='open时移焦点，Back关闭；ON_STOP清临时状态；启动先fold再onPrimary',migration='拆成geometry、presentation状态与业务启动回调，保留手势/焦点恢复顺序',example='LiftHero(key="game", tabs=tabs, onOpen={}, onPrimary=launch, background=bg, words=title, button=play, rows=settings)',avoid='普通弹窗无需移植整套Hero状态依赖',related=['droiddeck.animation.lift-sheet'])
    comp('card-detail-host','CardDetailHost',[card,page],use='从游戏grid进入详情且保留返回画面',structure='Offscreen渐隐Host→保留的grid Column→shown详情树→PageFlood',parameters='gridScale.95；fade顶部14dp；PAGE_RETURN_MS900基础窗口',states='open/shown/leaving/from；grid焦点在covering时拒绝enter',api='open:String?,detailScroll,gridScrolled,onDetailFocus,wrap,grid,detail及bleedInsets',behavior='打开读取StoresMotion卡片原点，关闭延迟清shown，重开取消旧effect',migration='稳定身份与可测量卡片原点优先，无法定位时必须有回退',example='CardDetailHost(open,scroll,{false},{},grid={ Grid() },detail={ key -> Details(key) })',avoid='无限保留所有详情或跨Window原点未换坐标',related=['droiddeck.animation.page-flood'])
    comp('color-picker','ColorPickerDialog',[picker,colors],use='自定义渐变和True Black强调色',structure='AppDialog→旧新swatch→触摸色轮→三ValueSlider→hex→OK/Cancel',parameters='maxWidth460dp；色轮168dp；ColorCube44dp；Swatch48dp；hue0..360 step5，S/V0..100 step2',states='输入合法/非法、触摸调整、controller调整、确认/关闭',api='title,initial:Int,onDismiss,onApply(Int)；parseHex仅3/6位，可选#',behavior='非法hex禁用OK；色轮是触摸路径，滑杆/hex提供其他输入方式',migration='保留原始候选与确认应用分离；Palette校正可改变所见最终颜色，不将picker原值当最终主题值',example='ColorPickerDialog("Primary",initial,onDismiss={open=false},onApply={ save(it) })',avoid='需要alpha/8位hex的编辑器，原实现只支持不透明色')
    comp('launcher-layout','LauncherLayout与AppScale',[layout,scale],use='底部/侧边导航与用户界面缩放',structure='自定义Layout测navigation→1dp line→剩余内容，placeRelative支持方向',parameters='narrowScreen<600dp；NarrowPaneWidth520；AppScale选75/85/100/115/125/150%',states='bottomNavigation切向；宽高约束重算；scaled density和configuration同步',api='bottomNavigation,divider,navigation,content,modifier；scaledAppDensity/scaledAppConfiguration',behavior='dualScreen调用处可强制侧栏；不是仅由orientation或600自动决定',migration='迁移时保留字体缩放、导航占位与断点基准；勿单独scale绘制画面让命中框失配',example='LauncherLayout(bottomNavigation=true,divider=pal.line,navigation={ Nav() },content={ Page() })',avoid='直接把Android Configuration dp当浏览器CSS px断点')
    return p

if __name__=='__main__':
    finish_project(build_project())
