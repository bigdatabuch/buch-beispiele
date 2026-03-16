# Kapitel 11 (NoSQL) -- Multi-Model-Datenbanken: ArangoDB

In diesem Kapitel lernen Sie die grundlegenden Datenstrukturen und typischen Anwendungsfälle von ArangoDB kennen.
------------------------------------------------------------------------

# Voraussetzungen

Für dieses Kapitel benötigen Sie:

- **Docker**
- das geklonte Repository dieses Buchs

Falls Sie Docker noch nicht installiert haben:

https://docs.docker.com/get-docker/

------------------------------------------------------------------------

# ArangoDB Docker Container starten

Mit dem folgenden Befehl können Sie einen ArangoDB Container erstellen: 
    docker run -e ARANGO_NO_AUTH=1 -p 8529:8529 -d --name test-arangodb arangodb

Sie können den Status des Containers mit den folgenden Befehlen prüfen: 

    docker compose ps
    docker compose logs -f arangodb

------------------------------------------------------------------------

# ArangoDB Webinterface 

Die Web-UI lässt sich mit der URL `http://localhost:8529/` öffnen. Im Buch wird ausschließlich mit der Web-UI gearbeitet. 

------------------------------------------------------------------------

# Collections anlegen

Collections findet man im linken Menü. Per `Add collection` lassen sich verschiedene Collections hinzufügen. 

------------------------------------------------------------------------

# ArangoDB Daten einlesen 

1. Variante: JSON Dokument einlesen
- restaurants.json

2. Variante: INSERT im Editor unter dem Menüpunkt `Queries` ausführen. 
- `insert_users`
- `insert_likes`

------------------------------------------------------------------------

# Graph anlegen 

- Graphs - *Add Graph* - *GeneralGraph*
- Name *social*; Edge-Definition: *likes* von *users* *restaurants*
- `Create` klicken

------------------------------------------------------------------------

# Beispiele aus dem Buch ausführen (Web UI)

Die Beispiele aus dem Buch lassen sich ebenfalls im Editor unter `Queries` ausführen. Das Beispiel aus Listing 11.24 ist im Skript `query_empfehlungen`  abgelegt. 

------------------------------------------------------------------------

# Container stoppen

Wenn Sie ArangoDB nicht mehr benötigen, können Sie den Container stoppen:

    docker stop arangodb

------------------------------------------------------------------------

# Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm arangodb

Danach können Sie arangodb erneut starten.

------------------------------------------------------------------------

# Fehlerbehebung (Debugging)

Falls ArangoDB nicht wie erwartet funktioniert, können die folgenden Befehle bei der Fehlersuche helfen.

------------------------------------------------------------------------

## Laufende Container anzeigen

Überprüfen Sie zunächst, ob der Container läuft:

    docker ps

Der Container `arangodb` sollte in der Liste erscheinen.

Wenn Sie auch gestoppte Container sehen möchten:

    docker ps -a

------------------------------------------------------------------------

## Container-Logs anzeigen

Falls der Container nicht startet oder Fehler auftreten, können Sie die Logs anzeigen:

    docker logs arangodb

Diese enthalten oft Hinweise auf Konfigurationsprobleme oder Portkonflikte.
