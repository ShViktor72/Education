
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Создание SparkSession
spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("WordCount") \
    .getOrCreate()

# Чтение CSV файла
df = spark.read.csv("hdfs://namenode:8020/airports.dat", header=True, inferSchema=True)



# Вывод первых 5 строк
df.show(2)



# Фильтрация данных
high_price_products = df.filter(col("_c3") == "Kazakhstan")
high_price_products.show()


# Присвоение имен колонкам
df = df.withColumnRenamed("_c0", "id") \
       .withColumnRenamed("_c1", "name") \
       .withColumnRenamed("_c2", "city") \
       .withColumnRenamed("_c3", "country") \
       .withColumnRenamed("_c4", "iata_code") \
       .withColumnRenamed("_c5", "icao_code") \
       .withColumnRenamed("_c6", "latitude") \
       .withColumnRenamed("_c7", "longitude") \
       .withColumnRenamed("_c8", "altitude") \
       .withColumnRenamed("_c9", "timezone") \
       .withColumnRenamed("_c10", "type") \
       .withColumnRenamed("_c11", "region") \
       .withColumnRenamed("_c12", "object_type") \
       .withColumnRenamed("_c13", "source")


# Вывод первых 5 строк
df.show(5)


# Вывод только определенных колонок
selected_columns = df.select("name", "city", "country", "iata_code", "timezone")
selected_columns.show(5)


kazAirports = selected_columns.filter(col("_c3") == "Kazakhstan")
kazAirports .show()


kazAirports = selected_columns.filter(col("_c3") == "Russia")
kazAirports .show()





