# Kapitel 11 (NoSQL) -- Zeitreihendatenbanken: InfluxDB

In diesem Kapitel lernen Sie die grundlegenden Datenstrukturen und typischen Anwendungsfälle von InfluxDB kennen.
------------------------------------------------------------------------

## Voraussetzungen

Für dieses Kapitel benötigen Sie:

-   **Docker**
-   Grundkenntnisse der Kommandozeile
-   das geklonte Repository dieses Buchs

Falls Sie Docker noch nicht installiert haben:

https://docs.docker.com/get-docker/

------------------------------------------------------------------------

## InfluxDB mit Docker Compose starten

Wechseln Sie in das Verzeichnis, welches die Datei `docker-compose.yml` für InfluxDB enthält. Starten Sie den Container mit 

    docker compose up -d

Sie können den Status des Containers mit den folgenden Befehlen prüfen: 

    docker compose ps
    docker compose logs -f influxdb

------------------------------------------------------------------------

## InfluxDB Daten einlesen 

Die Daten aus dem Beispiel werden mit dem Skript `createData.py` generiert (Ausgabe: `air_quality.lp`). Für Demonstrationszwecke werden die Messwerte nicht nur zufällig, sondern mit einem einfachen Tagesverlauf erzeugt. 

- **NO2, PM10 und PM2.5** steigen typischerweise zu den Hauptverkehrszeiten am Morgen und am späten Nachmittag.
- **Ozon** ist eher tagsüber höher und erreicht seine Spitzenwerte häufig am frühen Nachmittag.
- Kleine Zufallsschwankungen

So lassen sich in InfluxDB, im Data Explorer oder in Grafana später Diagramme erzeugen, die einem realen Messverlauf ähnlicher sehen als rein gleichverteilte Zufallswerte.

Um diese in die Datenbank zu importieren, kann man folgenden `curl` - Befehl im Terminal ausführen: 

    curl -XPOST "http://localhost:8086/api/v2/write?org=air_quality_org&bucket=air_quality&precision=ns" --header "Authorization: Token my-secret-token1" --data-binary @air_quality.lp

Der Befehl sendet eine HTTP-POST Anfrage an die InfluxDB API, um Zeitreihendaten im Line Protocol Format in ein Bucket zu schreiben.
-  `http://localhost:8086/api/v2/write`: Write-API der InfluxDB
- `org=air_quality_org`: Organisation, zu der die Daten gehören 
- `bucket=air_quality`: Bucket, in den die Daten geschrieben werden 
- `precision=ns`: Zeitstempel der Daten in Nanosekunden-Genauigkeit
- `--header "Authorization: Token my-secret-token"`: Authentifizierung über ein API Token 
- `--data-binary @air_quality.lp` sendet Inhalt der Datei unverändert an die API 

------------------------------------------------------------------------

## InfluxDB Weboberfläche aufrufen 

Nach dem Start erreichen Sie InfluxDB unter der Weboberfläche: http://localhost:8086 zu erreichen. 

Beim ersten Start müssen Sie folgendes eingeben:
- Username
- Password

Im Beispiel werden beide Parameter in der `docker_compose.yml` Datei definiert. 

Daten können im Data Explorer (oben im Menü links) dargestellt werden. Dort lassen sich Bucket, Measurment, Tags und die einzelnen Felder (NO2, PM10, PM2_5 oder Ozon) auswählen.

------------------------------------------------------------------------

## Beispiele aus dem Buch ausführen (CLI)

Abfragen werden in InfluxDB mit der Flux Query Language ausgeführt. Ein einfaches Beispiel, um Daten aus dem Bucket `air_quality` der letzten fünf Stunden abzurufen:

    docker exec -it influxdb influx query -org air_quality_org ' 
    from(bucket: "air_quality") 
        |> range(start: -5h)
    '
Da die Luftqualitätsdaten in unserem Beispiel im Measurement air_quality gespeichert sind und die Tags city und station enthalten, kann die Abfrage weiter eingeschränkt werden:

    docker exec -it influxdb influx query -org air_quality_org ' 
    from(bucket: "air_quality") 
        |> range(start: -5h) 
        |> filter(fn: (r) => r._measurement == "air_quality") 
        |> filter(fn: (r) => r.city == "Ingolstadt") 
        |> filter(fn: (r) => r.station == "Muenchener_Strasse") 
    '

Diese Query liefert alle Messwerte der Luftqualität für die Messstation Muenchener_Strasse in Ingolstadt innerhalb der letzten fünf Stunden. Die Ergebnisse werden tabellarisch direkt im Terminal ausgegeben.

## Daten löschen

In InfluxDB können bereits gespeicherte Zeitreihendaten gezielt wieder gelöscht werden. Dies geschieht über die Delete API. Dabei wird ein Zeitbereich angegeben, in dem Daten entfernt werden sollen.

    curl -X POST "http://localhost:8086/api/v2/delete?org=air_quality_org&bucket=air_quality" \
        --header "Authorization: Token my-secret-token1" \
        --header "Content-Type: application/json" \
        --data '{"start":"2026-01-01T00:00:00Z","stop":"2027-01-01T00:00:00Z"}'

Wichtig: Bei mehrzeiligen Shell-Befehlen muss der Backslash \ jeweils das letzte Zeichen der Zeile sein. Andernfalls werden die folgenden Zeilen nicht mehr als Teil desselben Befehls interpretiert.

InfluxDB-Daten lassen sich normalerweise nicht direkt aktualisieren. Üblich ist, neue Punkte zu schreiben oder Daten gezielt zu löschen.

------------------------------------------------------------------------

## Container stoppen

Wenn Sie InfluxDB nicht mehr benötigen, können Sie den Container stoppen:

    docker stop influxdb

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm influxdb

Danach können Sie influxdb erneut starten.

------------------------------------------------------------------------

## Fehlerbehebung (Debugging)

Falls der Container nicht wie erwartet funktioniert, können die folgenden Befehle bei der Fehlersuche helfen.

## Laufende Container anzeigen

Überprüfen Sie zunächst, ob der Container läuft:

    docker ps

Der Container `influxdb` sollte in der Liste erscheinen.

Wenn Sie auch gestoppte Container sehen möchten:

    docker ps -a


## Container-Logs anzeigen

Falls der Container nicht startet oder Fehler auftreten, können Sie die Logs anzeigen:

    docker logs influxdb

Diese enthalten oft Hinweise auf Konfigurationsprobleme oder Portkonflikte.
