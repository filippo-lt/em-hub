# Developer metrics — merged Jira + GitHub — 2026-04

**Generated:** 2026-04-27  
**Sources:** `make dev-metrics-month MONTH=2026-04` and `make github-metrics-month MONTH=2026-04` (`/Users/ftosetto/Projects/metrics`).  
**Jira:** delivered items in month; NO QA = items flagged; bounces = changelog count.  
**GitHub:** commits, PRs, composite score (script output).

---

## Merged table (one row per person)

| Developer | Jira stories | Jira bugs | Jira total | SP | NO QA (bounces) | GH commits | GH PRs | GH score |
|-----------|-------------:|----------:|-----------:|---:|----------------:|-----------:|-------:|---------:|
| Andrew Laminski | 3 | 0 | 3 | 5.0 | 0 (0) | 21 | 5 | 10 |
| Anton Shkuray | 7 | 4 | 11 | 30.0 | 12 (13) | 91 | 19 | 62 |
| Artem Shyianov | 14 | 2 | 16 | 44.0 | 3 (3) | 23 | 12 | 32 |
| Dmytro Tkachenko | 11 | 2 | 13 | 29.0 | 0 (0) | 79 | 8 | 47 |
| Edward Liu | 6 | 18 | 24 | 87.0 | 3 (3) | 104 | 34 | 83 |
| Oleksii Lebediev | 5 | 8 | 13 | 44.0 | 2 (3) | 31 | 18 | 47 |
| Serhii Kostrykin | 5 | 1 | 6 | 20.0 | 0 (0) | 77 | 10 | 53 |
| Shu Zhang | 7 | 1 | 8 | 67.0 | 1 (1) | 50 | 3 | 24 |
| Viacheslav Lypchenko | 11 | 11 | 22 | 62.0 | 1 (1) | 34 | 14 | 43 |
| Volodymyr Marienkov | 6 | 9 | 15 | 47.0 | 2 (3) | 53 | 24 | 66 |
| Xiaochun Mou | 3 | 18 | 21 | 68.0 | 2 (2) | 197 | 97 | 93 |
| Andrei Marinov | — | — | — | — | — | 21 | 7 | 12 |
| Vladyslav Krut | — | — | — | — | — | 97 | 15 | 70 |

**Jira month totals:** 78 stories, 74 bugs, 152 items, 503 SP, 26 NO QA (29 bounces).  
**GitHub month totals:** 878 commits, 266 PRs (aggregate line stats in raw script output).

---

## Analysis

- **Strong on both signals:** Xiaochun Mou and Edward Liu lead on GitHub score and sit at the top on Jira SP (68 / 87). High bug volume on Jira for both; worth confirming that matches expectations (stability work vs scope creep).
- **Jira-heavy, GitHub quieter:** Shu Zhang (67 SP, GH score 24) — delivery shows in Jira; GitHub activity is more commits, fewer PRs. Andrew Laminski is light on both SP (5) and GH score (10); confirm allocation and whether work is outside tracked repos.
- **GitHub-strong, not on Jira rollup:** Vladyslav Krut (score 70) and Andrei Marinov (score 12) do not appear in the April Jira dev-metrics table — likely different projects, config roster, or work not counted as Story/Bug in that export. Align configs if they should be on the same view.
- **Quality flag:** Anton Shkuray is the standout on **NO QA / bounces** (12 / 13) while still mid-high on GitHub (62). That deserves a focused conversation (definition of done, QA handoff, ticket granularity), not just a metrics pass.
- **Line churn (GitHub):** Vladyslav Krut and Serhii Kostrykin show very large deleted-line totals in the raw GitHub run — often bulk deletes, generated files, or vendor drops. Do not read that as “more engineering” without context.

---

## Raw reference (same run as merge)

<details>
<summary>Jira summary (2026-04)</summary>

```
Developer                      Projects             Stories    Bugs     Total    SP       NO QA (bounces)   
Andrew Laminski                FAIOSMAU, ADIOSMAU   3          0        3        5.0      0 (0)             
Anton Shkuray                  FAIOSMAU             7          4        11       30.0     12 (13)           
Artem Shyianov                 IMIOSMAU, IMOEXT     14         2        16       44.0     3 (3)             
Dmytro Tkachenko               ADIOSMAU             11         2        13       29.0     0 (0)             
Edward Liu                     TTIOSMAU             6          18       24       87.0     3 (3)             
Oleksii Lebediev               ADIOSMAU             5          8        13       44.0     2 (3)             
Serhii Kostrykin               SMIOSMAU, IMIOSMAU   5          1        6        20.0     0 (0)             
Shu Zhang                      TTIOSMAU             7          1        8        67.0     1 (1)             
Viacheslav Lypchenko           IMANDMAU             11         11       22       62.0     1 (1)             
Volodymyr Marienkov            ADIOSMAU             6          9        15       47.0     2 (3)             
Xiaochun Mou                   TTIOSMAU             3          18       21       68.0     2 (2)             
TOTAL                                               78         74       152      503.0    26 (29)           
```

</details>

<details>
<summary>GitHub summary (2026-04)</summary>

```
Developer                      Commits    PRs      Score 
Xiaochun Mou                   197        97       93    
Edward Liu                     104        34       83    
Vladyslav Krut                 97         15       70    
Volodymyr Marienkov            53         24       66    
Anton Shkuray                  91         19       62    
Serhii Kostrykin               77         10       53    
Dmytro Tkachenko               79         8        47    
Oleksii Lebediev               31         18       47    
Viacheslav Lypchenko           34         14       43    
Artem Shyianov                 23         12       32    
Shu Zhang                      50         3        24    
Andrei Marinov                 21         7        12    
Andrew Laminski                21         5        10    
TOTAL                          878        266      
```

</details>
