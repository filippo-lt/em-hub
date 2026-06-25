import Foundation

/// Resolve the path to cc_cost.py.
/// 1. `CC_COST_SCRIPT` env var wins (handy for testing / non-standard layouts).
/// 2. Otherwise derive it relative to this source file: the script lives at
///    `<token-tracker>/cc_cost.py`, and this file is at
///    `<token-tracker>/app/Sources/CCTokenBar/Runner.swift` — four levels down.
func resolveScriptPath() -> String {
    if let p = ProcessInfo.processInfo.environment["CC_COST_SCRIPT"], !p.isEmpty {
        return p
    }
    var url = URL(fileURLWithPath: #filePath)
    for _ in 0..<4 { url.deleteLastPathComponent() }   // -> <token-tracker>
    return url.appendingPathComponent("cc_cost.py").path
}

enum RunnerError: LocalizedError {
    case scriptMissing(String)
    case nonZeroExit(Int32, String)

    var errorDescription: String? {
        switch self {
        case .scriptMissing(let path):
            return "cc_cost.py not found at:\n\(path)\nSet CC_COST_SCRIPT to override."
        case .nonZeroExit(let code, let err):
            return "cc_cost.py exited \(code):\n\(err)"
        }
    }
}

/// Run `python3 cc_cost.py --json` and decode the result. Pure I/O, no actor
/// state — safe to call from a detached background task.
func loadReport() throws -> Report {
    let path = resolveScriptPath()
    guard FileManager.default.fileExists(atPath: path) else {
        throw RunnerError.scriptMissing(path)
    }

    let proc = Process()
    proc.executableURL = URL(fileURLWithPath: "/usr/bin/env")
    proc.arguments = ["python3", path, "--json"]

    let out = Pipe()
    let err = Pipe()
    proc.standardOutput = out
    proc.standardError = err
    try proc.run()

    let data = out.fileHandleForReading.readDataToEndOfFile()
    let errData = err.fileHandleForReading.readDataToEndOfFile()
    proc.waitUntilExit()

    guard proc.terminationStatus == 0 else {
        let msg = String(data: errData, encoding: .utf8) ?? ""
        throw RunnerError.nonZeroExit(proc.terminationStatus, msg)
    }

    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    return try decoder.decode(Report.self, from: data)
}
