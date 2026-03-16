import duckdb
conn = duckdb.connect()
conn.execute("""
    SET s3_region='us-east-1';
    SET s3_endpoint='localhost:9000';
    SET s3_access_key_id='minioadmin';
    SET s3_secret_access_key='minioadmin123';
    SET s3_use_ssl=false;
    SET s3_url_style='path';
""")

# Abfrage auf den PARTITIONIERTEN Daten.
# DuckDB erkennt die /jahr=.../monat=... Struktur ('Hive-Partitioning')
# und wendet den WHERE-Filter bereits auf die Dateipfade an.
# So wird NUR die Parquet-Datei für Februar 2025 gelesen!
partitioned_query = """
    SELECT 
        produkt,
        SUM(umsatz) as monatsumsatz
    FROM 's3://datalake/sales/partitioned/**/*.parquet' -- Lesen aus partitioniertem Pfad
    WHERE jahr = 2025 AND monat = 2 -- Filter auf Partitions-Spalten
    GROUP BY produkt
    ORDER BY monatsumsatz DESC;
"""
feb_result = conn.execute(partitioned_query).fetchdf()

print("\n--- Analyse der partitionierten Daten (nur Februar 2025) ---")
print(feb_result)
conn.close()