import duckdb

# DuckDB-Verbindung herstellen
conn = duckdb.connect()

# DuckDB mitteilen, wie es sich mit unserem lokalen S3 (MinIO) verbinden soll
conn.execute("""
    SET s3_region='us-east-1';
    SET s3_endpoint='localhost:9000';
    SET s3_access_key_id='minioadmin';
    SET s3_secret_access_key='minioadmin123';
    SET s3_use_ssl=false;
    SET s3_url_style='path';
""")

# SQL-Abfrage direkt auf dem S3-Objekt ausführen
# Beachten Sie, wie der S3-Pfad direkt in der FROM-Klausel verwendet wird!
query = """
    SELECT 
        region,
        produkt,
        COUNT(*) as anzahl_verkaufe,
        ROUND(AVG(umsatz), 2) as avg_umsatz
    FROM 's3://datalake/sales/raw/2025/sales_data_full.parquet'
    GROUP BY ALL
    ORDER BY region, produkt
"""
result_df = conn.execute(query).fetchdf()

print("--- DuckDB Analyse direkt von S3 ---")
print(result_df)
conn.close()