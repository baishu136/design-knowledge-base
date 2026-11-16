// Adapted from https://github.com/mihonapp/mihon at 4823ba69ca65fa707fb89406f3a4c43c9e0053dd
// Source: app/src/main/java/eu/kanade/presentation/reader/appbars/ReaderAppBars.kt
// Copyright 2015 Javier Tomás; Copyright 2024 Mihon Open Source Project. Apache-2.0.
// Modified for this knowledge base; see the original file for additional attribution.
// Subset: top bar only. Reduced motion is an adaptation; not present locally in the original.
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.core.tween
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInVertically
import androidx.compose.animation.slideOutVertically
import androidx.compose.runtime.Composable

@Composable
fun ReaderBarMotion(visible: Boolean, reducedMotion: Boolean, content: @Composable () -> Unit) {
    val slideMs = if (reducedMotion) 0 else 200
    val fadeMs = if (reducedMotion) 0 else 150
    AnimatedVisibility(
        visible = visible,
        enter = slideInVertically(tween(slideMs)) { -it } + fadeIn(tween(fadeMs)),
        exit = slideOutVertically(tween(slideMs)) { -it } + fadeOut(tween(fadeMs)),
    ) { content() }
}
