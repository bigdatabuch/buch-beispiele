# Kapitel 11 (NoSQL) -- Key-Value-Stores: Redis

In diesem Kapitel lernen Sie die grundlegenden Datenstrukturen und typischen Anwendungsfälle von Redis kennen und sehen, wie Redis als In-Memory-Datenbank für schnelle Datenstrukturen eingesetzt werden kann. Alle Beispiele des Kapitels lassen sich mit einem lokalen Docker-Container ausführen.

------------------------------------------------------------------------

## ⚡ Quick Start

Starten Sie Redis sofort mit:

    docker run -d --name redis -p 6379:6379 redis:latest \
    redis-server --requirepass s3cret

Verbinden Sie sich anschließend mit der Redis CLI:
    docker exec -it redis redis-cli -a s3cret

Testen Sie anschließend die Verbindung:

    PING

Erwartete Antwort:

    PONG

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
> Redis-Befehle wie `PING`, `HSET` oder `MULTI` werden in der Redis CLI ausgeführt.

------------------------------------------------------------------------

## Redis Container starten

Für die Beispiele im Kapitel verwenden wir eine Redis-Instanz mit aktivierter Persistenz.

    mkdir -p ./redis-data

    docker run -d --name redis \
    -p 6379:6379 \
    -v "$PWD/redis-data":/data \
    redis:latest \
    redis-server --save 60 1 --appendonly yes --requirepass s3cret


Dieser Befehl:

- lädt automatisch das offizielle Redis Image
- startet einen Container im Hintergrund
- öffnet den Redis-Port **6379** auf Ihrem lokalen Rechner
- vergibt den Container-Namen **redis**
- bindet das lokale Verzeichnis `redis-data` in den Container ein
- aktiviert die periodische Datensicherung (RDB Snapshot) (`--save 60`)
- aktiviert das **Append Only File (AOF)** (`--appendonly yes`)
- schützt den Zugriff auf Redis mit einem Passwort (`--requirepass s3cret`)

------------------------------------------------------------------------

## Überprüfen, ob Redis läuft

Um zu testen, ob der Server korrekt gestartet wurde, führen Sie folgenden Befehl aus: 

    docker exec -it redis redis-cli -a s3cret ping

Die erwartete Antwort lautet:

    PONG

Wenn Sie diese Antwort erhalten, läuft Redis korrekt.

------------------------------------------------------------------------

## Beispiele aus dem Buch ausführen
Das folgende Beispiel speichert ein Produkt als Redis Hash. Die Befehle werden in einer Transaktion ausgeführt, sodass sie atomar verarbeitet werden.


Sie können die Beispiele aus dem Buch direkt in der Redis CLI im Container ausführen. 

    docker exec -it redis redis-cli -a s3cret    

Führen Sie die folgenden Befehle aus: 

    # Transaktion starten: Alle folgenden Befehle werden gesammelt 
    MULTI
    HSET product:123 name "IDEA Pax" price "499.00" stock "25" category "Kleiderschrank"
    EXPIRE product:123 300

    # Transaktion ausführen
    EXEC

    # Lesen
    HGETALL product:123
    HMGET product:123 name price
    TTL product:123

    # Preis ändern
    HSET product:123 price "459.99"

    # Bestand ändern
    HINCRBY product:123 stock -1

    # TTL anpassen / entfernen
    EXPIRE product:123 600
    PERSIST product:123

    # Löschen
    DEL product:123

------------------------------------------------------------------------

## Redis Daten zurücksetzen

Während des Kapitels werden viele Schlüssel in Redis erzeugt.\
Um die Datenbank zurückzusetzen, können Sie alle Schlüssel löschen: 

    docker exec -it redis redis-cli -a s3cret FLUSHDB

------------------------------------------------------------------------

## Container stoppen

Wenn Sie Redis nicht mehr benötigen, können Sie den Container stoppen:

    docker stop redis

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm redis

Danach können Sie Redis erneut starten.

------------------------------------------------------------------------

## Fehlerbehebung (Debugging)

Falls Redis nicht wie erwartet funktioniert, können die folgenden Befehle bei der Fehlersuche helfen.

## Laufende Container anzeigen

Überprüfen Sie zunächst, ob der Redis-Container läuft:

    docker ps

Der Container `redis` sollte in der Liste erscheinen.

Wenn Sie auch gestoppte Container sehen möchten:

    docker ps -a


## Container-Logs anzeigen

Falls Redis nicht startet oder Fehler auftreten, können Sie die Logs anzeigen:

    docker logs redis

Diese enthalten oft Hinweise auf Konfigurationsprobleme oder Portkonflikte.
