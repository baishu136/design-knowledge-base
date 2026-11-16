// Adapted from https://github.com/Droid-Deck/DroidDeck @ f65e7a3d436bee56f32626dc3536708d12e43162
// Source: app/src/main/java/com/droiddeck/launcher/ui/Theme.kt
// Attribution: DroidDeck contributors. GPL-3.0. Modified for this knowledge base.
// Hue-only controller, no ThemeColors palette/contrast generation. Caller owns motion preference.
import androidx.compose.animation.core.*
import androidx.compose.runtime.*

@Composable
fun HueCycle(speed: Int, reducedMotion: Boolean, initialHue: Float = 0f, onHue: (Float) -> Unit) {
    var lastHue by remember { mutableFloatStateOf(initialHue) }
    val callback by rememberUpdatedState(onHue)
    if (reducedMotion) return
    val bounded = speed.coerceIn(1, 10)
    key(bounded) {
        val start = remember { lastHue }
        val hue by rememberInfiniteTransition(label = "hue").animateFloat(
            initialValue = start, targetValue = start + 360f,
            animationSpec = infiniteRepeatable(tween(30_000 / bounded, easing = LinearEasing), RepeatMode.Restart),
            label = "huePhase",
        )
        val stepped = ((hue % 360f) / 3f).toInt() * 3f
        SideEffect {
            if (stepped != lastHue) { lastHue = stepped; callback(stepped) }
        }
    }
}
