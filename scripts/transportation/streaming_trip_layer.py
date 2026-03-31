from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Inisialisasi Spark Session
spark = SparkSession.builder.appName("TransportationStreaming").getOrCreate()

# Mendefinisikan Schema untuk data yang masuk
schema = StructType([
    StructField("trip_id", StringType()),
    StructField("vehicle_type", StringType()),
    StructField("location", StringType()),
    StructField("distance", DoubleType()),
    StructField("fare", DoubleType()),
    StructField("timestamp", StringType())
])

# Membaca data stream dari direktori JSON
df = spark.readStream.schema(schema).json("stream_data/transportation")

# Mengonversi kolom timestamp dari string ke tipe data timestamp
df = df.withColumn("timestamp", to_timestamp("timestamp"))

# Menulis data stream ke format Parquet
df.writeStream \
    .format("parquet") \
    .option("path", "data/serving/transportation") \
    .option("checkpointLocation", "data/checkpoints/transportation") \
    .start() \
    .awaitTermination()