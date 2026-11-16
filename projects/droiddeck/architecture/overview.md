# overview

Android入口和SessionActivity负责运行时/多显示与系统窗口；ui目录组织Compose界面及大量定制运动，core/session保存偏好与业务。UI技术栈由app/build.gradle固定：Compose BOM2024.02.00、Kotlin2.1.0、Java17，minSdk26/target28；README安装推荐Android9+，应与技术构建下限分开记录。

Motion在FrontEndScreen.kt定义而不在独立Motion.kt。tw/sp在scale=0返回snap，非零时保留基础Tween/Spring参数，系统Compose时钟再缩放；手写协程delay使用ms(base)=round(base*scale)。FocusGlide数值求解器则显式按scale调整dt。不要再给tw传入已经ms缩放的duration而双重缩放。

归档没有递归填充MaliBridge/Syncthing子模块；Linux/Steam/KDE等外部界面不属于本轮原生设计系统。未执行Gradle、Rust、Docker、部署和启动脚本。

## 来源与状态

source-verified：上面明确的实现事实。标为“分析”的解释为 inferred；未运行原项目。

- [`app/build.gradle:135` — `versionName "0.7.1"`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/build.gradle#L135)
- [`app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt:329` — `internal object Motion`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FrontEndScreen.kt#L329)
- [`app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt:189` — `private fun Modifier.focusGlideOverlay`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/app/src/main/java/com/droiddeck/launcher/ui/FocusGlide.kt#L189)
- [`.gitmodules:1` — `[submodule`](https://github.com/Droid-Deck/DroidDeck/blob/f65e7a3d436bee56f32626dc3536708d12e43162/.gitmodules#L1)
