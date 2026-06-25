// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "CCTokenBar",
    platforms: [.macOS(.v13)],            // MenuBarExtra requires macOS 13+
    targets: [
        .executableTarget(
            name: "CCTokenBar",
            path: "Sources/CCTokenBar"
        )
    ]
)
