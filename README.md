# java-build-tooling

Six small builds for Java 21 that show how Gradle, Maven, Bazel and plain scripts handle shared configuration, caching, reproducibility and repository layout, using one tiny Orders domain.

## What is inside

| Folder | What it shows | Run |
| --- | --- | --- |
| [`gradle-convention-plugins`](./gradle-convention-plugins) | One convention plugin in an included build shared by two modules | `./gradlew build :orders-app:run` |
| [`maven-bom-multimodule`](./maven-bom-multimodule) | A Maven BOM that pins versions for a multi-module reactor | `./mvnw -B verify` |
| [`gradle-build-cache`](./gradle-build-cache) | A local Gradle build cache restoring `compileJava` after `build/` is deleted | `./verify.sh` |
| [`bazel-minimal`](./bazel-minimal) | The smallest Bazel `java_binary` with a pinned `rules_java` | `bazelisk run //:app` |
| [`reproducible-builds`](./reproducible-builds) | A Maven jar with an identical SHA-256 across two builds | `./verify.sh` |
| [`monorepo-vs-polyrepo`](./monorepo-vs-polyrepo) | An affected-modules calculator over a four-module layout | `python3 affected.py` |

## Prerequisites

- Java 21
- Maven 3.9+ (or the included wrapper in `maven-bom-multimodule`)
- Gradle 8.10.2 to generate the wrapper in the two Gradle folders
- Bazelisk (optional, only for `bazel-minimal`)
- Python 3 for `monorepo-vs-polyrepo`

## How to read it

Start with `maven-bom-multimodule`, then `gradle-convention-plugins` to compare how each tool shares configuration. The other folders are independent. Each folder README says what was run and what was not.
