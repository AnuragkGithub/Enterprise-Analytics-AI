import duckdb
import json

con = duckdb.connect("data/processed/database.duckdb")

with open("sql_queries/queries.json") as f:
    queries = json.load(f)

def run_query(query_id):

    if query_id not in queries:
        raise ValueError(f"Invalid query_id returned by LLM: {query_id}")

    sql = queries[query_id]["sql"]

    return con.execute(sql).df()