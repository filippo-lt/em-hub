# Dev Metrics — 2026-06

_Source: Jira (leadtech.atlassian.net) · generated 2026-07-01_  _GitHub metrics not included — connector not available in this environment._

Reporting period: 2026-06-01 → 2026-06-30. Scope: TTIOSMAU (Tattooist), FAIOSMAU (Face AI), SMIOSMAU (Screen Mirroring). "Delivered" = transitioned into Closed / Resolved / Waiting for Deployment / PO REVIEW-APPROVAL / Complete dev during the month. "QA bounceback" = transitioned into No QA Pass / No-QAPass / No Pass during the month (one count per issue, by assignee).

## Configured developers

| Developer | Project | Items delivered | Story points | QA bouncebacks |
| --- | --- | ---: | ---: | ---: |
| Edward Liu | TTIOSMAU | 42 | n/a | 3 |
| Shu Zhang | TTIOSMAU | 8 | n/a | 2 |
| Xiaochun Mou | TTIOSMAU | 49 | n/a | 2 |
| Anton Shkuray | FAIOSMAU | 0 | n/a | 0 |
| Andrew Laminski | FAIOSMAU | 3 | n/a | 0 |
| Serhii Kostrykin | SMIOSMAU | 3 | n/a | 0 |

Story points show `n/a`: the Jira connector in this environment returns a fixed field projection and does not expose `customfield_10016`, so points could not be read for any issue (see Notes).

## Summary

- **Top contributors (by items delivered, configured devs):** Xiaochun Mou (49) and Edward Liu (42) dominate; together they account for ~87% of the configured-dev output. Story-point ranking is unavailable this month.
- **Low / zero activity:** Anton Shkuray delivered 0 (no matching Jira account found — likely deactivated or renamed). Andrew Laminski (3) and Serhii Kostrykin (3) were low; Shu Zhang at 8 is well below the two TTIOSMAU leads.
- **QA bouncebacks:** 10 across the whole scope; 7 fall on configured devs, concentrated on **Edward Liu (3)**, with Xiaochun Mou (2) and Shu Zhang (2). The remaining 3 are non-configured: Andrey Marinov (2) and 1 unassigned ticket (TTIOSMAU-2111).
- **Config drift (delivered work by people not in the config):** 102 of 207 delivered items (~49%) were shipped by contributors not in the dev-metrics config — led by **Andrey Marinov (37, SMIOSMAU)**, Serena Deng (13), Vladyslav Krut (13), Oscar Blanco Vallejo (9), Ruben Gomez Navarro (8), Miguel Fernandez Gonzalez (6), Oleksii Andrieiev (5), Oleksii Lavrukhin (3), Demetrio Lledo Garcia (3), Maria Rodriguez D'Albano (2), Erica Piña Marin (2), Victor Jalencas Lobera (1). The config likely needs updating.
- **Status names:** all three bounceback status names ("No QA Pass", "No-QAPass", "No Pass") were accepted by JQL without error, so none had to be dropped. All five delivered-status names were valid.

## Other assignees (config drift) — delivered

| Assignee | Items delivered |
| --- | ---: |
| Andrey Marinov | 37 |
| Serena Deng | 13 |
| Vladyslav Krut | 13 |
| Oscar Blanco Vallejo | 9 |
| Ruben Gomez Navarro | 8 |
| Miguel Fernandez Gonzalez | 6 |
| Oleksii Andrieiev | 5 |
| Oleksii Lavrukhin | 3 |
| Demetrio Lledo Garcia | 3 |
| Maria Rodriguez D'Albano | 2 |
| Erica Piña Marin | 2 |
| Victor Jalencas Lobera | 1 |

Total delivered across scope: **207** (configured devs 105 + other assignees 102). Total QA bouncebacks across scope: **10**.

## Notes / limitations (autonomous run)

- **Story points unavailable.** Both `searchJiraIssuesUsingJql` and `getJiraIssue` in this environment ignore the `fields` parameter and return a fixed projection that excludes `customfield_10016`. Points could not be retrieved for any issue and are reported as `n/a` rather than 0 (reporting 0 would misleadingly imply zero-point work). If point tracking is required, a connector that honours field selection is needed.
- **Unresolved developers.** User lookup returned no account for "Anton Shkuray" or "Serhii Kostrykin". Anton has 0 delivered items and 0 bouncebacks. Serhii, despite the failed lookup, does appear as an assignee on 3 delivered SMIOSMAU items (counted by display name).
- **Method.** Delivered items were enumerated by paging the full result set (207 issues over 3 pages) and aggregating assignee display names; QA bouncebacks (10 issues) were aggregated the same way. Counts are exact for the queried statuses and date range.
- **GitHub metrics** are not included — no GitHub connector in this environment.
