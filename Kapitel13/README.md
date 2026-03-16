# Kapitel 13: Verarbeitungsparadigmen

Dieses Kapitel behandelt verschiedene Frameworks zur verteilten Datenverarbeitung, darunter Hadoop MapReduce, Apache Spark, Apache Flink und Apache Ignite.

## Übersicht

| Framework | Paradigma | Sprache | Beschreibung |
|-----------|-----------|---------|--------------|
| [Hadoop](./hadoop-java/) | Batch | Java | Klassische MapReduce-Verarbeitung großer Datenmengen |
| [Spark](./spark/) | Batch/Streaming | Python/Java | Schnelle, in-Memory-Verarbeitung mit RDDs, DataFrames und MLlib |
| [Spark (Java)](./spark-java/) | Batch/Streaming | Java | Spark-Beispiele in Java |
| [Spark Streaming](./spark-streaming-tutorial/) | Streaming | Python | Echtzeit-Verarbeitung mit Structured Streaming |
| [Flink](./flink-java/) | Streaming | Java | Echtzeit-Stream-Verarbeitung |
| [Ignite (Java)](./ignite-java/) | Batch/Streaming | Java | In-Memory-Datenbank mit SQL-Unterstützung |
| [Ignite (Python)](./ignite-py/) | Batch/Streaming | Python | Python Thin Client für Apache Ignite |

## Hadoop MapReduce

Hadoop MapReduce ist das klassische Framework für die Batch-Verarbeitung großer Datenmengen. Es basiert auf dem MapReduce-Paradigma, bei dem Daten in der Map-Phase transformiert und in der Reduce-Phase aggregiert werden.

- [CardCount-Beispiel](./hadoop-java/card-count/) — Zählen von Kartenfarben
- [WordCount-Beispiel](./hadoop-java/word-count/) — Zählen von Wortfrequenzen

## Apache Spark

Spark ist ein schnelles Framework für die verteilte Datenverarbeitung, das sowohl Batch- als auch Streaming-Verarbeitung unterstützt. Es bietet APIs für Java, Python (PySpark) und R.

- [Spark Notebooks (Python)](./spark/) — Einführung in RDDs, DataFrames und MLlib mit PySpark
- [Spark Notebooks (Python)](./spark-python/) — Identische Beispiele wie oben
- [Spark Java Beispiele](./spark-java/) — Spark-Implementierungen in Java

## Apache Spark Streaming

Structured Streaming ist Spark's kontinuierliche Stream-Verarbeitungs-Engine.

- [Spark Streaming Tutorial](./spark-streaming-tutorial/) — Coffee-Shop Bestell-Streaming mit Docker Compose

## Apache Flink

Flink ist ein Framework für die Echtzeit-Stream-Verarbeitung mit niedriger Latenz.

- [Flink Java Beispiele](./flink-java/) — SocketWordCount mit Docker Compose

## Apache Ignite

Ignite ist eine In-Memory-Datenbank mit SQL-Unterstützung und verteiltem Computing.

- [Ignite Java Beispiele](./ignite-java/) — Sensor-Datenverarbeitung mit SQL und Affinity Keys
- [Ignite Python Thin Client](./ignite-py/) — Python-Client für Ignite

## Notebooks

Die Spark-Notebooks (`.ipynb`) bieten interaktive Einführungen in die jeweiligen Themen und können mit Google Colab oder lokal mit PySpark ausgeführt werden.

---

*Letzte Aktualisierung: 14. März 2026*