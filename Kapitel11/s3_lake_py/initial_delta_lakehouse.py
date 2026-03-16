import boto3
import numpy as np
import pandas as pd
from botocore.config import Config
from deltalake.writer import write_deltalake

# 1. Beispieldaten für ein fiktives E-Commerce-Unternehmen generieren
np.random.seed(42)
df = pd.DataFrame({
    'kunde_id': range(1, 10001),
    'umsatz': np.random.normal(1000, 300, 10000).round(2),
    'produkt': np.random.choice(['Laptop', 'Smartphone', 'Tablet', 'Monitor'], 10000),
    'region': np.random.choice(['Nord', 'Süd', 'Ost', 'West'], 10000),
    'datum': pd.to_datetime(pd.date_range('2025-01-01', periods=10000, freq='h'))
})

# 2. Die Storage-Optionen für MinIO bleiben identisch.
storage_options = {
    "AWS_ENDPOINT_URL": 'http://localhost:9000',
    "AWS_ACCESS_KEY_ID": 'minioadmin',
    "AWS_SECRET_ACCESS_KEY": 'minioadmin123',
    "AWS_ALLOW_HTTP": 'true' # In deltalake wird dies als String erwartet
}

# S3-Client konfigurieren (boto3 - offizieller AWS SDK)
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin123',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# 3. Bucket erstellen (falls nicht vorhanden)
bucket_name = "datalakehouse"
try:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' erstellt")
except s3_client.exceptions.BucketAlreadyExists:
    print(f"Bucket '{bucket_name}' existiert bereits")
except s3_client.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket '{bucket_name}' gehoert bereits Ihnen")

# Daten in eine neue Delta-Tabelle schreiben
delta_table_path = 's3://datalakehouse/sales_delta/'
write_deltalake(
    delta_table_path,
    df,
    mode='overwrite', # 'overwrite' ersetzt die Tabelle, 'append' fügt hinzu
    storage_options=storage_options
)

print(f"Daten erfolgreich als Delta-Tabelle nach '{delta_table_path}' geschrieben.")