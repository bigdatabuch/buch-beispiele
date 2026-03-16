# Kapitel 15: Datenanalyse und Visualisierung

Dieses Kapitel behandelt Techniken und Werkzeuge für die Big-Data-Visualisierung, von klassischen Diagrammen bis hin zu interaktiven Dashboards und Echtzeit-Monitoring.

## Übersicht der Code-Beispiele

### Python (Matplotlib/Seaborn/Echtzeitmonitoring OpenSearch+Grafana)

- **[plot.py](matplotlib_py/plot.py)** – Erstellung eines Liniendiagramms mit täglichen Verkaufszahlen
  - Verwendung von `pandas` für Data Frames und `matplotlib.pyplot` für die Visualisierung
  - Imperativer Ansatz mit Matplotlib
  - [Weitere Details in der README](matplotlib_py/README.md)

- **[simulation.py](matplotlib_py/simulation.py)** – Simulation von Echtzeit-Systemmetriken (CPU- und RAM-Auslastung) für Monitoring-Szenarien
  - Schreibt kontinuierlich Metriken in OpenSearch
  - Echtzeit-Datenstrom mit 1 Sekunde Intervall
  - [Weitere Details in der README](matplotlib_py/README.md)

### R (ggplot2)

- **[plot.R](ggplot2_R/plot.R)** – Erstellung eines Liniendiagramms mit täglichen Verkaufszahlen
  - Verwendung von `ggplot2` für deklarative Visualisierung
  - Speichert das Diagramm als PNG-Datei
  - [Weitere Details in der README](ggplot2_R/README.md)

## Echtzeit-Monitoring-Setup

Das Verzeichnis `matplotlib_py/` enthält ein vollständiges Setup für Echtzeit-Monitoring mit:

- **OpenSearch** – Speicherung und Indexierung der Metriken
- **OpenSearch Dashboards** – Visualisierung der Log- und Eventdaten
- **Grafana** – universelles Dashboard-Frontend für Zeitreihendaten

### Starten der Infrastruktur

```bash
cd matplotlib_py
docker compose up -d
```

Anschließend können Sie:
- OpenSearch Dashboards unter `http://localhost:5601` aufrufen
- Grafana unter `http://localhost:3000` konfigurieren (Datenquelle: OpenSearch)

## Weitere Informationen

Weitere Details zu den verwendeten Technologien und Strategien finden Sie im Kapitel.

---

*Letzte Aktualisierung: 14. März 2026*