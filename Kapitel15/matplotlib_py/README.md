# Kapitel 15: Python (Matplotlib/Seaborn) und Echtzeitmonitoring

Dieses Verzeichnis enthält Beispiele für die Big-Data-Visualisierung mit Python.

## Beispiele

### 1. Liniendiagramm mit pandas und matplotlib

Das Skript `plot.py` zeigt, wie man mit `pandas` und `matplotlib` ein Liniendiagramm für tägliche Verkaufszahlen erstellt.

**Voraussetzungen:**
```bash
pip install pandas matplotlib
```

**Ausführen:**
```bash
python plot.py
```

Das Skript erstellt ein Liniendiagramm mit Datenpunkten, das die täglichen Verkäufe im November 2023 zeigt.

### 2. Echtzeit-Monitoring-Setup

Das Verzeichnis enthält ein vollständiges Setup für Echtzeit-Monitoring mit:

- **OpenSearch** – Speicherung und Indexierung der Metriken
- **OpenSearch Dashboards** – Visualisierung der Log- und Eventdaten
- **Grafana** – universelles Dashboard-Frontend für Zeitreihendaten

**Starten der Infrastruktur:**
```bash
docker compose up -d
```

Anschließend können Sie:
- OpenSearch Dashboards unter `http://localhost:5601` aufrufen
- Grafana unter `http://localhost:3000` konfigurieren (Datenquelle: OpenSearch)

### 3. Simulation von Echtzeit-Metriken

Das Skript `simulation.py` simuliert kontinuierlich Systemmetriken (CPU- und RAM-Auslastung) und schreibt sie in OpenSearch.

**Voraussetzungen:**
```bash
pip install opensearch-py
```

**Ausführen:**
```bash
python simulation.py
```

Das Skript schreibt jede Sekunde neue Metriken in den Index `system-metrics`.

## Weitere Informationen

Weitere Details zu den verwendeten Technologien finden Sie im Buch.