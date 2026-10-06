# gradle-convention-plugins

A two-module Gradle build (`orders-core`, `orders-app`) that shares its configuration through a precompiled plugin in `build-logic/`.

## Goal

Share one build setup (Java 21 toolchain, JUnit BOM, test task) across modules with a convention plugin in an included build, instead of copy-pasting it or using `allprojects {}`.

## Run it

```bash
gradle wrapper --gradle-version 8.10.2   # once: generates gradlew, pinned to 8.10.2
./gradlew build :orders-app:run
```

Expected: the `orders-core` test passes and `:orders-app:run` prints `total=1000`.

Not run end to end: Gradle is not installed on the machine where this README was written, so this build has never been executed. No wrapper files are committed. The first run also needs network access for Maven Central.

## What it proves

- `build-logic/src/main/kotlin/orders.java-conventions.gradle.kts` defines the plugin `orders.java-conventions`, and `settings.gradle.kts` includes it with `includeBuild("build-logic")`.
- `orders-core/build.gradle.kts` is one line (applying the plugin); `orders-app/build.gradle.kts` adds `application` and a project dependency.
- Changing the toolchain version in the convention changes both modules at once; JUnit is pinned to 5.10.2.

## Trade-offs

- Convention plugins need the `kotlin-dsl` plugin and an extra build, which slows the first configuration.
- An included build is easier to test and share than `buildSrc`, which invalidates the whole build on any change.
- JUnit comes from Maven Central, so the first run needs network access.

## When not to use it

- For a single-module project or a throwaway script, a plain `build.gradle.kts` is simpler.
- When only one setting differs between modules, a small shared script may be enough.
