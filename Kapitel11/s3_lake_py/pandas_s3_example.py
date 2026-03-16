import pandas as pd

# 1. Daten aus dem "raw" Bereich unseres Data Lakes lesen
# Wir verwenden den gleichen S3-Pfad wie zuvor mit DuckDB
s3_path_raw = 's3://datalake/sales/raw/2025/sales_data_full.parquet'
storage_options = {
    "endpoint_url": 'http://localhost:9000',
    "key": 'minioadmin',
    "secret": 'minioadmin123',
}
df = pd.read_parquet(s3_path_raw, storage_options=storage_options)

# 2. Partitions-Spalten Hinzufügen
# Wir extrahieren Jahr und Monat aus der Datumsspalte
df['jahr'] = df['datum'].dt.year
df['monat'] = df['datum'].dt.month

# 3. Daten partitioniert zurück in den Data Lake schreiben
# Pandas und PyArrow erstellen automatisch eine Ordnerstruktur basierend auf den Werten
# in den `partition_cols`.
# Z.B.: .../jahr=2025/monat=1/....parquet
s3_path_partitioned = 's3://datalake/sales/partitioned/'
df.to_parquet(
    s3_path_partitioned,
    partition_cols=['jahr', 'monat'],
    storage_options=storage_options,
    engine='pyarrow'
)
print(f"Daten partitioniert nach '{s3_path_partitioned}' geschrieben.")