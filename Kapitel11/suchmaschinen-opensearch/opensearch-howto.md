# Kapitel 11 (NoSQL) -- Suchmaschine Opensearch

In diesem Unterkapitel erläutern wir den grundlegenden Umgang mit der Suchmaschine Opensearch.

------------------------------------------------------------------------

## Opensearch-Container starten

Für die Beispiele in diesem Kapitel verwenden den offiziellen Docker-Container von Cassandra, der ohne weitere Schritte nicht für den Produktiveinsatz genutzt werden sollte.

    docker run --name os-test \
      -p 9200:9200 \
      -e "discovery.type=single-node" \
      -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=StrongPW123?" \
      -e "OPENSEARCH_INITIAL_ADMIN_USERNAME=admin" \
      -i \
      opensearchproject/opensearch:latest

Dieser Befehl:

- lädt automatisch das offizielle Docker-Image
- startet einen Container im Hintergrund
- vergibt den Container-Namen **os-test**
- stellt Opensearch zum Testen auf ein Singlenode-System
- setzt Username und Passwort

Der Befehl braucht eine Weile, bis der Opensearch-Server vollständig gestartet ist. Sobald das geschafft ist können Sie im Browser die URL

  https://localhost:9200

aufrufen und sobald Sie das Sicherheitsrisiko auf Grund eines fehlenden SSL-Zertifikats akzeptiert und Nutzername und Passwort eingegeben haben,
sollten Sie eine Versionsübersicht angezeigt bekommen.

------------------------------------------------------------------------

## Beispiele aus dem Buch ausführen

Mit dem folgenden CURL-Befehl von der Konsole können Sie einen ersten Datensatz an Opensearch übermitteln:

curl -k -u "admin:StrongPW123?" \
  -X POST "https://localhost:9200/produkt-demo/_doc" \
  -H "Content-Type: application/json" \
  -d '{
      "produktname": "Laptop",
      "preis": 1200,
      "verfuegbar": 17
  }'

  Im Anschluss daran können wir den neu angelegten Demo-Index mit dem ersten Eintrag im Browser betrachten:

    https://localhost:9200/produkt-demo/_search


------------------------------------------------------------------------

## Container stoppen

Das geht wie folgt:

    docker stop os-test

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm os-test

Danach können Sie erneut von vorne beginnen.

