from deltalake import DeltaTable

# Die Storage-Optionen für MinIO bleiben identisch.
storage_options = {
    "AWS_ENDPOINT_URL": 'http://localhost:9000',
    "AWS_ACCESS_KEY_ID": 'minioadmin',
    "AWS_SECRET_ACCESS_KEY": 'minioadmin123',
    "AWS_ALLOW_HTTP": 'true' # In deltalake wird dies als String erwartet
}

# 1. Reise zurück in der Zeit zur Version 0 (vor dem MERGE)
delta_table_path = 's3://datalakehouse/sales_delta/'
# Initiale Version
delta_table_v0_df = DeltaTable(delta_table_path,
    version=0,  # Spezifische Version
    storage_options=storage_options
).to_pandas()
# Momentane Version (nach dem MERGE)
delta_table_latest_df = DeltaTable(delta_table_path,
    storage_options=storage_options
).to_pandas()

print(f"Anzahl Zeilen in der aktuellen Version: {len(delta_table_latest_df)}")
print(f"Anzahl Zeilen in Version 0: {len(delta_table_v0_df)}")