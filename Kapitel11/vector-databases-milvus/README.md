# Kapitel 11 (NoSQL) -- Vektordatenbanken: Milvus

In diesem Kapitel lernen Sie die grundlegenden Konzepte von Vektordatenbanken anhand von Milvus kennen. Milvus ist spezialisiert auf die Speicherung und Suche von Vektoren, was besonders für maschinelles Lernen und semantische Suche relevant ist.

------------------------------------------------------------------------

## Quick Start

Starten Sie Milvus mit Docker Compose:

    cd vector-databases-milvus
    docker compose up -d

Verbinden Sie sich mit der Milvus-Instanz (Port 19530):

    python -c "from pymilvus import MilvusClient; client = MilvusClient(uri='http://localhost:19530'); print('Connected:', client)"

------------------------------------------------------------------------

## Voraussetzungen

Für dieses Kapitel benötigen Sie:

- **Docker** und **Docker Compose**
- **Python 3** mit den Paketen `pymilvus` und `datasets`
- Grundkenntnisse der Kommandozeile

Falls Sie Docker noch nicht installiert haben:

https://docs.docker.com/get-docker/

------------------------------------------------------------------------

## Docker Compose Setup

Die `docker-compose.yml` konfiguriert eine Milvus-Standalone-Instanz mit:

- **etcd** - für Metadaten-Management
- **MinIO** - als Objektspeicher für Milvus
- **Milvus** - die eigentliche Vektordatenbank

------------------------------------------------------------------------

## Beispiele aus dem Buch ausführen

Das Beispiel im Jupyter Notebook `Text_Search_With_Milvus.ipynb` demonstriert:

1. Laden eines Wikipedia-Datensatzes aus dem HuggingFace-Datasets
2. Erstellen einer Collection mit Schema (ID, URL, Titel, Text, Embedding-Vektor)
3. Indexierung der Vektoren für schnelle Suche
4. Semantische Suche über die gespeicherten Texte

Führen Sie das Notebook aus:

    jupyter notebook Text_Search_With_Milvus.ipynb

------------------------------------------------------------------------

## Container stoppen

Wenn Sie Milvus nicht mehr benötigen:

    docker compose down

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker compose down -v

Danach können Sie Milvus erneut starten.

------------------------------------------------------------------------

## Weitere Informationen

- [Milvus Dokumentation](https://milvus.io/docs)
- [PyMilvus API Reference](https://pymilvus.readthedocs.io)
