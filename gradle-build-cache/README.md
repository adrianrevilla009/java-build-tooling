# gradle-build-cache

A Gradle project with a project-local build cache and `verify.sh`, which checks that `compileJava` is restored from the cache.

## Goal

Show that the Gradle build cache works: after deleting `build/`, the same inputs restore the `compileJava` output instead of recompiling.

## Run it

```bash
gradle wrapper --gradle-version 8.10.2   # once: generates gradlew, pinned to 8.10.2
./verify.sh
```

Expected: the script prints `CACHE HIT: :compileJava FROM-CACHE` and exits 0, or prints `CACHE MISS` and exits 1. Set `GRADLE=gradle` to use a system Gradle instead of the wrapper.

Not run end to end: Gradle is not installed on the machine where this README was written, so `verify.sh` has never been executed. No wrapper files are committed.

## What it proves

- `verify.sh` builds with `--build-cache`, deletes `build/`, builds again and greps the output for `:compileJava FROM-CACHE`.
- `settings.gradle.kts` points the cache at `.build-cache/` inside the project, so you can open the cached entries.
- `build.gradle.kts` pins the Java 21 toolchain, so the toolchain is part of the cache key.

## Trade-offs

- A local cache helps one machine only; teams need a remote cache to share hits.
- Tasks with undeclared inputs cause misses or wrong hits.
- `--no-daemon` makes the script slower but keeps it free of state.

## When not to use it

- For builds that compile in a few seconds, the cache adds more work than it saves.
- When the CI workspace is thrown away and no remote cache is available, a local cache never gets a hit.
