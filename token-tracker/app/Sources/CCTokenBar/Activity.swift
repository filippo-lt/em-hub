import Foundation
import SwiftUI

/// Live state of Claude Code, inferred from how recently any session log was
/// written. This is a heuristic — it can't perfectly tell "awaiting your
/// message" from "awaiting a permission prompt", but it reliably separates
/// actively-writing from finished-recently from long-idle.
enum ActivityState: Sendable {
    case working          // a log was written in the last few seconds
    case waitingForInput  // recent activity, but not actively writing
    case idle             // nothing for a while / no sessions

    var label: String {
        switch self {
        case .working: return "Working"
        case .waitingForInput: return "Waiting for input"
        case .idle: return "Idle"
        }
    }

    var color: Color {
        switch self {
        case .working: return .green
        case .waitingForInput: return .orange
        case .idle: return .secondary
        }
    }
}

/// Newest modification time across all Claude Code session logs. A cheap
/// directory walk (a handful of files) — no parsing, safe to call frequently.
func newestLogMtime() -> Date? {
    let base = ("~/.claude/projects" as NSString).expandingTildeInPath
    let fm = FileManager.default
    guard let en = fm.enumerator(atPath: base) else { return nil }
    var newest: Date?
    for case let rel as String in en where rel.hasSuffix(".jsonl") {
        let full = "\(base)/\(rel)"
        if let m = (try? fm.attributesOfItem(atPath: full))?[.modificationDate] as? Date {
            if newest == nil || m > newest! { newest = m }
        }
    }
    return newest
}
