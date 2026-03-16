# spark/stream_coffee_file.py
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col, to_timestamp, window, sum as _sum, count as _count, round as _round

spark = (SparkSession.builder
         .appName("CoffeeFileStream")
         .getOrCreate())

spark.conf.set("spark.sql.shuffle.partitions", "4")

# 1) Schema
schema = StructType([
    StructField("order_id",   StringType(), False),
    StructField("drink",      StringType(), False),
    StructField("size",       StringType(), False),
    StructField("quantity",   IntegerType(), False),
    StructField("unit_price", DoubleType(), False),
    StructField("event_time", StringType(), False),
])

# 2) Quelle: JSON-Lines aus data/input/ (nur neue Dateien)
raw = (spark.readStream
       .schema(schema)
       .option("maxFilesPerTrigger", 1)
       .json("/data/input"))

events = (raw
    .withColumn("event_time", to_timestamp(col("event_time")))
    .withColumn("revenue", _round(col("unit_price") * col("quantity"), 2))
)

# 3) Watermark + Deduplikation (im Watermark-Horizont)
dedup = (events
         .withWatermark("event_time", "2 minutes")
         .dropDuplicates(["order_id"]))

# 4) Fenster: 5-Minuten (tumbling)
agg = (dedup
    .groupBy(
        window(col("event_time"), "5 minutes"),
        col("drink")
    )
    .agg(
        _sum("revenue").alias("revenue"),
        _count("*").alias("orders")
    )
    .select(
        col("window.start").alias("window_start"),
        col("window.end").alias("window_end"),
        col("drink"),
        col("orders"),
        _round(col("revenue"), 2).alias("revenue")
    )
)

# 5a) Sink: Console (live Updates)
console_q = (agg.writeStream
    .outputMode("update")
    .format("console")
    .option("truncate", "false")
    .option("checkpointLocation", "/chk/console")   # Docker? -> "/chk/console"
    .start())

# 5b) Sink: Parquet (nur **finale** Fenster)
parquet_q = (agg.writeStream
    .outputMode("append")                           # nur abgeschlossene Fenster
    .format("parquet")
    .option("path", "/data/out/coffee_by_drink")     # Docker? -> "/data/out/coffee_by_drink"
    .option("checkpointLocation", "/chk/parquet")    # Docker? -> "/chk/parquet"
    .start())

spark.streams.awaitAnyTermination()

