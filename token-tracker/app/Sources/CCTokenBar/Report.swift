import Foundation

/// Decoded from `cc_cost.py --json`. Keys are snake_case in the JSON; the
/// decoder uses `.convertFromSnakeCase`, so properties are camelCase here.
struct Report: Codable, Sendable {
    var total: Double = 0
    var today: Double = 0
    var thisWeek: Double = 0
    var thisMonth: Double = 0
    var turns: Int = 0
    var byModel: [ModelRow] = []
    var byProject: [ProjectRow] = []
    var byWeek: [WeekRow] = []
    var byDay: [DayRow] = []
    var byDow: [DowRow] = []
    var byHour: [HourRow] = []
    var topSessions: [SessionRow] = []
    var tokens: Tokens = .init()

    struct ModelRow: Codable, Sendable, Identifiable {
        var model: String
        var cost: Double
        var turns: Int
        var id: String { model }
    }
    struct ProjectRow: Codable, Sendable, Identifiable {
        var project: String
        var cost: Double
        var id: String { project }
    }
    struct WeekRow: Codable, Sendable, Identifiable {
        var week: String
        var cost: Double
        var id: String { week }
    }
    struct DayRow: Codable, Sendable, Identifiable {
        var day: String
        var cost: Double
        var id: String { day }
    }
    struct DowRow: Codable, Sendable, Identifiable {
        var dow: String
        var cost: Double
        var id: String { dow }
    }
    struct HourRow: Codable, Sendable, Identifiable {
        var hour: Int
        var cost: Double
        var id: Int { hour }
    }
    struct SessionRow: Codable, Sendable, Identifiable {
        var session: String
        var date: String
        var project: String
        var cost: Double
        var id: String { session }
    }
    struct Tokens: Codable, Sendable {
        var input: Int = 0
        var output: Int = 0
        var cacheRead: Int = 0
        var cacheWrite: Int = 0
    }
}
