# reproducible-builds

A single-module Maven project and `verify.sh`, which builds the jar twice and compares SHA-256 hashes.

## Goal

Show that a Maven jar can be byte-for-byte identical across builds by fixing `project.build.outputTimestamp` and pinning plugin versions.

## Run it

```bash
./verify.sh
```

Expected: the script prints `build 1: <hash>`, `build 2: <hash>` and `REPRODUCIBLE`; if the hashes differ it prints `NOT REPRODUCIBLE` and exits 1. It runs `mvn -B -q clean package` twice, two seconds apart. Set `MVN=./mvnw` to use a wrapper. Java 21 and Maven are required.

Not run end to end: `verify.sh` itself was not executed. The same two builds were run by hand earlier and gave the same hash both times, which starts `49f4f7b4` and ends `486c`.

## What it proves

- `pom.xml` sets `project.build.outputTimestamp` to `2024-01-01T00:00:00Z`, so every entry in the jar gets a constant timestamp.
- The compiler and jar plugins are pinned (3.13.0 and 3.4.1), so the build does not drift with Maven defaults.
- Reproducibility is checked with a plain hash comparison of `target/orders-repro-1.0.0.jar`.

## Trade-offs

- It covers one machine and one JDK; a different JDK vendor or version can produce different class files, so a real check must pin the JDK too.
- Removing the timestamp property or the plugin versions should break it, which makes a good experiment.
- Only the jar is compared, not the POM or other published artifacts.

## When not to use it

- When you do not distribute artifacts and nobody needs to verify them.
- For supply-chain verification across machines, compare builds in a pinned container instead of on one host.
