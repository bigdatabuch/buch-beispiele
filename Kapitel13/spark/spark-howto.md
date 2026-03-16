# Ausführung von Jupyter Notebooks mit Spark

## Option 1 – Ausführen mit Docker

Docker ermöglicht eine reproduzierbare Umgebung ohne lokale Installation von Spark.

### Docker Image erstellen

Im Projektordner: 

    docker build -t pyspark-notebook

### Container starten

    docker run -p 8888:8888 -v $(pwd):/workspace pyspark-notebook

Danach erscheint im Terminal ein Jupyter Notebook Link, z.B.:

    http://127.0.0.1:8888/?token=...

Diesen Link im Browser öffnen.

### Notebook starten

1. `SparkDataFrames.ipynb` öffnen
2. Zellen nacheinander ausführen
3. Das Notebook läuft lokal im Container.

## Option 2 – Ausführen mit Google Colab

Das Notebook kann auch ohne lokale Installation über Google Colab ausgeführt werden. Colab stellt eine Python-Umgebung in der Cloud bereit.

### Notebook hochladen

1. Öffnen Sie: https://colab.research.google.com
2. Klicken Sie auf Upload Notebook
3. Laden Sie `SparkDataFrames.ipynb` hoch

### PySpark installieren
(falls notwendig)

In einer neuen Zelle ausführen: 
    !pip install pyspark

### SparkSession starten 

Danach kann Spark direkt im Notebook gestartet werden und alle Zellen des Notebooks ausgeführt werden. 