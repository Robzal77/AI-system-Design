# Architecture diagrams

These are proposed team designs informed by the user-provided learning notes and verified video topics. Mermaid diagrams render directly in GitHub. Each diagram states implementation status; only the limited offline lab is implemented here.

## 1. Enterprise AI CoE — high-level design

**Status:** Reference architecture. Shared controls support multiple business functions; data permissions remain enforced within each service.

```mermaid
flowchart TB
    subgraph Users[User and application layer]
        PORTAL[Enterprise AI portal]
        APPS[Commercial / Finance / Operations / HR apps]
    end
    subgraph Identity[Identity and security]
        SSO[Enterprise SSO: e.g. Entra ID]
        GW[API gateway: quotas and request identity]
        AUTH[Service and data authorization]
    end
    subgraph Control[AI control and orchestration]
        POLICY[Input policy and output validators]
        FLOW[Workflow orchestrator and durable state]
        ROUTER[Approved model router]
        CACHE[Eligible read-only cache]
        APPROVAL[Human approval service]
    end
    subgraph Data[Governed enterprise data]
        QUERY[Authorized query / measure service]
        RAG[ACL-filtered retrieval]
        SQL[SQL / Databricks / Dataverse]
        BI[Power BI / Fabric semantic models]
        DOCS[SharePoint / document sources]
    end
    subgraph Models[Approved model providers]
        PRIMARY[Primary provider]
        BACKUP[Compatible fallback provider]
    end
    OPS[Operations: traces / evaluations / audit / cost / adoption]
    PORTAL --> SSO
    APPS --> SSO
    SSO --> GW --> AUTH --> POLICY --> FLOW
    FLOW --> CACHE
    FLOW --> ROUTER
    FLOW --> APPROVAL
    FLOW --> QUERY
    FLOW --> RAG
    QUERY --> SQL
    QUERY --> BI
    RAG --> DOCS
    ROUTER --> PRIMARY
    ROUTER --> BACKUP
    GW -.-> OPS
    FLOW -.-> OPS
    ROUTER -.-> OPS
    APPROVAL -.-> OPS
```

Numbers and business KPIs should come from governed queries or semantic measures. Documents support explanation and evidence. Do not assume vector retrieval reliably computes a sales total.

## 2. Request lifecycle — low-level sequence

**Status:** Proposed service interactions. The lab simulates selected boundaries without these services.

```mermaid
sequenceDiagram
    actor User
    participant G as Gateway
    participant A as Authorization
    participant C as Cache
    participant O as Orchestrator
    participant D as Governed data
    participant R as Model router
    participant M as Approved provider
    participant V as Output validator
    User->>G: Request + session credential
    G->>A: Verify identity and permissions
    alt Denied
        A-->>G: Denial
        G-->>User: Unauthorized response
    else Authorized
        A-->>G: Server-derived tenant and permission context
        G->>C: Lookup with scoped/versioned key
        alt Eligible hit
            C-->>V: Cached answer and source versions
        else Miss
            G->>O: Validated request + trusted identity
            O->>D: Authorized query/retrieval
            D-->>O: Evidence + versions + citations
            O->>R: Task + constraints + budget
            R->>M: Model call within deadline
            M-->>V: Candidate answer
        end
        V-->>G: Valid answer or abstention/error
        G-->>User: Answer + citations + request ID
    end
```

Trace every step with a request ID. Validate cache eligibility before returning a hit. No raw credentials or sensitive document text belong in general telemetry.

## 3. Freshness and invalidation

**Status:** Proposed ingestion pipeline; CDC is not implemented in the lab.

```mermaid
flowchart LR
    SRC[Source insert / update / delete / ACL change] --> E[Versioned event]
    E --> Q[Durable ingestion queue]
    Q --> P[Idempotent processor]
    P --> V{Newer source version?}
    V -->|No| IGN[Ignore duplicate / older event]
    V -->|Yes| IDX[Update or delete index record and ACLs]
    IDX --> GEN[Commit checkpoint / corpus generation]
    GEN --> INV[Invalidate affected cached answers]
    GEN --> RET[Authorized retrieval sees new generation]
    P -->|Failure| DLQ[Retry budget then dead-letter queue]
    DLQ --> OWNER[Owner investigation and replay]
    E -.-> LAG[Measure event-to-index lag]
    GEN -.-> LAG
```

Use a coordinated visibility/invalidation strategy so a newly indexed generation cannot serve an old cache entry. Track permission revocations and tombstones, not only inserts.

## 4. Router and bounded fallback

**Status:** One deterministic task route and simulated timeout fallback exist in the lab. Deadlines, retry policies, and circuit breakers below are production design additions.

```mermaid
flowchart TD
    T[Task + data policy + budget] --> FILTER[Filter approved compatible providers]
    FILTER --> ROUTE[Choose model by task requirements]
    ROUTE --> CALL[Call within overall deadline]
    CALL --> OK{Valid response?}
    OK -->|Yes| OUT[Output validation and return]
    OK -->|No| ERR{Retryable transient error?}
    ERR -->|No| FAIL[Return controlled error / abstain]
    ERR -->|Yes| B{Budget and deadline remain?}
    B -->|No| FAIL
    B -->|Yes| NEXT[Bounded retry or approved fallback]
    NEXT --> CALL
```

An authorization denial cannot be bypassed through fallback. Keep write execution separate from inference retries.

## 5. Approval and execution states

**Status:** Proposed durable state machine. The lab stops at pending approval and executes no writes.

```mermaid
stateDiagram-v2
    [*] --> Pending: Store exact payload and expiry
    Pending --> Rejected: Authorized reviewer rejects
    Pending --> Expired: Approval window expires
    Pending --> Approved: Authorized reviewer approves payload hash
    Approved --> Revoked: Approval withdrawn
    Approved --> Expired: Execution window expires
    Approved --> Executing: Recheck hash, ACLs, expiry; atomic claim
    Approved --> Rejected: Payload or permission check fails
    Executing --> Completed: Durable execution receipt
    Executing --> Reconciling: Timeout or uncertain external result
    Reconciling --> Completed: Receipt confirms success
    Reconciling --> Failed: Confirmed failure
    Executing --> Failed: Confirmed failure
    Failed --> Pending: Corrected proposal gets new approval
    Completed --> [*]
    Rejected --> [*]
    Expired --> [*]
    Revoked --> [*]
```

Use the same idempotency key when reconciling an uncertain execution. A changed payload requires a new approval. Prevent simultaneous workers from executing the same action.

## 6. Agentic BI workflow

**Status:** Proposed workflow, not a deployed Power BI integration. Labels represent responsibilities; each can be a deterministic task, human task, or model-assisted agent.

```mermaid
flowchart TD
    BRD[BRD submission] --> INTAKE[SSO + intake validation]
    INTAKE --> ANALYZE[Analyze requirements and ambiguities]
    ANALYZE --> REQ{Requirement approval}
    REQ -->|Revise| ANALYZE
    REQ -->|Approved| META[Authorized metadata and measure discovery]
    META --> BUILD[Generate report / model / DAX proposal]
    BUILD --> VALIDATE[Syntax / dependencies / business logic checks]
    VALIDATE --> QA[RLS / OLS / performance / regression tests]
    QA --> GATE{Validation passed?}
    GATE -->|No| BUILD
    GATE -->|Yes| PUB{Approval of exact deployment artifact}
    PUB -->|Rejected| BUILD
    PUB -->|Approved| DEPLOY[Authorized staged deployment]
    DEPLOY --> MON[Monitor / audit / verify business outcomes]
    ORCH[Durable orchestrator: versions, state, bounded attempts] -.-> META
    ORCH -.-> BUILD
    ORCH -.-> QA
    ROUTE[Approved model router] -.-> ANALYZE
    ROUTE -.-> BUILD
```

Bound correction loops and escalate after the retry budget. Freeze approved requirements and deployment artifacts by version/hash. Actual deployment requires configured APIs, licenses, credentials, environment permissions, and the project owner's release rules.
