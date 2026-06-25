import SwiftUI
import AppKit

/// The dropdown shown when the menu bar item is clicked.
struct ContentView: View {
    @ObservedObject var store: UsageStore

    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            header

            if let r = store.report {
                rollups(r)
                Divider()
                section("By model", r.byModel.map { ($0.model, $0.cost, "\($0.turns) turns") })
                if !r.byProject.isEmpty {
                    Divider()
                    section("By project", r.byProject.map { (tilde($0.project), $0.cost, "") })
                }
                if r.byWeek.count > 1 {
                    Divider()
                    section("By week", r.byWeek.map { ($0.week, $0.cost, "") })
                }
                if r.byDow.contains(where: { $0.cost > 0 }) {
                    Divider()
                    bars("By day of week", r.byDow.map { ($0.dow, $0.cost) })
                }
            } else if let e = store.errorText {
                Text(e).font(.callout).foregroundColor(.red).fixedSize(horizontal: false, vertical: true)
            } else {
                Text("Loading…").foregroundColor(.secondary)
            }

            Divider()
            footer
        }
        .padding(14)
        .frame(width: 320)
    }

    private var header: some View {
        HStack {
            Image(systemName: "dollarsign.circle.fill")
            Text("Claude Code Usage").font(.headline)
            Spacer()
            HStack(spacing: 5) {
                Circle().fill(store.activity.color).frame(width: 7, height: 7)
                Text(store.activity.label).font(.caption).foregroundColor(.secondary)
            }
        }
    }

    private func rollups(_ r: Report) -> some View {
        VStack(spacing: 4) {
            statRow("Today", r.today)
            statRow("This week", r.thisWeek)
            statRow("This month", r.thisMonth)
            statRow("All time", r.total)
        }
    }

    private func statRow(_ label: String, _ value: Double) -> some View {
        HStack {
            Text(label).foregroundColor(.secondary)
            Spacer()
            Text(money(value)).monospacedDigit().bold()
        }
    }

    private func section(_ title: String, _ rows: [(String, Double, String)]) -> some View {
        VStack(alignment: .leading, spacing: 3) {
            Text(title.uppercased()).font(.caption2).foregroundColor(.secondary)
            ForEach(Array(rows.enumerated()), id: \.offset) { _, row in
                HStack {
                    Text(row.0).lineLimit(1).truncationMode(.middle)
                    Spacer()
                    if !row.2.isEmpty {
                        Text(row.2).font(.caption2).foregroundColor(.secondary)
                    }
                    Text(money(row.1)).monospacedDigit()
                }
            }
        }
    }

    private var footer: some View {
        HStack {
            if let t = store.lastUpdated {
                Text("Updated \(t.formatted(date: .omitted, time: .shortened))")
                    .font(.caption2).foregroundColor(.secondary)
            }
            Spacer()
            Button("Refresh") { store.refresh() }
            Button("Quit") { NSApplication.shared.terminate(nil) }
        }
    }

    private func bars(_ title: String, _ pairs: [(String, Double)]) -> some View {
        let maxVal = max(pairs.map { $0.1 }.max() ?? 0, 0.0001)
        return VStack(alignment: .leading, spacing: 4) {
            Text(title.uppercased()).font(.caption2).foregroundColor(.secondary)
            HStack(alignment: .bottom, spacing: 5) {
                ForEach(Array(pairs.enumerated()), id: \.offset) { _, p in
                    VStack(spacing: 2) {
                        RoundedRectangle(cornerRadius: 2)
                            .fill(Color.accentColor.opacity(0.75))
                            .frame(width: 18, height: CGFloat(p.1 / maxVal) * 38 + 2)
                        Text(p.0).font(.system(size: 9)).foregroundColor(.secondary)
                    }
                }
            }
        }
    }

    private func money(_ x: Double) -> String { "$" + String(format: "%.2f", x) }
    private func tilde(_ p: String) -> String { (p as NSString).abbreviatingWithTildeInPath }
}
