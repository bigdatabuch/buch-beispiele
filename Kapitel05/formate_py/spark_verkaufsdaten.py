from pyspark.sql import SparkSession

# Initialisiere Spark Session
spark = SparkSession.builder.appName("DataConversion").getOrCreate()

# Lese die CSV-Datei. Wir geben den Header an und lassen Spark das Schema ableiten.
df_sales = spark.read.csv(
    "verkaufsdaten.csv",
    header=True, # erste Zeile enthält Die Spaltennamen
    inferSchema=True  # Einfach, aber für große Dateien nicht empfohlen!
)

df_sales.printSchema() # Optional: Gebe abgeleitetes Schema aus