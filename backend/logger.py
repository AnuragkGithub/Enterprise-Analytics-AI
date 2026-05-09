import json
from datetime import datetime

LOG_FILE = "logs/query_logs.json"

def log_query(question, query_id, result):

    log = {
        "timestamp": str(datetime.now()),
        "question": question,
        "query_id": query_id,
        "rows_returned": len(result)
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log) + "\n")