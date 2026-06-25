import Foundation
import SwiftUI

/// Owns the current report and the live activity state.
/// - Cost numbers come from cc_cost.py (shelled out every `refreshInterval`).
/// - Activity state comes from a cheap native scan of log mtimes (every 2s),
///   re-evaluated each animation frame so transitions show promptly.
@MainActor
final class UsageStore: ObservableObject {
    @Published var report: Report?
    @Published var errorText: String?
    @Published var lastUpdated: Date?
    @Published var isLoading = false

    @Published var activity: ActivityState = .idle
    @Published var tick: Int = 0          // animation frame counter (advances only when not idle)

    private var costTimer: Timer?
    private var scanTimer: Timer?
    private var animTimer: Timer?
    private var newestMtime: Date?

    // Tunables.
    private let refreshInterval: TimeInterval = 30   // cost re-parse
    private let workingWindow: TimeInterval = 6      // "writing right now"
    private let idleWindow: TimeInterval = 600       // 10 min → idle
    private let frame: TimeInterval = 0.2            // animation tick

    /// Compact text shown in the menu bar.
    var menuTitle: String {
        if let r = report { return "$" + String(format: "%.2f", r.thisWeek) }
        return errorText == nil ? "…" : "!"
    }

    init() {
        refresh()
        scanActivity()

        costTimer = Timer.scheduledTimer(withTimeInterval: refreshInterval, repeats: true) { [weak self] _ in
            Task { @MainActor in self?.refresh() }
        }
        scanTimer = Timer.scheduledTimer(withTimeInterval: 2, repeats: true) { [weak self] _ in
            Task { @MainActor in self?.scanActivity() }
        }
        animTimer = Timer.scheduledTimer(withTimeInterval: frame, repeats: true) { [weak self] _ in
            Task { @MainActor in self?.animationFrame() }
        }
    }

    // MARK: cost

    func refresh() {
        guard !isLoading else { return }
        isLoading = true
        Task {
            do {
                let r = try await Task.detached(priority: .utility) { try loadReport() }.value
                self.report = r
                self.errorText = nil
                self.lastUpdated = Date()
            } catch {
                self.errorText = error.localizedDescription
            }
            self.isLoading = false
        }
    }

    // MARK: activity

    private func scanActivity() {
        Task.detached(priority: .utility) { [weak self] in
            let m = newestLogMtime()
            await MainActor.run {
                self?.newestMtime = m
                self?.recomputeActivity()
            }
        }
    }

    private func animationFrame() {
        recomputeActivity()                 // cheap; uses cached mtime + current time
        if activity != .idle { tick &+= 1 } // freeze the counter (and re-renders) when idle
    }

    private func recomputeActivity() {
        let next: ActivityState
        if let m = newestMtime {
            let age = Date().timeIntervalSince(m)
            next = age < workingWindow ? .working : (age < idleWindow ? .waitingForInput : .idle)
        } else {
            next = .idle
        }
        if next != activity { activity = next }
    }
}
