# Langfuse Integration for Face AI Backend

This document describes Langfuse in the context of the Face AI backend: what it is, how the backend uses LLMs today, and how Langfuse can improve traceability, prompt management, and evaluation.

---

## 1. Introduction to Langfuse

**Langfuse** is an open-source LLM engineering platform for observability, prompt management, and evaluation of LLM applications. It is self-hostable and extensible.

Main capabilities:

- **Observability and tracing** — Capture traces of LLM and non-LLM steps (API calls, retrieval, etc.) with latency, token usage, and cost. Supports sessions and user attribution. Built on OpenTelemetry for compatibility.
- **Prompt management** — Version prompts, deploy by environment/labels, run experiments (e.g. A/B tests), and link prompt versions to traces.
- **Evaluation** — Score and evaluate outputs via LLM-as-judge, user feedback, manual labeling, or custom logic. Use datasets for offline evaluation and production traces for online monitoring.

The platform is designed for technical teams that need to debug, analyze, and iterate on LLM behaviour, cost, and quality without changing application code for every experiment.

---

## 2. Introduction to Face AI: How It Uses the LLM

### 2.1 Scope of LLM Usage

Face AI uses **Gemini** as the only LLM provider today. It is used for **content generation (image)**. Other features (e.g. AI Lab, YouCam) rely on external service APIs and are out of scope for this document. The following sections refer to “LLM” in a generic way so the approach can apply to other providers later.

### 2.2 Architecture

- **Gemini service** — All Gemini calls go through a single `GeminiService` in the backend. It handles image (and text) generation and optional structured output.
- **Filter processors** — Filters are implemented as processors that conform to a common `FilterProcessor` abstraction. Each processor has its own implementation and configuration and may use the LLM (Gemini) or other AI services to produce results. The architecture is extensible; today only Gemini is used for LLM-based filters.
- **Prompts** — Prompts are stored in **Firestore** and can be updated at runtime without redeploying the backend. The Firestore-based configuration source loads filter configs (including prompts) and supports refresh loops and live updates. Processors receive prompt text (or prompt maps keyed by variant) from this configuration.
- **Request handling** — Each request to the backend is traced and logged, including execution time. LLM calls themselves are not yet traced in a unified way that exposes prompt, model, cost, or output for analysis.

### 2.3 Current Gaps

The current setup works for production but has limitations for improving quality, cost, and safety.

**1. Lack of LLM observability**

Each LLM call is largely opaque to development and product:

- **Cost** — No per-request or per-user view of token usage and cost.
- **Inputs and outputs** — No central view of which prompt was used, what input (e.g. image, params) was sent, or what was generated.
- **Quality and edge cases** — Hard to see when the model degrades (e.g. by filter type, input type, or user segment) or to systematically improve the product.

Improving this would allow:

- Automatic evaluation of production workload (e.g. success rate, latency, cost).
- Building datasets and refining prompts (with care for compliance; initially using offline, self-prepared datasets is recommended).
- Cost visibility and budget optimisation.

**2. Limited prompt lifecycle**

Prompts are dynamic (Firestore) but there is no:

- **Versioning** — No history, rollback, or promotion of prompt versions.
- **Environments** — No clear split between production and development prompt sets.
- **Experimentation** — No built-in A/B testing or controlled rollout of prompt changes.

Versioning is a prerequisite for safe rollbacks, promotions, and experiments.

**3. No evaluation or scoring**

There is no dedicated way to:

- Evaluate observed LLM responses (automatically, by experts, or via user feedback).
- Attach scores to traces or filter runs.
- Use scores to drive improvements (e.g. prompt selection, model choice, or product rules).

A dedicated evaluation and scoring layer would close this gap.

The following sections (Traceability and Observability, Prompt Management, Evaluation and Scoring, and Langfuse Deployment Strategy) outline how Langfuse can address these points in the Face AI backend context.

---

## 3. Traceability and Observability for Face AI

Langfuse provides rich traceability and observability (see [Observability overview](https://langfuse.com/docs/observability/overview)). Its model is request-centric:

- **Observation** — A single flow event (e.g. one LLM call, tool call, or RAG step). Each observation has a type (span, generation, event, etc.), timing, and optional input/output.
- **Trace** — The full flow of one user request; a trace is a sequence of observations.
- **Session** — A sequence of user requests (traces) that belong together (e.g. one editing session in the app).

This maps cleanly to Face AI: one trace = one filter application; the session = the user’s editing session; observations = the filter “process” span and the underlying LLM (Gemini) generation. Each filter request that uses the LLM service (Gemini) performs **at most one LLM request** per invocation. The current implementation also has a **fallback**: when image generation fails, a stronger model can be used for retry.

### 3.1 Integration Approach: Observer Wrapper

Langfuse supports three ways to create observations ([Instrumentation](https://langfuse.com/docs/observability/sdk/instrumentation)): manual observations, context manager, and **observe wrapper**. For Face AI, the **observe wrapper** is the recommended option: it is the least intrusive and fits the current architecture.

- Apply the `@observe` decorator to the `process` method of filter processors that use the LLM. The decorator creates a span for each filter run and captures inputs, outputs, timing, and errors without changing the method’s internal logic.
- With the Python SDK’s default setup, supported LLM clients (including [Google GenAI](https://langfuse.com/integrations/model-providers/google-gemini)) are auto-instrumented, so the Gemini call inside the processor appears as a child **generation** observation under the processor span. No extra code is required inside `GeminiService` for basic tracing.

If the observer pattern later proves insufficient (e.g. for more complex flows or custom spans), the same trace model supports context managers or manual observations; the approach can be adjusted without changing the overall trace/session design.

**Example: decorating a Gemini-based processor**

Current pattern in a processor that uses Gemini (e.g. `GeminiBeardFilterProcessor`):

```python
# core/src/modules/filters/processors/beard/gemini_beard.py (conceptual integration)

from langfuse import observe
from core.src.modules.gemini.gemini_service import GeminiService, BytesImage
# ... other imports

class GeminiBeardFilterProcessor(BeardFilterProcessor):
    def __init__(self, gemini_service: GeminiService, config: BeardFilterConfiguration):
        super().__init__(config)
        self.gemini_service = gemini_service

    @observe(name="beard-filter", as_type="span")
    async def process(self, request: BeardFilterRequest) -> BeardFilterResponse:
        # ... existing logic: get prompt, image_data, call gemini_service.generate(), return response
        # No change to business logic; @observe records the span and nests the LLM generation underneath
```

The same pattern applies to other LLM-based processors (e.g. `GeminiGlassesFilterProcessor`, `GeminiSmileFilterProcessor`). Trace hierarchy becomes: **filter process span** → **Gemini generation** (if auto-instrumented).

To attach request context (user, session, filter type, etc.) to the trace, the root trace should be created at the HTTP layer (e.g. in the route or middleware that calls `filtersManager.process()`), and the processor should run inside that trace. For example, the route can start a root observation and set trace-level attributes (see below); the processor’s `@observe` then creates a child span of that trace.

### 3.2 Face AI Use of Langfuse Features

#### Sessions

Sessions group multiple traces (requests) from the same user flow. In Face AI, that corresponds to related filter applications (e.g. “add moustache” then “add van dyke beard”) and helps analyse patterns (which filters are combined, in what order). Not all filters use the LLM, so session-level analytics will mix LLM and non-LLM requests; the benefit is still useful for product and usage analysis.

**Implementation:** The mobile client generates a session identifier and sends it in a request header (e.g. `X-Session-Id`). The backend reads this header when handling the request and passes it to Langfuse as `session_id` on the trace (e.g. when starting the root observation in the route or via `propagate_attributes`).

#### User tracking (`user_id`)

Associating traces with a user enables per-user cost, usage, and quality analysis. Face AI already resolves the user from the auth token (RevenueCat-style anonymous id in the JWT payload). That same identifier should be sent to Langfuse as `user_id` on the trace.

**Implementation:** From `request.active_user_data.user_payload.user_id` (or the decoded JWT used for quota/auth). Set it on the trace when creating the root observation or via `propagate_attributes(user_id=..., session_id=...)` so all observations in the request inherit it.

#### Trace ID and feedback linking

The **mobile app** generates a **unique request id** per request and sends it (e.g. in a header such as `X-Request-Id`). This id is **proposed to be used as the Langfuse trace id** when creating the root observation. The same id can be returned in the response (or the client retains it), so when the user submits feedback (e.g. rating), the client sends the request id back to the backend. The backend can then attach the score to the corresponding trace in Langfuse via the trace id. This keeps feedback tightly coupled to the correct trace without introducing a separate id scheme.

#### Tags

Tags are useful for filtering and grouping traces in the Langfuse UI. For Face AI, **filter type** is a natural tag: e.g. `editor_screen_face_filters_beards`, `editor_screen_face_filters_glasses`. That allows quick filters like “all beard traces” or “all glasses traces” for debugging and cost analysis.

**Implementation:** When starting the root observation for the request, set `tags=[request.filter_type]` (or the concrete filter type used for that route). The `FilterRequest` base class exposes `filter_type` (e.g. `BeardFilterType`, `GlassesFilterType` in the codebase).

#### Metadata

The proposed data model from the AI Lab (e.g. provider, model, latency, success) fits our use case. We extend it with **filter-specific context** that is useful for debugging and evaluation: **filter type**, **requested filter options** (e.g. mode, variant), and the existing examples below. Metadata can carry these parameters without putting them in the main input/output. Examples: for beard — `mode` (e.g. `full_beard`); for lip color — `color_name`, `level`; for smile — `smile_type`; for size — `size_type`.

**Implementation:** When creating the root observation (or updating the current trace), set `metadata` from the request object, e.g. `metadata={"filter_type": request.filter_type, "mode": getattr(request, "mode", None), ...}`. Prefer non-PII, non-sensitive keys; avoid raw images or large payloads in metadata.

#### Multi-modality (images)

Face AI is **image-in, image-out**. In our case the **input** is not only the prompt but also **images** (e.g. the user’s photo). The proposed input/output model (prompt, image_url, metadata) fits; we extend it with **image input (base64)** so both request and response images are visible in the dashboard. Langfuse supports multi-modal content: it works with **base64 and URLs**, extracts base64 data URIs from payloads, uploads media to **object storage (S3-compatible)**, and links it to the trace. Supported image formats are **PNG, JPEG, WebP** ([Multi-Modality and Attachments](https://langfuse.com/docs/observability/features/multi-modality))—which fits our needs. The generated image can be attached to the generation observation for evaluation (e.g. human or model-as-judge scoring). On **Langfuse Cloud**, multi-modal attachments are currently free; pricing for additional storage/compute may change in the future ([Langfuse Cloud multi-modality](https://langfuse.com/docs/observability/features/multi-modality#langfuse-cloud)).

**Implementation:** Use the Langfuse SDK’s support for attaching media (e.g. image URL or base64 inline) to the generation observation corresponding to the Gemini call, so that the UI shows both input and output images for each trace.

#### Cost tracking

Langfuse infers token usage and cost when the LLM provider is instrumented (e.g. Gemini). No extra application code is required for basic cost per observation. Face AI can use this for: cost per request, per user, per filter type (via tags), and for payment or efficiency analysis.

#### Flushing and latency

For our use case, **trace flushing can be done in the background**: the Face AI backend runs for a long time (e.g. long-lived workers or request handlers), so the Langfuse SDK can submit traces asynchronously without blocking the response. This keeps request latency unaffected while still capturing full trace data.

#### Sampling

Initially, capturing **all** traces is recommended so you can validate behaviour and build dashboards. As the user base grows, trace volume may become too high; then enable **sampling** (e.g. sample a percentage of traces or sample by filter type / user segment) to control volume while keeping representative data. Langfuse supports sampling configuration; the exact policy can be decided later (e.g. in SDK config or at the gateway).

---

## 4. Prompt Management for Face AI

Langfuse provides [prompt management](https://langfuse.com/docs/prompt-management/overview): prompts are created, versioned, and deployed from the Langfuse UI or API, and fetched at runtime by name and optionally by version or label (e.g. `production`). Face AI can adopt this while keeping the existing filter configuration abstraction: the **source** of prompt content is swapped to Langfuse; the rest of the pipeline (provider, processors, driver configs) stays the same.

### 4.1 Keeping the Abstraction, Swapping the Prompt Data Source

Face AI already has a filter configuration layer:

- `**FiltersConfigurationSource`** — Abstract interface that returns a `FilterConfiguration` for a given config class (e.g. `BeardFilterConfiguration`).
- `**FiltersConfigurationProvider**` — Consults an ordered list of sources via `get_configuration(config_class)` and returns the first non-`None` result.
- **Concrete sources** — Today: `FirestoreFilterConfigurationSource` (prompts from Firestore) and `StandardFilterConfigurationSource` (fallback defaults). Each builds configs whose driver configs hold a **prompts dict** (e.g. `GeminiBeardFilterDriverConfiguration(prompts=...)`).

To use Langfuse as the prompt store **without replacing the Firestore source**, introduce a **`PromptSource`** interface (e.g. `get_prompt(key) -> str`) and have the driver config accept **only** a `PromptSource`. Any dictionary (e.g. the one read from Firestore today) is wrapped in a small adapter that implements `PromptSource`; the Langfuse-backed implementation is another such adapter. This wrapper is **injected into the Firestore source** (or the factory that builds it). When building Gemini driver configs, the Firestore source always passes a `PromptSource`—either the injected Langfuse one or a dict-backed adapter over the Firestore prompts. The driver config has a single, consistent abstraction; the rest of the pipeline (provider, processors) stays unchanged.

**Migration plan:** Prepare all prompts in Langfuse first, then deploy backend changes with **fallback to the dict from Firestore**. At runtime the backend tries to get the prompt from Langfuse; if that fails (e.g. Langfuse unavailable or prompt missing), it falls back to the Firestore-backed dict. This keeps the app working when Langfuse is down and allows a gradual cutover.

**Example: PromptSource interface, dict adapter, Langfuse adapter, and driver config**

1. **PromptSource interface and implementations** — One protocol; both Langfuse and a plain dict are exposed as `PromptSource`:

```python
# Conceptual: PromptSource protocol and two implementations

from langfuse import get_client
from typing import Protocol

class PromptSource(Protocol):
    def get_prompt(self, key: str) -> str: ...

class DictPromptSource:
    """Wraps a prompts dict so it satisfies PromptSource. Use for Firestore-backed or static config."""

    def __init__(self, prompts: dict[str, str]):
        self._prompts = prompts

    def get_prompt(self, key: str) -> str:
        if key not in self._prompts:
            raise KeyError(f"Prompt not found for key: {key}")
        return self._prompts[key]

class LangfusePromptSource:
    """Fetches prompt content from Langfuse by prompt name and label. Injectable into config sources."""

    def __init__(self, label: str = "production", name_prefix: str = "face-ai"):
        self._client = get_client()
        self._label = label
        self._name_prefix = name_prefix

    def get_prompt(self, key: str) -> str:
        # e.g. key "beard/full_beard" -> Langfuse prompt name "face-ai/beard-full_beard"
        name = f"{self._name_prefix}/{key.replace('/', '-')}"
        prompt_obj = self._client.get_prompt(name, label=self._label)
        return prompt_obj.prompt if hasattr(prompt_obj, "prompt") else str(prompt_obj)
```

1. **Firestore source always passes a PromptSource** — When building a Gemini driver config, it uses the injected Langfuse `PromptSource` when present; otherwise it wraps the Firestore prompts dict in `DictPromptSource` and passes that:

```python
# Conceptual: inside FirestoreFilterConfigurationSource, when building beard config

def _create_beard_config(self, doc_data: dict) -> BeardFilterConfiguration | None:
    # ...
    if "gemini" in drivers:
        gemini_config = drivers["gemini"]
        if self.prompt_source is not None:
            # Langfuse: use the injectable prompt source
            source: PromptSource = self.prompt_source
            key_prefix = "beard"
        else:
            # Firestore: wrap the prompts dict in a PromptSource adapter
            prompts_dict = gemini_config.get("prompts", {})
            if not prompts_dict:
                return None
            source = DictPromptSource(prompts_dict)
            key_prefix = None  # keys are the dict keys (e.g. "full_beard") as-is

        driver_configurations["gemini"] = GeminiBeardFilterDriverConfiguration(
            prompt_source=source,
            prompt_key_prefix=key_prefix,  # for Langfuse: "beard" -> key "beard/full_beard"
        )
```

1. **Driver config accepts only PromptSource** — The driver config takes a single `prompt_source` (and optional key prefix for Langfuse naming). `get_prompt(mode)` always delegates to the prompt source:

```python
# Conceptual: GeminiBeardFilterDriverConfiguration after change — only PromptSource

class GeminiBeardFilterDriverConfiguration(FilterDriverConfiguration):
    driver_name = "gemini"

    def __init__(
        self,
        prompt_source: PromptSource,
        prompt_key_prefix: str | None = None,
    ):
        self.prompt_source = prompt_source
        self.prompt_key_prefix = prompt_key_prefix  # e.g. "beard" for Langfuse key "beard/full_beard"

    def get_prompt(self, mode: str) -> str:
        key = f"{self.prompt_key_prefix}/{mode}" if self.prompt_key_prefix else mode
        return self.prompt_source.get_prompt(key)
```

The driver config has one abstraction: it always uses a `PromptSource`. Any dictionary (Firestore, defaults, or tests) is wrapped in `DictPromptSource`; Langfuse is used via `LangfusePromptSource`. Naming (key prefix, Langfuse prompt names), caching, and sync/async for `get_prompt` can be tuned in implementation.

### 4.2 How Face AI Can Use Prompt Management

- **Prompt linked to trace** — When a request uses a prompt fetched from Langfuse, the SDK can associate that prompt (name and version) with the trace. In Langfuse you can then see which prompt version was used for each filter run, and correlate behaviour (e.g. errors or cost) with prompt content.
- **Prompt diff and history** — Langfuse keeps a version history for each prompt. Prompt diff and history let you see what changed between versions and when, which supports safe rollbacks and clearer debugging when a new version behaves worse.
- **Comparing performance by prompt version** — In the Evaluation section we use prompt versions to compare how different prompts perform (e.g. on a fixed dataset or on production traces). Versioning in Langfuse is the basis for that comparison.
- **Labels and A/B testing** — Langfuse is not an A/B testing platform: it does not assign users to variants or decide which prompt to serve. It does support **labels** (e.g. `production`, `experiment-v2`). Face AI can use an external A/B or feature-flag tool to split the audience (e.g. by user id or segment) and then, per request, pass a **label** (or prompt name/version) to the Langfuse source. The backend fetches the prompt for that label (e.g. `label="production"` for control, `label="experiment-v2"` for the variant) and uses it in the existing flow. So: A/B tool decides “this user gets variant B”; backend asks Langfuse for the prompt with `label="variant-b"` and uses it; traces and evaluations in Langfuse are still grouped by prompt version/label for analysis.

---

## 5. Evaluation and Scoring for Face AI

Langfuse serves as the **observability and evaluation platform** for Face AI image generation, providing: tracing of generation requests, user feedback collection, annotation workflows, dataset creation from traces, experiment management, and automated evaluation via **LLM-as-a-Judge**. It supports evaluation pipelines that combine automated scoring with human annotation ([e.g. Langsmith vs Langfuse vs Maxim](https://dev.to/debmckinney/choosing-an-evaluation-stack-langsmith-vs-langfuse-vs-maxim-16ej)).

Two workflows are proposed, depending on **data governance** (whether production user-generated images may be used).

### 5.1 Approach 1 — Restricted Environment (No Production Images)

**Goal:** Improve models and prompts **without using production user-generated images**, e.g. for compliance. All evaluation datasets are built from **development or staging traces**.

**Process:**

1. **Trace collection** — Image generation in dev/staging is logged as Langfuse traces. Each trace includes: prompt, generation parameters, generated image, model version, prompt version, and metadata. These traces form the candidate pool for datasets.
2. **Expert annotation** — Experts review traces via **annotation queues**. Annotations can include: prompt alignment score, image quality score, artifact detection, preferred output, and comments or corrected prompts. Queues allow domain experts to label traces and turn them into evaluation datasets ([LLM observability tools](https://www.langchain.com/articles/llm-observability-tools)).
3. **Dataset creation** — Annotated traces become structured datasets (e.g. prompt, generated_image, optional reference_image, human_score, quality_labels). Datasets act as ground truth for experiments.
4. **Experiments** — When improving prompts or models, run the generation pipeline on the dataset and record outputs as experiment runs (e.g. Dataset `dev_image_quality_v1`, Experiment A: prompt_template_v1 + model_v1 vs Experiment B: prompt_template_v2 + model_v1).
5. **Evaluation** — Experiment outputs are scored with **LLM-as-a-Judge**: a multimodal model evaluates prompt alignment, realism, artifacts, and composition. LLM judges can score without ground-truth references ([Langfuse evaluations](https://heidloff.net/article/langfuse-evaluations)). Optional: human annotation, pairwise ranking, automated metrics (e.g. CLIP similarity).
6. **Deployment decision** — Compare experiments on average quality score, prompt alignment, artifact rate, latency, and compute cost; deploy improved versions.

### 5.2 Approach 2 — Production Feedback Loop (Production Images Allowed)

**Goal:** Use **real production data and user feedback** to continuously improve image generation.

**Process:**

1. **Production trace logging** — All generation requests are logged as Langfuse traces (prompt, parameters, generated image, model and prompt version).
2. **User feedback** — Users provide feedback (e.g. like/dislike, optional rating, report issue). This is a key signal for poor generations.
3. **Online LLM evaluation** — An automated evaluator runs on production traces. A multimodal judge scores prompt–image alignment, visual quality, artifacts, and safety; scores are attached to traces ([Langfuse LLM-as-a-judge](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge)).
4. **Trace filtering** — Prioritise traces for review using rules such as: judge_score below threshold, user_dislike, rare prompt category, artifact detection. This creates a high-signal review pool.
5. **Expert annotation** — Selected traces go to annotation queues. Experts validate or correct judge scores, label failure types (e.g. prompt misinterpretation, artifact, style mismatch, composition, safety), and suggest improved prompts.
6. **Dataset creation** — Reviewed traces become dataset items, reflecting real user failures and edge cases.
7. **Continuous experiments** — Teams run experiments (new prompt templates, models, pipelines, parameters) and evaluate against the dataset.
8. **Deployment and monitoring** — New versions are deployed gradually; monitor average judge score, user satisfaction, artifact rate, latency, and compute cost.

### 5.3 Recommended Improvements

- **Scoring** — The AI Lab–style scoring approach (e.g. 1–5 stars, normalized to 0–1.0, attached via trace id) fits our use case. Additional **evaluation context** can improve scoring: e.g. **side-by-side images** (original input vs generated output, or variant A vs B) in the annotation UI to make human or model-as-judge evaluation more reliable.
- **Pairwise evaluation** — For images, pairwise comparison ("Which of A/B better matches the prompt?") is often more reliable than absolute scoring.
- **Hybrid evaluation** — Combine human annotations, LLM-as-a-Judge, automated metrics, and user feedback for robust quality signals.
- **Error clustering** — Cluster failures (e.g. prompt alignment, artifacts, style mismatch, composition) to identify systemic issues.
- **Version tracking** — Experiments should track prompt version, model version, generation parameters, and dataset version for reproducible evaluation.

### 5.4 Continuous Improvement Loop

```
Image Generation → Langfuse Trace → User Feedback + LLM Judge → Trace Filtering
       → Annotation Queue → Dataset Creation → Experiments → Prompt/Model Improvements
       → Deployment → Production Monitoring
```

### 5.5 Benefits

- Compliance-safe evaluation when production images are restricted.
- Scalable automated scoring via LLM-as-a-Judge.
- Continuous dataset growth from traces and annotations.
- Faster prompt and model iteration with versioned experiments.
- Transparent quality monitoring (scores, artifact rate, user feedback).

---

## 6. Langfuse Deployment Strategy

This section evaluates deployment options for the Face AI application and the broader organization, and recommends an approach.

### 6.1 Deployment Options: Cloud vs Self-Hosted

Langfuse is available in two forms:

- **Langfuse Cloud** — Managed SaaS; usage-based pricing ([pricing](https://langfuse.com/pricing)).
- **Self-Hosted** — Open-source deployment on private infrastructure via Docker or Kubernetes ([self-hosting](https://langfuse.com/self-hosting), [ClickHouse + Langfuse](https://clickhouse.com/docs/cloud/features/ai-ml/langfuse)).

Both use the same core platform. Self-hosting keeps traces, prompts, and evaluation data in-house and allows integration with existing observability and DevOps tooling. It is well suited when **multiple applications** share a **centralized evaluation and observability platform**.

**Context for this document:** multiple applications will use Langfuse, a dedicated DevOps team manages infrastructure, and centralized observability is preferred. Under these conditions, **self-hosting Langfuse as a shared internal platform is the recommended approach**.

### 6.2 Self-Hosted: Architecture and Deployment Options

Self-hosted Langfuse uses a distributed stack:


| Component                      | Purpose                                    |
| ------------------------------ | ------------------------------------------ |
| PostgreSQL                     | Application state                          |
| ClickHouse                     | Trace analytics, high-throughput ingestion |
| Redis                          | Queue and caching                          |
| Object Storage (S3-compatible) | Large payload storage                      |
| Langfuse Web + Workers         | API and background processing              |


ClickHouse drives analytics and scale; Redis handles queues and caching ([Langfuse + ClickHouse](https://clickhouse.com/blog/langfuse-and-clickhouse-a-new-data-stack-for-modern-llm-applications)). The platform runs as multiple containers (web, workers, databases, cache) and can be deployed with **Docker Compose** (small setups) or **Kubernetes / Helm** (recommended for production). Production typically uses multiple web replicas, autoscaling workers, and managed databases ([PostgreSQL](https://langfuse.com/self-hosting/deployment/infrastructure/postgres), [ClickHouse](https://langfuse.com/self-hosting/deployment/infrastructure/clickhouse)).

**Alignment with current infra:** The current infrastructure is **GCP** and is assumed to be used for Langfuse deployment. If the organization already uses Kubernetes, managed PostgreSQL (e.g. Cloud SQL), managed Redis, and S3-compatible storage (e.g. GCS with S3-compatible API), self-hosted Langfuse fits by adding ClickHouse (managed or self-managed) and the Langfuse workloads. Deployment options should be evaluated against this stack (e.g. Helm chart on existing GCP clusters vs dedicated Langfuse namespace).

### 6.3 Resource Requirements and Environment Configuration

- **Resource requirements** — Plan for: PostgreSQL (application DB), ClickHouse (analytics), Redis, object storage, and Langfuse web/worker pods. Sizing depends on trace volume and retention; start with Langfuse’s recommended minimums and scale ClickHouse and workers as ingestion and query load grow. Exact resources (CPU, number of instances, memory) are yet to be decided based on estimated workload; see **Risks, blockers, and open questions** below.

### 6.4 Upgrade, Maintenance, and Operational Overhead

Self-hosting implies:

- **Upgrades** — Follow Langfuse release notes and upgrade the application containers; coordinate with PostgreSQL/ClickHouse/Redis compatibility when applicable.
- **Maintenance** — Backups (PostgreSQL and optionally ClickHouse), monitoring (health, latency, queue depth), logging, and capacity planning.
- **Operational overhead** — With a **dedicated DevOps team**, this can be absorbed via existing CI/CD, monitoring, and runbooks. Without it, Langfuse Cloud reduces operational burden at the cost of data leaving internal infrastructure and usage-based pricing.

### 6.5 Data Retention and Storage Scaling

- **Retention** — Define how long traces, prompts, and evaluation data are kept (e.g. 90 days for traces, longer for datasets). Configure retention in Langfuse and, for ClickHouse, use TTL or retention policies so storage does not grow unbounded.
- **Storage scaling** — ClickHouse and object storage grow with trace volume and payload size. Plan scaling for both (e.g. ClickHouse cluster sizing, S3 lifecycle or tiering) and align retention with compliance and cost.

### 6.6 Recommendation and Summary


| Option             | Best for                                                   |
| ------------------ | ---------------------------------------------------------- |
| **Langfuse Cloud** | Small teams, quick start, minimal ops                      |
| **Self-Hosted**    | Multiple applications, centralized platform, data in-house |


**Recommendation:** Operate **Langfuse as a centralized self-hosted platform** for the organization:

- One shared instance used by Face AI and other applications.
- Deployed on internal Kubernetes (or equivalent), integrated with existing auth, monitoring, and storage.
- Centralized observability and evaluation, shared datasets, and consistent data governance and retention.

Langfuse Cloud remains an option for early prototyping or isolated experiments; for long-term production use across multiple services, self-hosting offers better alignment with data governance, scalability, and reuse of existing DevOps capacity.

### 6.7 Risks, blockers, and open questions

- **Exact resource sizing** — CPU, number of instances, and memory for Langfuse (and optionally ClickHouse/Redis) are yet to be decided based on estimated workload. This should be refined once trace volume and retention targets are known.
- **Langfuse availability** — The main risk is **Langfuse becoming unavailable** (outage, network, or misconfiguration). The app **must continue to work when Langfuse is down**. Tracing and prompt management should be best-effort: failures to send traces or to fetch prompts from Langfuse must not break request handling. For **prompt management** in particular, **fallback prompts** are required—either hardcoded defaults or another source (e.g. Firestore dict as in the migration plan). Ensure the backend always has a usable prompt source when Langfuse is unreachable.

---

## 7. General applicability for content-generating applications

The patterns described in this document are not specific to Face AI or image generation. Langfuse, and the way we use it here, applies to **any application that generates content**—whether that content is **text** (e.g. chatbots, summarization, code generation, copywriting) or **images** (e.g. image editing, style transfer, generative art). The same three pillars—**prompt strategy**, **tracing**, and **evaluation**—fit well and can be used in general across such apps.

### 7.1 Why it fits content-generation apps

Content-generation applications share a common shape:

- **Inputs** — Prompts (and optionally other inputs such as images, documents, or context).
- **Model calls** — One or more LLM or generative model calls that produce the output.
- **Outputs** — Generated text or images (or both) that need to be correct, on-brand, and cost-effective.

To improve quality, cost, and safety, teams need to see what was sent to the model, what was returned, how much it cost, and how good the result was. That is exactly what Langfuse is built for: **observability**, **prompt management**, and **evaluation** in one place.

### 7.2 Prompt strategy (general)

- **Single abstraction** — Regardless of modality (text or image), prompts can be managed through a single abstraction (e.g. a `PromptSource` or Langfuse prompt API). The app asks for a prompt by key or name; the platform supplies the version appropriate for the environment or experiment.
- **Versioning and rollout** — Prompts are versioned, labeled (e.g. `production`, `experiment-v2`), and linked to traces. Any content-generating app can use this to roll out prompt changes safely, compare versions, and roll back if needed.
- **A/B and experiments** — An external A/B or feature-flag system can choose which prompt (or model) to use per request; the backend fetches the corresponding prompt from Langfuse by label or version. The same pattern works for text and image apps.

### 7.3 Tracing (general)

- **Request-centric model** — One trace = one user request; observations = model calls, tool calls, or other steps. This applies to text generation (e.g. one chat turn, one summarization call) and image generation (e.g. one filter application, one style transfer).
- **Sessions and users** — Sessions group related requests (e.g. a conversation, an editing session). User IDs attach cost, usage, and quality to users. Both are modality-agnostic.
- **Metadata and tags** — Tags (e.g. feature name, model, prompt version) and metadata (e.g. parameters, variant) help filter and analyze traces for any type of content.
- **Cost and latency** — Token usage and cost are tracked for LLM calls; latency is captured for every step. Image-generation apps may also track compute or token cost per request in the same trace model.

### 7.4 Evaluation (general)

- **Automated scoring** — LLM-as-a-Judge (or similar) can score text outputs (relevance, tone, correctness) or image outputs (prompt alignment, quality, artifacts). The evaluation pipeline is the same; only the judge prompt and metrics are tailored to the modality.
- **Human annotation** — Annotation queues and datasets work for both text and image: experts label quality, errors, or preferences; the result is a dataset for experiments and monitoring.
- **User feedback** — Thumbs up/down, ratings, or issue reports apply to any generated content. Feedback can be attached to traces and used for filtering, prioritization, and continuous improvement.
- **Experiments** — Run experiments (prompt A vs B, model A vs B) on fixed datasets or on sampled production traces; compare scores, cost, and latency. Same workflow for text and image apps.

### 7.5 Summary

For **any app that generates content** (text or image), the same organizational usage applies:


| Pillar              | Role in content-generating apps                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------ |
| **Prompt strategy** | One place to version, deploy, and experiment with prompts; works for all modalities.             |
| **Tracing**         | Full visibility per request: inputs, outputs, cost, latency, sessions, users.                    |
| **Evaluation**      | Automated scoring, human annotation, user feedback, and experiments to improve quality and cost. |


Face AI (image generation) is one concrete instance of this. The same framework—centralized observability, prompt management, and evaluation—can be adopted for other internal applications that generate text or images, with minimal conceptual change and a single shared Langfuse platform (as in section 6).