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
            // Menu bar label re-renders whenever `store` publishes (tick / state),
            // which drives the animation. Text/symbol swaps render reliably here.
            glyph
            Text(store.menuTitle)
        }
        .menuBarExtraStyle(.window)
    }

    @ViewBuilder
    private var glyph: some View {
        switch store.activity {
        case .working:
            Text(spinnerFrame)               // braille spinner
        case .waitingForInput:
            Text(store.tick / 4 % 2 == 0 ? "●" : "○")   // slow blink (~0.8s)
        case .idle:
            Image(systemName: "dollarsign.circle")
        }
    }

    private var spinnerFrame: String {
        let frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        return frames[store.tick % frames.count]
    }
}

/// Hide the Dock icon so this behaves as a pure menu bar accessory.
final class AppDelegate: NSObject, NSApplicationDelegate {
    func applicationDidFinishLaunching(_ notification: Notification) {
        NSApp.setActivationPolicy(.accessory)
    }
}
