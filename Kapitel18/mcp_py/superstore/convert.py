import pandas as pd
import sqlite3

df = pd.read_csv("superstore.csv")
conn = sqlite3.connect("superstore.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()