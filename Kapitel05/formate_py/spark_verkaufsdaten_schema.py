from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# Initialisiere Spark Session
spark = SparkSession.builder.appName("DataConversion").getOrCreate()

schema = StructType([
    StructField("KundenID", IntegerType(), True),
    StructField("AuftragID", StringType(), True),  # String, solange 'A' vorne steht (z.B. Auftrag ID 'A2000')
    StructField("Produkt", StringType(), True),
    StructField("Preis", DoubleType(), True),
])

# Lese die CSV-Datei. Wir geben den Header an und lassen Spark das Schema ableiten.
df_sales = spark.read.csv(
    "verkaufsdaten.csv",
    header=True, # erste Zeile enthält Die Spaltennamen
    schema=schema  # Schema explizit definieren!
)

df_sales.printSchema() # Optional: Gebe abgeleitetes Schema aus

#### Schreiben

# Schreibe den Data Frame in das Parquet-Format.
# Spark kümmert sich um Kompression und Metadaten automatisch.
df_sales.write.mode("overwrite").parquet("verkaufsdaten.parquet")