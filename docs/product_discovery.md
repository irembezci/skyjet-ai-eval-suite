# Product Discovery: SkyJet AI Customer Support Assistant

## 1. Problem Space & Context
Aviation customer service operates under high volume and severe margin pressure. Flight disruptions, baggage queries, and seat changes create massive call-center queues. Today, airlines handle this with a fragmented two-tier approach:
* **Tier-0 (Legacy Chatbots):** Rule-based intent matchers (e.g., lexical keyword bots) that fail at conversational nuances, cannot resolve edge cases, and frequently dump static URL links on frustrated passengers.
* **Tier-1 (Human Support Agents):** Expensive ($4.50–$6.00 per contact), slow during disruption spikes (wait times exceeding 45 minutes), and burdened by repetitive transactional tasks (seat reassignment, baggage checks).
* **The Cloud GenAI Paradox:** While commercial models (e.g., GPT-4) can converse fluidly, routing millions of passenger inquiries through third-party APIs introduces ongoing token costs and exposes PII (Personally Identifiable Information) across external network boundaries.


## 2. Jobs to Be Done (JTBD)

### Job 1: Quick Policy Clarity
* **When** I am packing or traveling with specialized items (pets, sporting goods, restricted baggage),
* **I want to** get an authoritative, unambiguous yes/no answer with exact limits,
* **So that** I don't face unexpected fees or boarding denial at the airport gate.

### Job 2: Frictionless Self-Service Operations
* **When** I need to verify my reservation or change my seat assignment,
* **I want to** complete the modification directly in the chat interface in seconds,
* **So that** I don't have to log into complex legacy booking portals or wait on hold for an agent.

### Job 3: Trust & Privacy Assurance
* **When** I share my booking references and personal travel details,
* **I want to** be certain my data is isolated and cannot be accessed by other passengers,
* **So that** my personal itinerary and identity remain strictly secure.


## 3. User Personas

| Dimension | Persona A: "Stressed Commuter" (Sarah) | Persona B: "Rule-Conscious Traveler" (Kenan) |
| :--- | :--- | :--- |
| **Profile** | Frequent business flyer, time-constrained, on mobile. | Family/leisure traveler, traveling with infant or pet. |
| **Primary Need** | Instant seat modification and gate/status checks. | Nuanced policy guidance (cabin pet weights, stroller limits). |
| **Frustration** | Getting linked to a 20-page web portal when asking to change a seat. | Ambiguous chatbot answers like *"Check our website for details"*. |
| **Success Metric** | Task resolution in under 15 seconds. | 100% factual policy answers without conflicting guidelines. |


## 4. Competitive Landscape Benchmark

| Feature / Metric | Legacy Chatbots (Rule-based) | Enterprise Cloud LLM (GPT-4) | **SkyJet AI (Hardened SLM)** |
| :--- | :--- | :--- | :--- |
| **Inference Cost** | Near-zero | High ($0.03–$0.06 / resolution) | **$0.00 / Query (On-Premise)** |
| **Data Privacy (PII)** | On-premise capable | Third-party cloud exposure | **Zero Egress (Local Qwen 1.7B)** |
| **Conversational Fluency** | Poor (Rigid keyword trees) | Superior | **High (RAG Grounded)** |
| **Transactional Tooling** | Fragile API hooks | Non-deterministic triggers | **Deterministic JSON Tool Gate** |
| **Latency (p50)** | < 1,000 ms | 2,500–5,000 ms | **~3,350 ms** |
| **Security Guardrails** | Static filters | Prompt-only defenses | **Backend Identity Gate (IDOR Block)** |


## 5. Strategic Product Thesis
By pairing an open-weight Small Language Model (**Qwen 1.7B**) with **RAG** for policy retrieval and **Deterministic Backend Routing** for mutations, an airline can automate up to 60% of Tier-1 inbound contacts at zero recurring token cost, maintaining compliance and PII protection.
