# bazel-minimal

A `MODULE.bazel` and a `BUILD.bazel` with one `java_binary` that builds and runs a small Orders `App`.

## Goal

Show the smallest Bazel setup for a Java 21 program: one module file that pins `rules_java` and one build file with a single target.

## Run it

```bash
USE_BAZEL_VERSION=7.4.1 bazelisk run //:app
```

Expected: `total=1000`. With a system `bazel` instead, run `bazel run //:app`. The first run needs network access to fetch `rules_java`.

Not run end to end: Bazel is not installed on the machine where this README was written, so the output above comes from reading `App.java` (2 x 500 cents), not from a real run.

## What it proves

- A Java target is declared in a few lines of `BUILD.bazel`, and its inputs are listed explicitly in `srcs`.
- `rules_java` is pinned to 7.12.2 in `MODULE.bazel`, and the Bazel version is pinned through `USE_BAZEL_VERSION`.
- `src/main/java/lab/orders/App.java` holds its own `Order` record, so the target has no other dependencies.

## Trade-offs

- Builds are hermetic and cacheable, but you must learn Starlark and maintain `BUILD` files by hand or with generators.
- Maven dependencies would need `rules_jvm_external`, which this folder leaves out to stay minimal.
- There is no `.bazelversion` file, so the Bazel version depends on the environment variable.
- IDE support is weaker than for Maven or Gradle.

## When not to use it

- For a single-language, single-team project, Maven or Gradle is cheaper to adopt.
- Bazel pays off for large polyglot monorepos, not for one small service.
