import duckdb
import pandas as pd
import os

con = duckdb.connect("data/processed/database.duckdb")

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        table = file.replace(".csv","")
        df = pd.read_csv(os.path.join(folder,file))
        con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM df")

print("All tables loaded successfully")