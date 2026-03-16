import pandas as pd
from deltalake import DeltaTable

# Die Storage-Optionen für MinIO bleiben identisch.
storage_options = {
    "AWS_ENDPOINT_URL": 'http://localhost:9000',
    "AWS_ACCESS_KEY_ID": 'minioadmin',
    "AWS_SECRET_ACCESS_KEY": 'minioadmin123',
    "AWS_ALLOW_HTTP": 'true' # In deltalake wird dies als String erwartet
}

# 1. Beispieldaten für den Merge-Vorgang erstellen
# Ein neuer Verkauf (kunde_id 10001) und eine Korrektur für Kunde 25
# Annahme: Die Korrektur spiegelt die initialen Verkausdaten wieder (d.h. ein SQL Join mit kunde_id und datum gelingt)
updates_df = pd.DataFrame({
    'kunde_id': [10001, 25],
    'umsatz': [199.99, 1150.00], # Neuer Verkauf und korrigierter Umsatz
    'produkt': ['Zubehör', 'Smartphone'],
    'region': ['Nord', 'West'],
    'datum': pd.to_datetime(['2025-02-15 10:00:00', '2025-01-01 02:00:00'])
})

# 2. Bestehende Delta-Tabelle öffnen
delta_table_path = 's3://datalakehouse/sales_delta/'
delta_table = DeltaTable(delta_table_path, storage_options=storage_options)

# 3. MERGE-Operation ausführen
# Dies ist eine deklarative, SQL-ähnliche Anweisung.
delta_table.merge(
    source=updates_df,
    predicate='source.kunde_id = target.kunde_id AND source.datum = target.datum',
    source_alias='source',
    target_alias='target'
).when_matched_update_all().when_not_matched_insert_all().execute()

print("MERGE-Operation erfolgreich abgeschlossen.")
print(f"Aktuelle Version der Tabelle: {delta_table.version()}")