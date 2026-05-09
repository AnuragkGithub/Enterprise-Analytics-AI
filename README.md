# Enterprise Analytics AI

Enterprise-grade AI-powered Analytics Assistant built using **FastAPI, Streamlit, SQL Intelligence, Prompt Engineering, and Dynamic Visualization Systems**.

The platform enables natural language analytics over enterprise datasets through intelligent query routing, SQL generation, relationship mapping, and visualization workflows.

---

# Features

- Natural Language to SQL Analytics
- AI-Powered Query Routing
- Dynamic SQL Generation
- Enterprise Data Relationship Mapping
- Interactive Streamlit Dashboard
- FastAPI Backend Services
- Prompt Engineering Framework
- Visualization Engine
- Schema-Aware Query Intelligence
- Training Dataset Support
- Modular Analytics Architecture

---

# Core Capabilities

## AI Query Intelligence

- Natural language analytics
- Dynamic query understanding
- Intelligent routing engine
- SQL query generation
- Context-aware analytics

## Enterprise Analytics

- Cross-table analysis
- Relationship-aware querying
- Data catalog intelligence
- Query optimization workflows
- Analytical result generation

## Visualization System

- Dynamic chart generation
- Interactive dashboard rendering
- Analytical data visualizations
- Automated chart selection

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Development |
| FastAPI | Backend API |
| Streamlit | Frontend Dashboard |
| SQLAlchemy | Database Engine |
| SQLite | Data Storage |
| Pandas | Data Processing |
| JSON | Metadata & Schema |
| YAML | Configuration |
| Plotly | Visualization |
| Prompt Engineering | AI Query Intelligence |

---

# Project Structure

```bash
ENTERPRISE_ANALYTICS_AI/
│
├── backend/
│   ├── query_engine.py
│   ├── query_router.py
│   ├── relationships.py
│   ├── server.py
│   ├── sql_generator.py
│   └── visualization_engine.py
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── examples/
│   └── question_variations.json
│
├── frontend/
│   ├── app.py
│   └── __init__.py
│
├── prompts/
│   └── system_prompt.txt
│
├── schema/
│   ├── data_catalog.json
│   ├── relationships.json
│   └── tables_schema.json
│
├── sql_queries/
│   └── queries.json
│
├── training_data/
│   ├── fine_tuning_dataset.jsonl
│   └── nl_sql_pairs.json
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# System Architecture

```text
User Question
      ↓
Frontend Dashboard
      ↓
Query Router
      ↓
Prompt + Relationship Engine
      ↓
SQL Generator
      ↓
Query Engine
      ↓
Visualization Engine
      ↓
Analytics Output
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/AnuragkGithub/Enterprise-Analytics-AI.git

cd Enterprise-Analytics-AI
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Backend

Start FastAPI server:

```bash
uvicorn backend.server:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Running Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

# Example User Queries

```text
Show top failing jobs

Analyze warehouse utilization trends

Show creator-wise runtime analysis

Compare workspace performance

Generate failure insights

Show runtime variance by pipeline
```

---

# Query Routing Example

```python
def route_question(question):

    if "runtime" in question:
        return "RUNTIME_ANALYSIS"

    elif "failure" in question:
        return "FAILURE_ANALYSIS"

    return "GENERAL_ANALYTICS"
```

---

# Sample SQL Generation

```sql
SELECT 
    creator,
    AVG(runtime) AS avg_runtime
FROM jobs
GROUP BY creator
ORDER BY avg_runtime DESC;
```

---

# Training Dataset Support

The platform supports:

- NL-to-SQL training
- Fine-tuning datasets
- Query variations
- Prompt engineering workflows

Files:

```text
nl_sql_pairs.json
fine_tuning_dataset.jsonl
question_variations.json
```

---

# Visualization Engine

The visualization engine dynamically selects charts based on:

- Query result shape
- Data type analysis
- Aggregation patterns
- Analytical context

---

# Screenshots

## Streamlit Dashboard

_Add dashboard screenshot here_

## Swagger API Docs

_Add Swagger screenshot here_

## Analytics Visualizations

_Add chart screenshots here_

---

# Future Enhancements

- OpenAI / Groq Integration
- RAG-Based Query Intelligence
- Vector Database Support
- Real-Time Streaming Analytics
- Multi-Database Connectivity
- Cloud Deployment
- Authentication & RBAC
- AI Agent Workflows
- Autonomous Analytics Generation

---

# Author

## Anurag Karmakar

- Python Developer
- AI & Analytics Enthusiast
- FastAPI + Streamlit Developer
- Data Engineering Explorer

---

# License

MIT License