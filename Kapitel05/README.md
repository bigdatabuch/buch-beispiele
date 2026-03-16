# Kapitel 5: Datenformate - Code-Beispiele

Dieses Verzeichnis enthält Python-Beispiele für die Arbeit mit verschiedenen Datenformaten im Kontext von Big Data. Die Beispiele illustrieren die Konzepte aus Kapitel 5 ("Datenformate") des Big Data-Buchs.

## Übersicht der Beispiele

| Beispiel | Format | Beschreibung |
|----------|--------|--------------|
| [`pandas_df_csv.py`](#pandas_df_csvpy) | CSV → Parquet | Pandas-DataFrame mit CSV-Daten erstellen und als Parquet speichern |
| [`pandas_df_json.py`](#pandas_df_jsonpy) | JSON / JSONL | Lesen von JSON-Listen und JSON Lines (JSONL) mit Pandas |
| [`arrow_format.py`](#arrow_formatpy) | Parquet (Arrow) | Arrow-Tabelle erstellen und als Parquet-Datei speichern |
| [`avro_format.py`](#avro_formatpy) | Avro | Daten mit Avro-Schema serialisieren und deserialisieren |
| [`spark_verkaufsdaten.py`](#spark_verkaufsdatenpy) | CSV → Parquet (Spark) | Spark-DataFrame mit automatischer Schema-Inferenz |
| [`spark_verkaufsdaten_schema.py`](#spark_verkaufsdaten_schemapy) | CSV → Parquet (Spark) | Spark-DataFrame mit explizit definiertem Schema |

---

## Einzelne Beispiele

### [`pandas_df_csv.py`](formate_py/pandas_df_csv.py)

**Zweck:** Einfache Datenverarbeitung mit Pandas - CSV lesen, transformieren und als Parquet speichern.

**Was zeigt es:**
- Lesen einer CSV-Datei mit `pd.read_csv()`
- Datenfilterung und -transformation (Spalte berechnen)
- Speichern als Parquet mit `df.to_parquet()`

**Datenquelle:** [`kunden.csv`](formate_py/kunden.csv)

```python
# CSV lesen → Transformieren → Parquet speichern
df = pd.read_csv("kunden.csv")
df["Mitglied_jahre"] = 2025 - pd.to_datetime(df["Registriert_seit"]).dt.year
df_berlin = df[df["Wohnort"] == "Berlin"]
df_berlin.to_parquet("berliner_kunden.parquet")
```

---

### [`pandas_df_json.py`](formate_py/pandas_df_json.py)

**Zweck:** Unterschiedliche JSON-Formate mit Pandas verarbeiten.

**Was zeigt es:**
- Lesen einer JSON-Liste mit `pd.read_json()`
- Lesen von JSON Lines (JSONL) mit `lines=True`

**Datenquellen:** 
- [`daten.json`](formate_py/daten.json) - JSON-Liste
- [`daten.jsonl`](formate_py/daten.jsonl) - JSON Lines Format

```python
# JSON-Liste laden
df1 = pd.read_json("daten.json")

# JSON Lines laden
df2 = pd.read_json("daten.jsonl", lines=True)
```

---

### [`arrow_format.py`](formate_py/arrow_format.py)

**Zweck:** Arrow-Tabelle mit PyArrow erstellen und als Parquet speichern.

**Was zeigt es:**
- Erstellen einer PyArrow-Tabelle aus Dictionary
- Speichern mit `pq.write_table()`
- Laden mit `pq.read_table()` und Konvertierung zu Pandas DataFrame

**Ergebnis:** Erzeugt die Datei `kunden_arrow.parquet`

```python
# Arrow-Tabelle erstellen
data = {"Kunden_ID": [101, 102, 103], "Name": ["Meier", "Huber", "Schmidt"], ...}
table = pa.table(data)

# Als Parquet speichern
pq.write_table(table, "kunden_arrow.parquet")
```

---

### [`avro_format.py`](formate_py/avro_format.py)

**Zweck:** Daten mit Apache Avro serialisieren und deserialisieren.

**Was zeigt es:**
- Definieren eines Avro-Schemas (JSON-basiert)
- Schreiben mit `DataFileWriter`
- Lesen mit `DataFileReader`
- Verwendung von `logicalType` für Datumswerte

**Ergebnis:** Erzeugt die Datei `kunden.avro`

```python
# Schema definieren
schema_json = '''{
    "type": "record",
    "name": "Kunde",
    "fields": [
        {"name": "Kunden_ID", "type": "int"},
        {"name": "Registriert_seit", "type": {"type": "int", "logicalType": "date"}}
    ]
}'''

# Daten schreiben und lesen
with open('kunden.avro', 'wb') as f:
    writer = DataFileWriter(f, DatumWriter(), schema)
    writer.append(kunde)
```

---

### [`spark_verkaufsdaten.py`](formate_py/spark_verkaufsdaten.py)

**Zweck:** Spark-DataFrame aus CSV mit automatischer Schema-Inferenz erstellen.

**Was zeigt es:**
- SparkSession initialisieren
- CSV mit `inferSchema=True` lesen (automatische Typerkennung)
- Speichern als Parquet

**Datenquelle:** [`verkaufsdaten.csv`](formate_py/verkaufsdaten.csv)

**Achtung:** Für große Dateien ist `inferSchema` nicht empfohlen (siehe Kommentar im Code).

```python
spark = SparkSession.builder.appName("DataConversion").getOrCreate()

df_sales = spark.read.csv(
    "verkaufsdaten.csv",
    header=True,
    inferSchema=True  # Automatische Schema-Erkennung
)

df_sales.write.mode("overwrite").parquet("verkaufsdaten.parquet")
```

---

### [`spark_verkaufsdaten_schema.py`](formate_py/spark_verkaufsdaten_schema.py)

**Zweck:** Spark-DataFrame aus CSV mit explizit definiertem Schema erstellen.

**Was zeigt es:**
- Definieren eines Schemas mit `StructType` und `StructField`
- Explizite Typzuweisung (`IntegerType`, `StringType`, `DoubleType`)
- Bessere Performance und Kontrolle gegenüber `inferSchema`

**Datenquelle:** [`verkaufsdaten.csv`](formate_py/verkaufsdaten.csv)

**Empfehlung:** Dieser Ansatz ist für Produktionssysteme vorzuziehen.

```python
schema = StructType([
    StructField("KundenID", IntegerType(), True),
    StructField("AuftragID", StringType(), True),
    StructField("Produkt", StringType(), True),
    StructField("Preis", DoubleType(), True),
])

df_sales = spark.read.csv(
    "verkaufsdaten.csv",
    header=True,
    schema=schema  # Explizites Schema
)
```

---

## Ausführliche Informationen

Weitere Informationen zu den vorgestellten Datenformaten (CSV, JSON, Parquet, Avro) und den verwendeten Frameworks (Pandas, PyArrow, Spark) finden Sie in **Kapitel 5 "Datenformate"** des Big Data-Buchs.

---

## Voraussetzungen

Die Beispiele erfordern Python mit folgenden Paketen (siehe [`pyproject.toml`](formate_py/pyproject.toml)):

- avro>=1.12.0
- pandas>=2.3.2
- pyarrow>=21.0.0
- pyspark>=4.0.1

---

*Letzte Aktualisierung: 14. März 2026*