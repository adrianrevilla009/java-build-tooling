rootProject.name = "orders-cache"

buildCache {
    local {
        // Project-local cache so the demo does not touch ~/.gradle.
        directory = file(".build-cache")
    }
}
