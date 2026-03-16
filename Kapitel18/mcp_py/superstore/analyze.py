import pandas as pd

# CSV laden
df = pd.read_csv("superstore.csv", parse_dates=["Order Date"])

# Gesamtumsatz und -profit je Jahr berechnen
df["Year"] = df["Order Date"].dt.year
yearly = df.groupby("Year")[["Sales","Profit"]].sum().reset_index()

print(yearly)