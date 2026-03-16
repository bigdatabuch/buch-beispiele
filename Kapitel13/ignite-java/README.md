# Apache Ignite (Java)

## Beispiele

### Langsames, lokales Aggregieren

Demonstriert die grundlegende Verwendung von Apache Ignite mit einer einfachen in-memory Aggregation über Sensor-Daten. Dieses Beispiel zeigt den Unterschied zwischen lokaler und verteilter Verarbeitung.

- [SensorReading.java](src/main/java/de/bigdatabuch/SensorReading.java) - Datenmodell für Sensor-Readings
- [IgniteSensorLangsamLokal.java](src/main/java/de/bigdatabuch/IgniteSensorLangsamLokal.java) - Beispiel für lokale Aggregation

### Schnelles, verteiltes Aggregieren mit SQL

Zeigt, wie Apache Ignite's SQL-Fähigkeiten genutzt werden können, um große Datenmengen effizient in einem verteilten Cluster zu aggregieren. Dieses Beispiel nutzt die native SQL-Unterstützung von Ignite für maximale Performance.

- [SensorReadingSQL.java](src/main/java/de/bigdatabuch/SensorReadingSQL.java) - Datenmodell mit SQL-Annotationen
- [IgniteSensorSchnellVerteilt.java](src/main/java/de/bigdatabuch/IgniteSensorSchnellVerteilt.java) - Beispiel für verteilte SQL-Abfragen

### Affinity Keys

Beispiel eines Onlineshops, das zeigt, wie Affinity Keys verwendet werden können, um verwandte Daten (Kunden und Bestellungen) auf dem gleichen Cluster-Knoten zu speichern. Dies reduziert Netzwerk-Overhead bei Joins und verbessert die Performance erheblich.

- [Kunde.java](src/main/java/de/bigdatabuch/affinity_de/affinity/Kunde.java) - Kunden-Datenmodell
- [Bestellung.java](src/main/java/de/bigdatabuch/affinity_de/affinity/Bestellung.java) - Bestellungs-Datenmodell mit Affinity Key
- [IgniteOnlineshopDe.java](src/main/java/de/bigdatabuch/affinity_de/affinity/IgniteOnlineshopDe.java) - Beispielanwendung mit Kunden und Bestellungen

### Python Thin Client

Zeigt, wie ein Python-Client über den Thin Client mit einem Apache Ignite Cluster kommunizieren kann. Der Cluster wird in Java gestartet, während die Verbindung und Abfragen von Python aus erfolgen.

- [IgniteSensorPythonThinClient.java](src/main/java/de/bigdatabuch/thinclient/IgniteSensorPythonThinClient.java) - Java-Server-Code für den Thin Client
- Weitere Python-Beispiele im [ignite-py Projekt](../ignite-py/)

## Mit Java >= 17 starten

siehe [Ignite Java Dokumentation](https://ignite.apache.org/docs/ignite2/latest/quick-start/java)

Beim Starten ist es nötig folgende VM Argumente mitanzugeben (CLI, IDE, Shell)

```bash
-Djava.net.preferIPv4Stack=true
--add-opens=java.base/jdk.internal.access=ALL-UNNAMED
--add-opens=java.base/jdk.internal.misc=ALL-UNNAMED
--add-opens=java.base/sun.nio.ch=ALL-UNNAMED
--add-opens=java.base/sun.util.calendar=ALL-UNNAMED
--add-opens=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED
--add-opens=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED
--add-opens=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED
--add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED
--add-opens=java.base/java.io=ALL-UNNAMED
--add-opens=java.base/java.nio=ALL-UNNAMED
--add-opens=java.base/java.net=ALL-UNNAMED
--add-opens=java.base/java.util=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent.locks=ALL-UNNAMED
--add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED
--add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/java.lang.invoke=ALL-UNNAMED
--add-opens=java.base/java.math=ALL-UNNAMED
--add-opens=java.sql/java.sql=ALL-UNNAMED
--add-opens=java.base/java.lang.reflect=ALL-UNNAMED
--add-opens=java.base/java.time=ALL-UNNAMED
--add-opens=java.base/java.text=ALL-UNNAMED
--add-opens=java.management/sun.management=ALL-UNNAMED
--add-opens java.desktop/java.awt.font=ALL-UNNAMED
```