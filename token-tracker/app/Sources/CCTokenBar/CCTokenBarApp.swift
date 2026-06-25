import SwiftUI
import AppKit

@main
struct CCTokenBarApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate
    @StateObject private var store = UsageStore()

    var body: some Scene {
        MenuBarExtra {
            ContentView(store: store)
        } label: {
            // Image + Text in the menu bar; title updates as the store refreshes.
            Image(systemName: "dollarsign.circle")
            Text(store.menuTitle)
        }
        .menuBarExtraStyle(.window)
    }
}

/// Hide the Dock icon so this behaves as a pure menu bar accessory.
final class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) {
        NSApp.setActivationPolicy(.accessory)
    }
}
