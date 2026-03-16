# Kapitel 11 (NoSQL) -- Wide-Column-Stores: Cassandra

In diesem Unterkapitel erläutern wir den grundlegenden Umgang mit Cassandra.

------------------------------------------------------------------------

## ⚡ Quick Start

Starten Sie Cassandra direkt mit:

    docker run --name cass -d cassandra:latest

Verbinden Sie sich anschließend mit der Cassandra-Shell:
    docker exec -it cass bash
    cqlsh

------------------------------------------------------------------------

## Voraussetzungen

Für dieses Kapitel benötigen Sie:

-   **Docker**
-   Grundkenntnisse der Kommandozeile
-   das geklonte Repository dieses Buchs

Falls Sie Docker noch nicht installiert haben:

https://docs.docker.com/get-docker/

------------------------------------------------------------------------

> ⚠️ **Hinweis**
>
> Befehle mit `docker` werden im Terminal ausgeführt.  
> CQL-Befehle von Cassandra werden in der Cassandra-Shell (cqlsh) ausgeführt.

------------------------------------------------------------------------

## Cassandra-Container starten

Für die Beispiele in diesem Kapitel verwenden den offiziellen Docker-Container von Cassandra, der ohne weitere Schritte nicht für den Produktiveinsatz genutzt werden sollte.

    docker run --name cass -d cassandra:latest

Dieser Befehl:

- lädt automatisch das offizielle Docker-Image
- startet einen Container im Hintergrund
- vergibt den Container-Namen **cass**

------------------------------------------------------------------------

## Überprüfen, ob Cassandra läuft

Um zu testen, ob der Server korrekt gestartet wurde, führen Sie folgenden Befehl aus: 

    docker exec -it cass bash
    cqlsh
    SHOW VERSION

Sofern alles funktioniert, erhalten Sie die Versionen von cqlsh und des verwendeten Cassandra-Protokolls angezeigt.

------------------------------------------------------------------------

## Beispiele aus dem Buch ausführen
Das folgende Beispiel legt in cqlsh eine beispielhafte Tabelle mit E-Mail-Adressen von Kunden eines Online-Shops an:

-- Keyspace (ähnlich zu einer DB in SQL) anlegen
CREATE KEYSPACE IF NOT EXISTS shop WITH REPLICATION = {
  'class' : 'NetworkTopologyStrategy',
  'datacenter1' : '1'
};

USE shop;

-- Tabelle anlegen
CREATE TABLE IF NOT EXISTS customers (
  userid text PRIMARY KEY,
  mail text
);

-- Daten einfügen
INSERT INTO customers(userid, mail) VALUES('Mayer', 'mayer0815@gmx.de');
INSERT INTO shop.customers(userid, mail) VALUES('Schulze', 'schulze123@gmx.at');

-- Daten abfragen
SELECT * FROM customers;

SELECT * FROM customer WHERE userid = 'Mayer';

-- Daten aktualisieren
UPDATE customers SET mail_address = 'schulz123@gmx.de' WHERE userid = 'Schulze' AND mail_label = 'privat';

-- Tabelle erweitern
ALTER TABLE customers ADD city text;

------------------------------------------------------------------------

## Container stoppen

Das geht wie folgt:

    docker stop cass

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm cass

Danach können Sie erneut von vorne beginnen.

------------------------------------------------------------------------

## Fehlerbehebung (Debugging)

Falls etwas nicht wie erwartet funktioniert, können die folgenden Befehle bei der Fehlersuche helfen.

Überprüfen Sie zunächst, ob der Container läuft:

    docker ps

Der Container `cass` sollte in der Liste erscheinen.

Falls Cassandra nicht wie erwartet startet oder andere Fehler auftreten, kann es auch hilfreich sein, die Logs auf der Konsole, also außerhalb des Containers anzuzeigen:

    docker logs cass
