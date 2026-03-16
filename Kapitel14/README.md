# Kapitel 14: Skalierbare Algorithmen und Datenstrukturen

Dieses Kapitel behandelt probabilistische Algorithmen und Datenstrukturen für die Verarbeitung großer Datenmengen. Diese Ansätze ermöglichen es, mit begrenztem Speicherplatz Näherungslösungen für Zähl-, Mengen- und Verteilungsprobleme zu berechnen.

## Übersicht der Algorithmen

| Algorithmus | Datei | Beschreibung | Komplexität |
|-------------|-------|--------------|-------------|
| **Morris-Counter** | [MorrisCounter.java](src/MorrisCounter.java) | Zählt große Zahlen mit weniger Bits durch probabilistisches Zählen | O(log log n) Bits |
| **HyperLogLog** | [HyperLogLogExample.java](src/HyperLogLogExample.java) | Schätzt die Kardinalität (Anzahl eindeutiger Elemente) großer Mengen | O(1) Speicher |
| **Bloom-Filter** | [BloomFilterExample.java](src/BloomFilterExample.java) | Testet Mengenzugehörigkeit mit möglichen falsch-positiven Ergebnissen | O(n) Speicher |
| **t-digest** | [TDigestExample.java](src/TDigestExample.java) | Schätzt Quantile und Verteilungen großer Datenmengen | O(k) Speicher, k=Kompressionsfaktor |

## Code-Beispiele im Detail

### Morris-Counter
Der Morris-Counter ermöglicht das Zählen von Events mit deutlich weniger Bits als benötigt würden, indem er probabilistisch zählt (z. B. nur jedes zweite, vierte, usw. Event). Dies spart Speicherplatz, bringt aber eine gewisse Ungenauigkeit mit sich.

**Beispiel:** Zählt bis 1000 mit einem 8-Bit-Register statt 10 Bits.

### HyperLogLog
HyperLogLog schätzt die Anzahl eindeutiger Elemente (Kardinalität) in großen Datenmengen. Der Algorithmus wandelt Werte über Hash-Funktionen in Binärwerte um und zählt die führenden Nullen, um die Menge zu approximieren.

**Beispiel:** Schätzt die Kardinalität einer Million Werte mit einer Fehlerrate von ~0,3 % bei nur 1024 Byte Speicher.

### Bloom-Filter
Ein Bloom-Filter ist eine space-efficient Datenstruktur, die testet, ob ein Element in einer Menge enthalten sein kann. Er kann falsch-positive Treffer liefern, aber niemals falsch-negative.

**Beispiel:** Prüft, ob die Werte 4 und 7 in einer Menge enthalten sind, mit 1 % Fehlerwahrscheinlichkeit.

### t-digest
Der t-digest-Algorithmus schätzt Quantile (Median, Perzentile) und Verteilungen großer Datenmengen. Er speichert eine komprimierte Darstellung der kumulierten Verteilungsfunktion (CDF).

**Beispiel:** Berechnet Median (50%-Quantil) und Anteil der Werte kleiner als x aus 1000 Zahlen.

## Abhängigkeiten

Die Beispiele benötigen folgende JAR-Dateien aus dem `lib/`-Verzeichnis:
- `hll-1.6.0.jar` – HyperLogLog-Implementierung von Aggregate Knowledge
- `guava-31.1-jre.jar` – Google Guava (für BloomFilter und Hash-Funktionen)
- `t-digest-3.3.jar` – t-digest-Implementierung von Ted Dunning
- `fastutil-8.5.11.jar` – Fastutil-Datenstrukturen

## Verwandte Kapitel

- **Kapitel 11**: Kafka-Streams und Echtzeit-Datenverarbeitung
- **Kapitel 13**: Spark und verteilte Datenverarbeitung
- **Kapitel 17**: Machine Learning mit Big Data

## Weitere Ressourcen

- [Originalpaper zum Morris-Counter (1978)](https://doi.org/10.1145/359619.359621)
- [HyperLogLog Paper (Flajolet et al., 2007)](https://doi.org/10.1016/j.tcs.2007.08.006)
- [Bloom-Filter Paper (1970)](https://doi.org/10.1145/362686.362692)
- [t-digest Paper (Dunning, 2019)](https://arxiv.org/abs/1902.04023)

---

*Letzte Aktualisierung: 14. März 2026*