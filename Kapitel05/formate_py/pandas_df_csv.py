import pandas as pd

# 1. Lesen einer CSV-Datei
df = pd.read_csv("kunden.csv")

# 2. Transformation
df["Mitglied_jahre"] = 2025 - pd.to_datetime(df["Registriert_seit"]).dt.year
df_berlin = df[df["Wohnort"] == "Berlin"]

# 3. Speichern als Parquet
df_berlin.to_parquet("berliner_kunden.parquet")