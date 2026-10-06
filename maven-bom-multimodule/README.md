# maven-bom-multimodule

A Maven reactor with a parent POM and three modules: `orders-bom`, `orders-core` and `orders-app`.

## Goal

Show a multi-module Maven build where one BOM pins every dependency version and the modules import it instead of repeating versions.

## Run it

```bash
./mvnw -B verify
```

Expected: a reactor of `orders-bom`, `orders-parent`, `orders-core` and `orders-app`, one passing test (`OrderTest`) and `BUILD SUCCESS`. This was run with a system Maven 3.8.6 as `mvn -B verify` and produced exactly that. Not run end to end: the Maven Wrapper (`mvnw`, pinned to Maven 3.9.9) itself has not been executed. Java 21 is required.

## What it proves

- `orders-core` declares `junit-jupiter` without a `<version>`; the 5.10.2 pin comes from `orders-bom`.
- `orders-app` depends on `orders-core` without a version, which also comes from the BOM, and Maven builds `orders-core` first.
- The parent `pom.xml` pins the compiler, surefire and jar plugin versions in `pluginManagement`.

## Trade-offs

- Each module imports the BOM itself rather than inheriting it, which costs a few lines per module but lets outside projects import the same BOM.
- BOM and parent share version 1.0.0 here; a real setup would release them separately.
- Maven's XML is verbose compared to Gradle's version catalogs.

## When not to use it

- For a single module, a `<dependencyManagement>` block in its own POM is enough.
- If your team already uses Gradle, a version catalog gives the same result.
