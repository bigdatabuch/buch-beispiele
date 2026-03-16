# Apache Ignite mit Python Thin Client

Python Thin Client für Apache Ignite.

## Was gemacht wird
- Verbindung zu einem laufenden Apache Ignite Java-Cluster herstellen
- Auf Caches zugreifen (z. B. `sensorCacheSql`)
- SQL-Abfragen über den Thin Client ausführen

## Wie es genutzt wird
1. Zuerst den Java-Ignite-Cluster starten (siehe `IgniteSensorPythonThinClient.java` in `ignite-java`)
2. Python-Abhängigkeiten installieren: `pip install pyignite` (siehe `pyproject.toml`)
3. Skript ausführen: `python thinclient.py`

Das Beispiel zeigt eine SQL-Abfrage zur Berechnung des Durchschnitts der Temperaturen für eine bestimmte Stadt (hier: Mannheim).

