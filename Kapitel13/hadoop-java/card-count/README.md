# CardCount-Beispiel mit Hadoop MapReduce

Dieses Beispiel zeigt, wie mit Hadoop MapReduce Kartenfarben gezählt werden. Es ist das klassische "Hello World" für MapReduce.

## Beschreibung

Das Programm liest eine Textdatei mit Karteninformationen (z.B. "Pik Ass", "Karo Dame") und zählt, wie oft jede Farbe (Kreuz, Pik, Herz, Karo) vorkommt.

## Quellcode

- [CardGenerator.java](src/main/java/de/hsma/bdea/CardGenerator.java) — Erzeugt eine Testdatei mit zufälligen Karten
- [CardCount.java](src/main/java/de/hsma/bdea/CardCount.java) — MapReduce-Job zum Zählen der Kartenfarben

## Bauen und Ausführen

Das Projekt nutzt Maven. Bauen mit:

```bash
mvn clean package
```

Ausführen mit (Anpassung der Pfade erforderlich):

```bash
java -cp target/card-count-1.0-SNAPSHOT.jar de.hsma.bdea.CardCount /path/to/input /path/to/output
```

## Weitere Informationen

Siehe auch das ausführliche Kapitel 13 im Buch für eine detaillierte Erklärung des MapReduce-Paradigmas.
