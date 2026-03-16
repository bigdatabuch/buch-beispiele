# Spark Java Beispiele

Dieses Verzeichnis enthält Spark-Beispiele in Java.

## Beschreibung

Diese Beispiele zeigen, wie Spark mit Java genutzt werden kann. Sie sind die Java-Entsprechung der Python-Notebooks in `../spark/`.

## Quellcode

- [PiExampleModern.java](src/main/java/de/th_mannheim/informatik/big_data/PiExampleModern.java) — Berechnung von Pi mit Spark

## Bauen und Ausführen

Das Projekt nutzt Maven. Bauen mit:

```bash
mvn clean package
```

Ausführen mit:

```bash
mvn exec:java -Dexec.mainClass="de.th_mannheim.informatik.big_data.PiExampleModern"
```

## Weitere Informationen

Siehe auch die Python-Notebooks in `../spark/` für vergleichbare Beispiele.
