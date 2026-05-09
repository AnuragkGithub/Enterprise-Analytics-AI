from fastapi import FastAPI
from backend.llm_router import detect_query
from backend.query_engine import run_query
from backend.logger import log_query

app = FastAPI()

@app.post("/ask")

def ask_question(payload: dict):

    question = payload["question"]

    query_id = detect_query(question)

    result = run_query(query_id)

    log_query(question, query_id, result)

    return {
        "query_id": query_id,
        "data": result.to_dict()
    }