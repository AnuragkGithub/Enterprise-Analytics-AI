import duckdb
import json

con = duckdb.connect(
    "data/processed/database.duckdb",
    read_only=True
)

with open("sql_queries/queries.json") as f:
    queries = json.load(f)

def run_query(query_id):

    sql = queries[query_id]["sql"]

    return con.execute(sql).df()