# WordCount-Beispiel mit Hadoop MapReduce

Dieses Beispiel zeigt, wie mit Hadoop MapReduce Wortfrequenzen in Textdateien gezählt werden. Es ist das klassische "Hello World" für MapReduce.

## Beschreibung

Das Programm liest eine oder mehrere Textdateien und zählt, wie oft jedes Wort vorkommt. Es unterstützt auch fortgeschrittenere Features wie Sortierung und Partitionierung.

## Quellcode

- [WordCount.java](src/main/java/de/hsma/bdea/WordCount.java) — MapReduce-Job zum Zählen von Wortfrequenzen

## Bauen und Ausführen

Das Projekt nutzt Maven. Bauen mit:

```bash
mvn clean package
```

Ausführen mit (Anpassung der Pfade erforderlich):

```bash
java -cp target/word-count-1.0-SNAPSHOT.jar de.hsma.bdea.WordCount /path/to/input /path/to/output
```

## Weitere Informationen

Siehe auch das ausführliche Kapitel 13 im Buch für eine detaillierte Erklärung des MapReduce-Paradigmas.
