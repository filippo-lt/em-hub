# Source data

## ADIOSMAU_tests_combined_2026-05-04.json

Xray test export from the ADIOSMAU Jira project.

### Filters applied at export

- Component: `iOS_AID`
- Plus 18 `[Exterior]` tests without component (manually included)

### Stats

- 354 total tests
- All `testType.kind = "Steps"`, `testType.name = "Manual"`
- All `isCucumber = false` (this pipeline is what changes that)
- Average ~3.8 steps per test

### Distribution by feature prefix

| Prefix              | Count |
| ------------------- | ----- |
| `[Results]`         | 24    |
| `[Exterior]`        | 20    |
| `[Settings]` / `Settings` | 28 |
| `[Garden]` / `Garden -` / `[Garden design]` | 21 |
| `[Paywall]`         | 17    |
| `[Interior]`        | 15    |
| `[Paint]`           | 13    |
| `Discover`          | 10    |
| `[Debug]` / `Debug` | 10    |
| `[Style]`           | 9     |
| `[Superwall]`       | 7     |
| `[Credits]`         | 6     |
| `[Onboarding]`      | 6     |
| `[Payment]`         | 5     |
| `[Color]`           | 4     |
| `[Force Update]` / `Force Update` | 8 |
| `[Projects]`        | 4     |
| `[iOS Permissions]` | 2     |
| `[Replace]`         | 2     |
| no clean prefix     | 141   |

### Note on the unprefixed 141

These need classification before phase 1 can be run on them. Cheapest
approach: have the `/spec-from-tests` skill (or a classifier prompt)
read the unprefixed summaries and propose feature buckets.

### Refreshing this export

When the QA team updates tests in Xray, re-export and replace this file.
The export query / API call should be documented in the iOS repo's
README under "QA tooling" — it's not specific to this pipeline.
