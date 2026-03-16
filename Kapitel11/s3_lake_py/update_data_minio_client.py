import pandas as pd
import numpy as np
from minio import Minio
from io import BytesIO

# 1. MinIO Client initialisieren
minio_client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin123",
    secure=False
)

# 2. Bucket erstellen (falls nicht vorhanden)
bucket_name = "datalake"
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' erstellt.")

# 3. Beispieldaten für ein fiktives E-Commerce-Unternehmen generieren
np.random.seed(42)
df = pd.DataFrame({
    'kunde_id': range(1, 10001),
    'umsatz': np.random.normal(1000, 300, 10000).round(2),
    'produkt': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'Monitor'], 10000),
    'region': np.random.choice(['Nord', 'Süd', 'Ost', 'West'], 10000),
    'datum': pd.to_datetime(pd.date_range('2025-01-01', periods=10000, freq='h'))
})

# 4. Daten in-memory in das Parquet-Format konvertieren
# BytesIO erstellt einen binären Puffer im Arbeitsspeicher, der sich wie eine Datei verhält.
buffer = BytesIO()
df.to_parquet(buffer, engine='pyarrow')
buffer.seek(0) # Zurück zum Anfang des Puffers springen, um ihn lesen zu können.

# 5. Datei (als Objekt) in MinIO hochladen
object_name = "sales/raw/2025/sales_data_full.parquet"
minio_client.put_object(
    bucket_name,
    object_name,
    buffer,
    length=buffer.getbuffer().nbytes,
    content_type='application/octet-stream' # Generischer Typ für Binärdaten
)
print(f"Datei erfolgreich hochgeladen: s3://{bucket_name}/{object_name}")