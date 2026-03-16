# Kapitel 11 (NoSQL) -- Document-Stores: MongoDB

In diesem Kapitel lernen Sie die grundlegenden Datenstrukturen und typischen Anwendungsfälle von MongoDB kennen.

------------------------------------------------------------------------

## ⚡ Quick Start

Starten Sie einen MongoDB Container sofort mit:

     docker run -d \
     --name mongo \
     -p 27017:27017 \
     -v mongo_data:/data/db \
     mongo:latest

Verbinden Sie sich anschließend mit der MongoDB-Shell:
    docker exec -it mongo mongosh

------------------------------------------------------------------------

# Voraussetzungen

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
> MongoDB-Befehle wie `PING`, `HSET` oder `MULTI` werden in der MongoDB-Shell ausgeführt.

------------------------------------------------------------------------

# MongoDB Container starten

Für die Beispiele im Kapitel verwenden wir eine MongoDB-Instanz mit aktivierter Persistenz.

    mkdir -p ./redis-data

    docker run -d --name redis \
    -p 6379:6379 \
    -v "$PWD/redis-data":/data \
    redis:latest \
    redis-server --save 60 1 --appendonly yes --requirepass s3cret


Erklärung der einzelnen Parameter:

- `docker run` startet einen neuen Container aus einem Docker-Image
- `-d` startet den Container im Hintergrund, sodass das aktuelle Terminal weiter benutzt werden kann
- `--name mongo`vergibt den Container-Namen **mongo** 
- `-p 27017:27017` leitet den Port **27017** des Containers auf den Port **27017** des Hostsystems weiter. Dadurch ist die MongoDB-Datenbank vom Host oder aus dem Netzwerk über diesen Port erreichbar. 
- `-v mongo_data:/data/db` bindet ein Docker-Volume namens `mongo-data` in das Verzeichnis `/data/db` im Container ein. Dieses Verzeichnis enthält die Datenbankdateien von MongoDB. 
- `mongo:latest` verwendet die aktuellste Version des offiziellen MongoDB-Image. 

------------------------------------------------------------------------

# Beispiele aus dem Buch ausführen
Das folgende Beispiel fügt zwei Dokumente in die Collection *cases* ein:

Sie können die Beispiele aus dem Buch direkt in der MongoDB-Shell im Container ausführen. 

    docker exec -it mongo mongosh    

Führen Sie die folgenden Befehle aus: 

    db.cases.insertMany([
        {
            caseId: "CASE-2025-001",
            date: ISODate("2025-08-20"),
            familyName: "Nguyen",
            location: "Region X",
            members: [
                { name: "Hoa", age: 34, medicalNeeds: "Diabetes" },
                { name: "Minh", age: 6 }
            ],
            needs: ["Unterkunft", "Medizinische Versorgung"],
            assignedVolunteer: "Anna Müller",
            status: "offen"
        },
        {
            caseId: "CASE-2025-002",
            person: { name: "Jeanette Lagarde", age: 76 },
            location: "Region Y",
            needs: ["Nahrungsmittelhilfe", "Psychologische Betreuung"],
            language: "Französisch",
            followUpDate: ISODate("2025-09-15"),
            status: "in Bearbeitung"
        }
    ])

------------------------------------------------------------------------

## In der Datenbank suchen
Das folgende Beispiel sucht in allen Dokumenten aus der Sammlung *cases* die Dokumente, die ein Schlüssel-Wert-Paar mit `location : "Region X" enthalten: 

    db.cases.find({location:"Region X"})

------------------------------------------------------------------------

## Dokumente aktualisieren

Im Beispiel wird für den Fall mit der ID "CASE-2025-001" der Name der Helferin geändert sowie das Alter von Hoa auf 36 erhöht.

    db.cases.updateOne(
        { "caseId": "CASE-2025-001" }, // Filter nach bestimmter CaseID
        {
            $set: {
                "assignedVolunteer": "Bernd Meier", // Familienname ändern
            },
            $inc: {
                "members.0.age": 1 // Alter um ein Jahr erhöhen
            }
        }
    );

------------------------------------------------------------------------

## Dokumente löschen

Im Beispiel  werden alle Fälle der Region Y gelöscht. 

    db.cases.deleteMany({"location": "Region Y"})

------------------------------------------------------------------------

## Indexierung

MongoDB unterstützt die Erstellung von Indizes zu einem beliebigen verschachtelten Feld in der JSON-Struktur. Es lassen sich sowohl Einzelindizes als auch zusammengesetzte Indizes erstellen. 

    db.cases.createIndex({ "caseID": 1})

------------------------------------------------------------------------

## Aggregatfunktionen

Die folgende Funktion berechnet die Anzahl der Fälle pro Helfer für die Region X

    db.cases.aggregate([
        // Stage 1: Filter Region X
        {
            $match: {location: "Region X"}
        },
        // Stage 2: Gruppierung nach Helfern; Anzahl der Fälle zählen
        {
            $group: { _id: {"assignedVolunteer": "$assignedVolunteer"},
            totalCount: { $sum: 1 } }
        }
    ])

------------------------------------------------------------------------

## MongoDB Daten zurücksetzen

Um die Datenbank direkt in der Shell zurückzusetzen, können Sie die Datenbank auswählen und anschließend löschen: 

    use myDatabase
    db.dropDatabase()

------------------------------------------------------------------------

## Container stoppen

Wenn Sie MongoDB nicht mehr benötigen, können Sie den Container stoppen:

    docker stop mongo

------------------------------------------------------------------------

## Container entfernen (Reset)

Falls Sie das Kapitel komplett zurücksetzen möchten:

    docker rm mongo

Danach können Sie MongoDB erneut starten.

------------------------------------------------------------------------

## Daten vollständig löschen (inklusive Volume)

Wenn Sie zusätzlich alle gespeicherten Daten entfernen möchten: 

    docker volume rm mongo_data


# Fehlerbehebung (Debugging)

Falls MongoDB nicht wie erwartet funktioniert, können die folgenden Befehle bei der Fehlersuche helfen.

## Laufende Container anzeigen

Überprüfen Sie zunächst, ob der Container läuft:

    docker ps

Der Container `mongo` sollte in der Liste erscheinen.

Wenn Sie auch gestoppte Container sehen möchten:

    docker ps -a


## Container-Logs anzeigen

Falls MongoDB nicht startet oder Fehler auftreten, können Sie die Logs anzeigen:

    docker logs mongo

Diese enthalten oft Hinweise auf Konfigurationsprobleme oder Portkonflikte.
