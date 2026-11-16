// Adapted from https://github.com/Droid-Deck/DroidDeck @ f65e7a3d436bee56f32626dc3536708d12e43162
// Source: app/src/main/java/com/droiddeck/launcher/ui/LaunchFlood.kt
// Attribution: DroidDeck contributors. GPL-3.0. Modified for this knowledge base.
// Controller subset: four edge progress values and covered callback. No Canvas/brand/gesture blocking.
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.spring
import androidx.compose.runtime.*
import androidx.compose.ui.geometry.Rect
import androidx.compose.ui.geometry.Size
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.launch
import kotlin.math.roundToInt

@Composable
fun rememberLaunchEdges(from: Rect, viewport: Size, reducedMotion: Boolean, onCovered: () -> Unit): List<Float> {
    val edges = remember { List(4) { Animatable(0f) } }
    val reached = remember { mutableStateListOf(false, false, false, false) }
    val callback by rememberUpdatedState(onCovered)
    LaunchedEffect(from, viewport, reducedMotion) {
        if (viewport.width <= 0 || viewport.height <= 0) return@LaunchedEffect
        edges.forEach { it.snapTo(0f) }
        reached.indices.forEach { reached[it] = false }
        if (reducedMotion) {
            edges.forEach { it.snapTo(1f) }; reached.indices.forEach { reached[it] = true }
            callback()
            return@LaunchedEffect
        }
        val travel = listOf(from.left, from.top, viewport.width - from.right, viewport.height - from.bottom).map { it.coerceAtLeast(0f) }
        val far = travel.max().coerceAtLeast(1f)
        coroutineScope {
            val jobs = edges.mapIndexed { i, edge -> launch {
                val lead = travel[i] / far
                delay((180 * (1 - lead)).roundToInt().toLong())
                edge.animateTo(1f, spring(dampingRatio = .48f, stiffness = 110 + 80 * lead)) {
                    if (value >= 1f) reached[i] = true
                }
            } }
            snapshotFlow { reached.all { it } }.first { it }
            callback()
            jobs.forEach { it.join() }
        }
    }
    return edges.mapIndexed { i, edge -> if (reached[i]) maxOf(edge.value, 1f) else edge.value }
}
