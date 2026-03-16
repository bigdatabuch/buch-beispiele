# Spark Streaming Tutorial

Dieses Tutorial zeigt, wie mit Spark Structured Streaming kontinuierliche Datenströme verarbeitet werden können. Als Beispiel dient ein Coffee-Shop, der Bestellungen in Echtzeit verarbeitet.

## Beschreibung

Das Beispiel simuliert kontinuierliche Bestellungen und verarbeitet diese in 5-Minuten-Fenstern. Es zeigt typische Streaming-Operationen wie Watermarks, Deduplikation und Aggregation.

## Quellcode

- [generate_orders.py](generate_orders.py) — Simuliert Bestellungen und schreibt sie als JSON-Dateien
- [stream_orders.py](spark/stream_orders.py) — Verarbeitet die Bestellungen mit Spark Structured Streaming

## Docker Compose Setup

Das Tutorial nutzt Docker Compose für eine einfache Einrichtung:

```bash
docker-compose up -d
```

Dann die Daten-Generierung starten:

```bash
docker-compose exec app python generate_orders.py
```

Und schließlich die Stream-Verarbeitung starten:

```bash
docker-compose exec app python spark/stream_orders.py
```

## Weitere Informationen

Siehe auch das ausführliche Kapitel 13 im Buch für eine detaillierte Erklärung des Streaming-Paradigmas.
