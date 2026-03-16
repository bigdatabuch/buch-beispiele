import pandas as pd
import numpy as np
import boto3
from io import BytesIO
from botocore.client import Config

# 1. S3-Client konfigurieren (boto3 - offizieller AWS SDK)
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin123',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# 2. Bucket erstellen (falls nicht vorhanden)
bucket_name = "datalake"
try:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' erstellt")
except s3_client.exceptions.BucketAlreadyExists:
    print(f"Bucket '{bucket_name}' existiert bereits")
except s3_client.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' gehoert bereits Ihnen")

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
object_key = "sales/raw/2025/sales_data_full.parquet"
s3_client.put_object(
    Bucket=bucket_name,
    Key=object_key,
    Body=buffer,
    ContentType='application/octet-stream'
)

# Metadaten des hochgeladenen Objekts abrufen
response = s3_client.head_object(
    Bucket=bucket_name,
    Key=object_key
)

print(f"Datei erfolgreich hochgeladen: s3://{bucket_name}/{object_key}")