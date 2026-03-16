# Kapitel 11 (NoSQL) -- Graph-Datenbanken: Neo4j

In diesem Kapitel lernen Sie die grundlegenden Datenstrukturen und typischen Anwendungsfälle von Neo4j kennen.
------------------------------------------------------------------------

# Voraussetzungen

Für dieses Kapitel benötigen Sie:

-   **Docker**
-   Grundkenntnisse der Kommandozeile
-   das geklonte Repository dieses Buchs

Falls Sie Docker noch nicht installiert haben:

https://docs.docker.com/get-docker/

------------------------------------------------------------------------

# Neo4J mit Docker Compose starten

Wechseln Sie in das Verzeichnis, welches die Datei `docker-compose.yml` für Neo4J enthält. Starten Sie den Container mit 

    docker compose up -d

Sie können den Status des Containers mit den folgenden Befehlen prüfen: 

    docker compose ps
    docker compose logs -f neo4j

------------------------------------------------------------------------

# Neo4j aufrufen 

Nach dem Start erreichen Sie Neo4j unter

- Weboberfläche: http://localhost:7474
- Bolt-Verbindung: bolt://localhost:7687

Sie können die Abfragen aber auch direkt im Container per Command Line Interface ausführen: 

    docker exec -it neo4j cypher-shell -u neo4j -p testtest

Nutzername und Passwort wurden in der `docker-compose.yml` Datei festgelegt. Die Shell kann man per 

    :exit

wieder verlassen. 

# Beispiele aus dem Buch ausführen (CLI)
Das folgende Beispiel erstellt zwei Knoten, Alice und Bob, wowie einen  Filmknoten (Harry Potter) und zwei Beziehungen.    

    CREATE (alice:Person {name: "Alice"});
    CREATE (bob:Person {name: "Bob"});

    // Filme und Beziehungen
    CREATE (potter:Movie {title: "Harry Potter"}),
    (alice)-[:RATED {score: 5}]->(potter),
    (alice)-[:FRIENDS_WITH]->(bob);

# Beispiele aus dem Buch ausführen (Skript)

**Alternative 1**
Der folgende Befehl kopiert eine Datei vom Host-System in einen laufenden Docker-Container.

    docker cp ./init.cypher neo4j:/init.cypher 

Mit `./init.cypher` referenzieren Sie Ihre Datei auf dem lokalen Rechner. `neo4j` referenziert den Namen des Containers und `/init.cypher` referenziert den Zielpfad im Container-Dateisystem.     

Das Skript kann mit dem Befehl 

    docker exec -it neo4j cypher-shell -u neo4j -p testtest -f /init.cypher    

ausgeführt werden. Bitte beachten Sie, dass Nutzername und Passwort mit der Konfiguration in der Datei `docker-compose.yml` übereinstimmen. Die Datei `init.cypher` muss im selben Ordner liegen.

**Alternative 2**
Schneller geht es mit: 

    docker exec -i neo4j cypher-shell -u neo4j -p testtest --format verbose < init.cypher

Mit dem Paramter `--format verbose` können Sie sich Fehler- und Erfolgsmeldungen ausgeben lassen. 

------------------------------------------------------------------------

## In der Datenbank suchen

Kompletter Graph ausgegeben lassen: 

    MATCH (n) 
    OPTIONAL MATCH (n)-[r]-(f) 
    RETURN n, r, f;

`OPTIONAL` führt dazu, dass Knoten, die keine Beziehungen haben, nicht entfernt werden.   

Nach dem Film *Harry Potter* suchen:

    MATCH (f:Film {name: "Harry Potter"})
    RETURN f;

Freunde und deren Bewertungen suchen: 

    MATCH (p:Person)-[:FRIENDS_WITH]->(f:Person)-[r:RATED]->(m:Movie)
    RETURN p.name, f.name, m.title, r.score;

Freunde finden, die den Film *Harry Potter* schon bewertet haben:

    MATCH (f:Movie)<-[r:RATED]-(p:Person) -[:FRIENDS_WITH]->(friend:Person) 
    WHERE f.title='Harry Potter' 
    RETURN DISTINCT p.name, friend.name;

Beliebteste Filme suchen: 

    MATCH (:Person)-[r:RATED]->(m:Movie)
    RETURN m.title, avg(r.score) AS rating
    ORDER BY rating DESC;

------------------------------------------------------------------------

## Daten aktualisieren oder löschen 

Änderung des Filmtitels

    MATCH (p:Movie {title: "Harry Potter"}) 
    SET p.title='Harry Potter und der Stein der Weisen', 
        p.year=2001 
    RETURN p;

Beziehungen zwischen zwei Knoten löschen 

    MATCH (j:Person {name:'Alice'}) - [r:FRIENDS_WITH]-> (n:Person {name: 'Bob'}) 
    DELETE r;

Knoten löschen

    MATCH (m:Person {name: 'Bob'})
    DELETE m

Gesamter Graph löschen

    MATCH(n)
    DETACH DELETE n; 

In Neo4j dürfen Knoten mit Beziehungen nicht direkt gelöscht werden. Deswegen werden mit `DETACH` Beziehungen von zu löschenden Knoten entfernt. 

------------------------------------------------------------------------

## Container stoppen

Wenn Sie Neo4j nicht mehr benötigen, können Sie den Container stoppen:

    docker stop neo4j

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm neo4j

Danach können Sie Neo4j erneut starten.

------------------------------------------------------------------------

# Fehlerbehebung (Debugging)

Falls Neo4j nicht wie erwartet funktioniert, können die folgenden Befehle bei der Fehlersuche helfen.

## Laufende Container anzeigen

Überprüfen Sie zunächst, ob der Container läuft:

    docker ps

Der Container `neo4j` sollte in der Liste erscheinen.

Wenn Sie auch gestoppte Container sehen möchten:

    docker ps -a


## Container-Logs anzeigen

Falls der Container nicht startet oder Fehler auftreten, können Sie die Logs anzeigen:

    docker logs neo4j

Diese enthalten oft Hinweise auf Konfigurationsprobleme oder Portkonflikte.
