// Adapted from https://github.com/mihonapp/mihon at 4823ba69ca65fa707fb89406f3a4c43c9e0053dd
// Source: presentation-core/src/main/java/tachiyomi/presentation/core/components/CircularProgressIndicator.kt
// Copyright 2015 Javier Tomás; Copyright 2024 Mihon Open Source Project. Apache-2.0.
// Modified for this knowledge base; see the original file for additional attribution.
// Subset: determinate rotation, no AnimatedContent crossfade. Explicit mode and reducedMotion added.
import androidx.compose.animation.core.*
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.rotate

@Composable
fun RotatingProgress(progress: Float, reducedMotion: Boolean) {
    val angle = if (reducedMotion) 0f else {
        val transition = rememberInfiniteTransition(label = "rotation")
        val value by transition.animateFloat(
            initialValue = 0f, targetValue = 360f,
            animationSpec = infiniteRepeatable(tween(2000, easing = LinearEasing), RepeatMode.Restart),
            label = "angle",
        )
        value
    }
    CircularProgressIndicator(progress = { progress.coerceIn(0f, 1f) }, modifier = Modifier.rotate(angle))
}
