import Foundation
import SwiftUI

/// Owns the current report and refreshes it on a timer by shelling out to
/// cc_cost.py. Main-actor isolated; the subprocess runs on a detached task.
@MainActor
final class UsageStore: ObservableObject {
    @Published var report: Report?
    @Published var errorText: String?
    @Published var lastUpdated: Date?
    @Published var isLoading = false

    private var timer: Timer?
    private let refreshInterval: TimeInterval = 30

    /// Compact text shown in the menu bar itself.
    var menuTitle: String {
        if let r = report {
            return "$" + String(format: "%.2f", r.thisWeek)
        }
        return errorText == nil ? "…" : "!"
    }

    init() {
        refresh()
        timer = Timer.scheduledTimer(withTimeInterval: refreshInterval, repeats: true) { [weak self] _ in
            Task { @MainActor in self?.refresh() }
        }
    }

    func refresh() {
        guard !isLoading else { return }
        isLoading = true
        Task {
            do {
                let r = try await Task.detached(priority: .utility) {
                    try loadReport()
                }.value
                self.report = r
                self.errorText = nil
                self.lastUpdated = Date()
            } catch {
                self.errorText = error.localizedDescription
            }
            self.isLoading = false
        }
    }
}
