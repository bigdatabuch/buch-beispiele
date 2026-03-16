import pyarrow as pa
import pyarrow.parquet as pq

# 1. Arrow-Tabelle erstellen
data = {
    "Kunden_ID": [101, 102, 103],
    "Name": ["Meier", "Huber", "Schmidt"],
    "Wohnort": ["Berlin", "Muenchen", "Hamburg"]
}
table = pa.table(data)

# 2. Arrow-Tabelle als Parquet-Datei speichern
pq.write_table(table, "kunden_arrow.parquet")

# 3. Parquet-Datei laden und als Pandas DataFrame anzeigen
table_read = pq.read_table("kunden_arrow.parquet")
df = table_read.to_pandas()

print(df)