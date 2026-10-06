plugins {
    id("orders.java-conventions")
    application
}

dependencies {
    implementation(project(":orders-core"))
}

application {
    mainClass = "lab.orders.App"
}
