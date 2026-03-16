import pandas as pd

# Gesamte Datei als JSON-Liste laden
df1 = pd.read_json("daten.json")
print(df1)

# JSON Lines Laden: lines=True
df2 = pd.read_json("daten.jsonl", lines=True)
print(df2)
