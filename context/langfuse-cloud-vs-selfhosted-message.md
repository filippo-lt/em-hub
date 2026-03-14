# Message: Langfuse — Cloud vs Self-Hosted

**Audience:** AI Lab and Product Leaders  
**Purpose:** Share the recommendation and rationale for Langfuse deployment (Cloud vs self-hosted).

---

## Short version (e.g. Slack / brief email)

**Langfuse deployment choice: we recommend self-hosting Langfuse** as a shared internal platform rather than using Langfuse Cloud.

**Why:** Multiple apps (including Face AI) will use it, we have a dedicated DevOps team, and we want observability and evaluation data in-house. Self-hosting gives us one centralized instance for tracing, prompt management, and evaluation across apps, with full control over data and retention. Langfuse Cloud is a good fit for small teams or quick experiments; for production use across several services, self-hosting aligns better with our data governance and reuse of existing infra.

**Next steps:** Align with DevOps on deployment (Kubernetes + PostgreSQL, ClickHouse, Redis, object storage), define retention and resource sizing once we have trace-volume estimates, and ensure our backends always fall back to existing prompt sources when Langfuse is unavailable.

---

## Medium version (e.g. email with a bit more context)

**Subject:** Langfuse for LLM observability — recommendation: self-hosted

Hi,

Following our evaluation of Langfuse for LLM observability, prompt management, and evaluation (see the [Langfuse integration doc](context/langfuse-integration.md)), here is the recommendation on **Langfuse Cloud vs self-hosted**.

**Recommendation: self-host Langfuse** as a centralized platform used by Face AI and other content-generating applications.

**Rationale:**

| | Langfuse Cloud | Self-hosted (recommended) |
|---|----------------|---------------------------|
| **Best for** | Small teams, quick start, minimal ops | Multiple applications, centralized platform, data in-house |
| **Data** | Data in Langfuse’s infrastructure | Data stays in our infrastructure; we control retention and governance |
| **Ops** | Fully managed | We run it (PostgreSQL, ClickHouse, Redis, object storage, Langfuse web/workers); DevOps can own deployment and maintenance |
| **Scale** | Usage-based pricing | We size and scale to our workload and retention |

Given that (1) several applications will use Langfuse, (2) we have a dedicated DevOps team, and (3) we want centralized observability and evaluation with data in-house, **self-hosting is the better long-term fit**. Langfuse Cloud remains an option for early prototyping or isolated experiments; for production across multiple services, we recommend the self-hosted path.

**Important:** Our backends must keep working if Langfuse is down. Tracing and prompt fetching will be best-effort, with fallback to existing prompt sources (e.g. Firestore) so that request handling never depends on Langfuse availability.

**Next steps:**

- Align with DevOps on deployment (e.g. Kubernetes/Helm on existing GCP, plus PostgreSQL, ClickHouse, Redis, S3-compatible storage).
- Define retention and resource sizing once we have trace-volume estimates.
- Proceed with integration work (tracing, prompt source abstraction, evaluation workflows) as per the integration doc.

Happy to discuss or walk through the full doc if helpful.

---

## One-line summary (for decks or bullet lists)

**Langfuse:** Recommend self-hosted as a shared platform for multiple apps; Cloud is an option for prototyping only; backends must fall back when Langfuse is unavailable.
