## Projekt bauen und ausführen (Docker + Maven)

Das Projekt kann ohne lokale Java- oder Maven-Installation mit Docker gebaut und gestartet werden.

### Hinweis für Windows (Git Bash)

Unter Git Bash kann es zu Problemen mit der automatischen Pfadkonvertierung kommen.  
Daher sollte vorher folgende Umgebungsvariable gesetzt werden:

    export MSYS_NO_PATHCONV=1

### Projekt bauen 

Der folgende Befehl startet einen Maven-Container, der das Projekt kompiliert und das Paket erstellt:

    docker run --rm \
    -v "$PWD":/app \
    -w /app \
    maven:3.9.9-eclipse-temurin-17 \
    mvn -B -DskipTests package -Dexec.mainClass=com.example.SocketWordCount

### Flink Container starten

    docker compose up -d

Job starten: 

    docker compose exec jobmanager \
    flink run -d /opt/flink/usrlib/socket-wordcount.jar \
    --host textsource --port 9000

Eingabe im Terminal:

    docker attach textsource

Ausgabe in den Logdateien: 

    docker compose logs -f taskmanager    