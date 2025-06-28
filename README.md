## Project Statement

**Title:** *AI Startup Intelligence MCP*

### 1. Purpose

Build a **minimal client–server “MCP” (Multi-source Company-Profiler) system** that can answer natural-language questions such as

> “Tell me about promising AI startups.”

The server aggregates and cross-validates data from:

| Tier-1 Paid Data | Public / Open Web |
| ---------------- | ----------------- |
| CB Insights      | Company websites  |
| Crunchbase       | News articles     |
| PitchBook        | SEC filings       |
| S\&P Capital IQ  | GitHub / LinkedIn |

### 2. High-Level Goals

1. **Query → Insight pipeline** in < 5 s for typical searches.
2. **Transparent reasoning** – show which sources support each fact.
3. **Confidence score** per data point (source count × recency × source weight).
4. **Zero-install web UI** with modern UX.

### 3. Architecture Overview

```text
┌──────────────────────┐      1. Query JSON/REST
│   MCP Frontend (FE)  │ ───────────────►
└──────────────────────┘                │
        ▲                               │
        │ 4. JSON response              ▼
┌──────────────────────┐      2. RPC       ┌─────────────────────────────┐
│   Auth-API Gateway   │ ───────────────► │ MCP Server (FastAPI)        │
└──────────────────────┘                  │  • Orchestrator             │
        ▲                                3│  • Source Connectors       │
        │  WebSocket                    ▼ │  • Reasoning / LLM Layer   │
┌──────────────────────┐   ┌──────────────┴┐ • Dedup & Scoring          │
│ React + Next.js FE   │   │ Headless Browser│ • Postgres + Redis cache  │
│ (TypeScript, Tailwind│   │  (Playwright)   └───────────────────────────┘
└──────────────────────┘
```

### 4. Component Details

| Layer                     | Key Tasks                                                                                                              | Suggested Tech                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Frontend (MCP-Client)** | • Search bar & filters  <br>• Result cards & expandable company drawer  <br>• “Why-this-fact” pop-over showing sources | Next.js 14, React Query, Shadcn/UI            |
| **API Gateway**           | • OAuth (GitHub/Google) <br>• Rate-limit per user <br>• Enforce paid-data usage quotas                                 | FastAPI-Users, Redis RateLimiter              |
| **Orchestrator**          | • Parse natural-language query <br>• Dispatch parallel jobs to connectors <br>• Fuse & rank results                    | FastAPI, Celery/RabbitMQ                      |
| **Source Connectors**     | • Auth to CB Insights, Crunchbase, etc. <br>• Scrape public pages with Playwright <br>• Normalize to a common schema   | Playwright (headless Chrome), Pydantic models |
| **Reasoning Layer**       | • Entity resolution (fuzzy name match, URL match) <br>• Confidence scoring heuristic + LLM justification               | Python, spaCy, OpenAI o3                      |
| **Storage / Cache**       | • Company & round tables <br>• ETL logs, error traces                                                                  | PostgreSQL, Redis                             |

### 5. Data-Validation Strategy

1. **Cross-source agreement** ≥ 2 sources → high confidence.
2. **Timestamp decay** ↓ confidence as data ages (half-life 6 months).
3. **Outlier detection** on funding/valuation vs. peer median.
4. **Manual override** hooks for analysts.

### 6. Sprint-Level Roadmap (8 weeks)

| Sprint       | Focus                                | Demo / Deliverable                      |
| ------------ | ------------------------------------ | --------------------------------------- |
| **0** (1 wk) | Requirements + API keys secured      | System design doc                       |
| **1**        | Skeleton FE + basic FastAPI endpoint | “Hello World” query returns stub data   |
| **2**        | Crunchbase + public web connector    | First end-to-end query with real data   |
| **3**        | CB Insights & PitchBook connectors   | Multi-source merge + confidence flags   |
| **4**        | Entity resolution & scoring engine   | Duplicate companies resolvable          |
| **5**        | Headless browser scrape module       | Pull GitHub & news headlines            |
| **6**        | LLM explanation layer                | “How we got this answer” feature        |
| **7**        | Polish UI, load test, auth, docs     | Candidate v1.0 deploy (Docker / Vercel) |

### 7. Success Metrics

* **< 5 s P95 latency** per query (100 results).
* **≥ 90 % precision** on company identity (hand-checked sample n=200).
* **NPS ≥ 45** from pilot users (analysts & founders).

### 8. Potential Risks & Mitigations

| Risk                      | Mitigation                                       |
| ------------------------- | ------------------------------------------------ |
| API quota / cost overruns | Caching, nightly batch syncs, tiered user plans  |
| Legal / T\&C compliance   | Respect robots.txt, honor data-provider licenses |
| Captcha / anti-bot blocks | Rotate IPs, use provider APIs where possible     |







## How to make this project

This repository now contains a more featureful implementation of the "AI Startup Intelligence MCP" system. The FastAPI server aggregates results from paid data providers (Crunchbase, CB Insights, PitchBook) and from public web scraping. All connectors are mocked, but the orchestrator shows how confidence scores are merged. To run the project locally:

```bash
# Install server dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r server/requirements.txt

# Start the API server
uvicorn server.app.main:app --reload
```

Open `client/index.html` in a browser and issue a search query. The server will return sample data from the mock connectors.
