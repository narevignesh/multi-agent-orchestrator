
---

# 🚀 Multi-Agent Orchestrator

**An Open-Source Reference Framework for Multi-Agent Coordination and AI Workflow Orchestration**

---

## 🧠 Overview

The **Multi-Agent Orchestrator** is a **production-grade, locally runnable system** that demonstrates how to coordinate multiple specialized AI agents to complete complex, multi-step tasks in a controlled, auditable, and safe environment.

It combines a **FastAPI backend** for orchestration and guardrails with a **Streamlit frontend** for task control and visualization. The project showcases **agentic system design**, **asynchronous task execution**, and **safety-first orchestration**.

The system integrates seamlessly with the **Grooq API** (or a mocked LLM client) for natural language reasoning, summarization, and decision-making.

---

## 🎯 Key Objectives

* ✅ Demonstrate a **modular multi-agent architecture** (Planner, Executor, Validator, Monitor).
* 🔄 Build an **async orchestrator** with retries, rollback hooks, and structured error handling.
* 🔐 Implement **safety layers** for input validation and prompt-injection protection.
* 📜 Maintain an **append-only audit trail** for transparency and compliance.
* 🧪 Provide a **comprehensive test suite** including safety, unit, and integration tests.
* 🧩 Deliver an **interactive Streamlit dashboard** for visual orchestration and analysis.

---

## 🏗️ System Architecture

### **1. Backend — FastAPI**

Core components live under the `app/` or `backend/app/` directory.

| Module                     | Description                                                                |
| -------------------------- | -------------------------------------------------------------------------- |
| **main.py**                | FastAPI entrypoint; registers routes and middleware.                       |
| **orchestrator.py**        | Async workflow engine managing agent coordination, retries, and rollbacks. |
| **agents/planner.py**      | Decomposes user task into subtasks with priority and dependency order.     |
| **agents/executor.py**     | Executes subtasks (API calls, data extraction, or model inference).        |
| **agents/validator.py**    | Ensures outputs meet formatting, policy, and factual rules.                |
| **safety.py**              | Validates input, removes unsafe tokens, detects prompt injections.         |
| **monitor.py**             | Logs step-by-step execution, metrics, and audit records.                   |
| **services/llm_client.py** | Handles Grooq API calls with retries and error control.                    |
| **models/schemas.py**      | Defines Pydantic models for validation of tasks, plans, and responses.     |

### **2. Frontend — Streamlit**

Located in `ui/` or `frontend/`.

| File                 | Description                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| **streamlit_app.py** | UI to create and submit orchestration tasks, view live logs, inspect plans, and download results. |
| **components/**      | Optional sub-components for progress visualization, safety alerts, and agent status.              |

### **3. Tests**

Comprehensive testing under `/tests`.

| Suite                    | Purpose                                                                |
| ------------------------ | ---------------------------------------------------------------------- |
| **tests/unit/**          | Individual agent and helper function validation.                       |
| **tests/integration/**   | Full pipeline verification using mocked Grooq responses.               |
| **tests/agentic_tests/** | Guardrail and rollback behavior validation against adversarial inputs. |

---

## 🔐 Safety & Guardrails

* Strict **Pydantic schema enforcement** for all input data.
* Prompt-injection detection for malicious tokens or instructions.
* Controlled execution layer that prevents unapproved external actions.
* Every rejected or sanitized input logged in **audit logs** for traceability.
* Sensitive fields are redacted before storage or display.

---

## 📊 Monitoring, Logging, and Compliance

* Each orchestration run generates **structured JSON logs** for every step.
* **Append-only audit log** captures:

  * Task ID, timestamp, and project name
  * Sanitized request payload
  * Generated plan and reasoning traces
  * Subtask outcomes, retries, and rollbacks
  * Validation and safety results
* **Metrics**: Execution time, retry counts, validation outcomes
* **Audit Log Path**: `app/logs/audit.log`

---

## 🌍 Example Real-World Workflow: Market Research (Competitive Analysis)

**Goal:** Create a 300-word competitive analysis for *Product X* focusing on pricing and features.

**Workflow:**

1. 🧩 **Planner:** Breaks task into subtasks:

   * Identify top competitors
   * Extract pricing and features
   * Generate synthesis draft
   * Validate and finalize report
2. ⚙️ **Executor:** Gathers data, performs synthesis via Grooq API.
3. 🧾 **Validator:** Checks word count, factual accuracy, compliance.
4. 📈 **Monitor:** Logs each phase and updates audit trail.

**Sample API Request:**

```json
{
  "task": "Create a 300-word competitive analysis for product X focusing on pricing and features",
  "project": "Market Research",
  "priority": "medium"
}
```

**Sample API Response (initial):**

```json
{
  "task_id": "task-20251026-001",
  "status": "accepted",
  "plan": [
    "Identify top 5 competitors",
    "Extract pricing tiers and key features",
    "Draft 300-word analysis",
    "Validate formatting and citations"
  ],
  "result": null
}
```

**Final Response:**

```json
{
  "task_id": "task-20251026-001",
  "status": "completed",
  "result": "<Final 300-word analysis>",
  "audit_path": "app/logs/audit.log"
}
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/narevignesh/multi-agent-orchestrator.git
cd multi-agent-orchestrator
```

### 2. Create Virtual Environment

#### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# or if split folders
pip install -r backend/requirements.txt
pip install -r ui/requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Update `.env` with:

```
GROOQ_API_KEY=your_grooq_api_key
LOG_LEVEL=INFO
AUDIT_LOG_PATH=app/logs/audit.log
MAX_RETRIES=3
RETRY_BACKOFF_SECONDS=2
```

### 5. Run Backend (FastAPI)

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

API Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6. Run Frontend (Streamlit)

```bash
streamlit run ui/streamlit_app.py --server.port 8501
```

UI → [http://localhost:8501](http://localhost:8501)

### 7. Submit Task Example

```bash
curl -X POST "http://127.0.0.1:8000/orchestrate" \
-H "Content-Type: application/json" \
-d '{
  "task":"Create a 300-word competitive analysis for product X focusing on pricing and features",
  "project":"Market Research",
  "priority":"medium"
}'
```

### 8. View Live Audit Log

```bash
tail -f app/logs/audit.log
```

---

## 🧪 Testing

Run all tests:

```bash
pytest -q
```

Specific suites:

```bash
pytest tests/unit -q
pytest tests/integration -q
pytest tests/agentic_tests -q
```

Mocked tests simulate Grooq API to enable **offline reproducibility**.

---

## 🧰 Development Notes

* Replace Grooq integration in `services/llm_client.py` with a **mock client** for local or CI runs.
* Each agent can register **rollback hooks** to revert failed steps.
* Structured logging ensures compatibility with **ReadyTensor observability**.
* No cloud or Docker dependencies — **fully local-first design**.

---

## 💡 Use Cases

* Research report synthesis
* Workflow decomposition & validation
* AI pipeline orchestration
* Safety-layer demonstration
* Audit-compliant automation demos

---

## 🔍 Keywords for ReadyTensor

`multi-agent`, `AI orchestrator`, `FastAPI`, `Streamlit`, `LLM`, `Grooq API`, `agentic architecture`, `task automation`, `prompt injection safety`, `AI governance`, `audit logging`, `async orchestration`, `AI system reliability`

---

## 🧑‍💻 Contributing

1. Fork the repository
2. Create a new branch (`feature/my-update`)
3. Commit changes and ensure tests pass
4. Submit a pull request

We welcome improvements to:

* Agent logic & safety rules
* Monitoring and logging enhancements
* Integration with more LLM providers

---

## 📜 License

This project is licensed under the **MIT License** — free for modification, use, and redistribution.

---

## 📈 Author & Maintainer

**Author:** Nare Vignesh
**University:** Mohan Babu University — B.Tech AI & ML
**GitHub:** [github.com/narevignesh](https://github.com/narevignesh)
**LinkedIn:** [linkedin.com/in/narevignesh](https://linkedin.com/in/narevignesh)
**Contact:** [vigneshnaidu022@gmail.com](mailto:vigneshnaidu022@gmail.com)

---

Wo
