from opensearchpy import OpenSearch
from datetime import datetime, timezone
import random, time

# Verbindung zu einer laufenden OpenSearch-Instanz (lokal)
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}]
)
print("Schreibe kontinuierlich Systemmetriken in den Index 'system-metrics'...")

while True:
    doc = {
        "timestamp": datetime.now(timezone.utc), # OpenSearch erkennt Datumstyp automatisch
        "cpu_usage_percent": random.randint(10, 90),
        "memory_usage_mb": random.randint(1000, 8000)
    }
    # Dokument in den Index schreiben
    client.index(index="system-metrics", body=doc)
    print(f"Eintrag gespeichert: CPU={doc['cpu_usage_percent']}%, RAM={doc['memory_usage_mb']}MB")
    time.sleep(1) # alle 1 Sekunde ein neuer Wert