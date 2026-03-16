# Kapitel 11 - Object Stores / Data Lakehouse mit S3 und Delta Lake

Dieses Verzeichnis enthält Beispiele für die Arbeit mit Object Stores (S3-kompatibel) und Delta Lake als Data Lakehouse-Lösung. Alle Beispiele verwenden MinIO als lokale S3-Implementierung.

> **Hinweis:** Die freie Community Version von MinIO wurde Ende 2025 überraschenderweise in den Maintenance Mode versetzt. Mögliche populäre und freie Alternativen sind u. a. RustFS (\url{https://github.com/RustFS/RustFS}) oder SeaweedFS (\url{https://github.com/seaweedfs/seaweedfs}). Beide unterstützen ebenfalls die S3-Schnittstelle.


------------------------------------------------------------------------

## ⚡ Quick Start

Starten Sie MinIO mit Docker Compose:

```bash
    docker compose up -d
```

MinIO ist dann unter http://localhost:9001 erreichbar (Web-UI) und http://localhost:9000 (S3-API).

------------------------------------------------------------------------

## Voraussetzungen

Für dieses Kapitel benötigen Sie:

- **Docker** und **Docker Compose**
- **Python 3** mit den Paketen aus `pyproject.toml` (boto3, deltalake, pandas, pyarrow, duckdb)
- Grundkenntnisse der Kommandozeile

Falls Sie Docker noch nicht installiert haben:

https://docs.docker.com/get-docker/

------------------------------------------------------------------------

## Docker Compose Setup

Die `docker-compose.yml` konfiguriert einen MinIO-Server mit:

- **MinIO** - S3-kompatibler Objektspeicher
- Zugangsdaten: `minioadmin` / `minioadmin123`

------------------------------------------------------------------------

## Beispiele

### Delta Lakehouse erstellen und verwalten

- **[initial_delta_lakehouse.py](initial_delta_lakehouse.py)** - Erstellt eine Delta-Tabelle in MinIO mit Beispieldaten
- **[update_data_boto_client.py](update_data_boto_client.py)** - Aktualisiert Daten mit dem AWS Boto3 SDK
- **[update_data_minio_client.py](update_data_minio_client.py)** - Aktualisiert Daten mit dem MinIO SDK
- **[merge_delta_lakehouse.py](merge_delta_lakehouse.py)** - Fügt neue Daten in bestehende Delta-Tabelle ein (MERGE-Operation)
- **[timetravel_delta_lakehouse.py](timetravel_delta_lakehouse.py)** - Zeigt Time-Travel-Funktionalität von Delta Lake
- **[delete_delta_lakehouse.py](delete_delta_lakehouse.py)** - Löscht Daten aus der Delta-Tabelle

### S3-Datenanalyse mit DuckDB und Pandas

- **[pandas_s3_example.py](pandas_s3_example.py)** - Liest Parquet-Dateien direkt von S3 mit Pandas
- **[pandas_plot.py](pandas_plot.py)** - Visualisiert S3-Daten mit Pandas und Matplotlib
- **[duckdb_s3_example.py](duckdb_s3_example.py)** - Führt SQL-Abfragen direkt auf S3-Parquet-Dateien aus
- **[duckdb_s3_partitioning.py](duckdb_s3_partitioning.py)** - Nutzt Hive-Partitionierung für effiziente Abfragen

### Metadatenverwaltung

- **[update_data_boto_client_metadaten_tags.py](update_data_boto_client_metadaten_tags.py)** - Verwaltet User-Defined Metadata und S3 Object Tags

------------------------------------------------------------------------

## Partitionierung

Die Beispiele zeigen, wie Daten mit Hive-Partitionierung (`jahr=2025/monat=1/`) organisiert werden können. Dies ermöglicht effiziente Abfragen mit "Partition Pruning", bei dem nur relevante Dateien gelesen werden.

------------------------------------------------------------------------

## Container stoppen

Wenn Sie MinIO nicht mehr benötigen:

```bash
    docker compose down
```

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten (inklusive Volumes):

```bash
    docker compose down -v # kurz für --volumes
```

Danach können Sie MinIO erneut starten.

------------------------------------------------------------------------

## Weitere Informationen

- [Delta Lake Dokumentation](https://delta.io)
- [MinIO Dokumentation](https://min.io/docs)
- [DuckDB S3 Import](https://duckdb.org/docs/stable/guides/network_cloud_storage/s3_import.html)

---

*Letzte Aktualisierung: 14. März 2026*