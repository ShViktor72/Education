
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg


# Создание SparkSession
spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("WordCount") \
    .getOrCreate()


# Проверка сессии
print(spark)


# Чтение файла из HDFS
df = spark.read.json("hdfs://namenode:8020/flights.json")



# Вывод схемы и типов данных для датасета о продажах автомобилей
print("Схема данных для датасета 'sales.csv':")
df.printSchema()

# Подсчет общего количества записей
total_records = df.count()

# Вывод результата
print(f"Общее количество записей: {total_records}")



# Удаление записей с отсутствующими значениями в ключевых полях 
cleaned_flights_df = df.dropna(subset=["DEP_DELAY", "DISTANCE"])


print("Количество записей в датасете  после очистки:")
print(cleaned_flights_df.count())


# Поиск 5 самых длинных рейсов по расстоянию
longest_flights_df = df.orderBy("DISTANCE", ascending=False).limit(5)

# Вывод результата
longest_flights_df.show()



# Вычисление средней задержки вылета и средней задержки прибытия
average_delays = df.select(avg("DEP_DELAY").alias("average_dep_delay"),
                           avg("ARR_DELAY").alias("average_arr_delay"))


# Вывод результата
average_delays.show()


# Вычисление среднего времени задержки по каждой дате
average_delay_by_date = df.groupBy("FL_DATE") \
    .agg(
        avg("DEP_DELAY").alias("average_dep_delay"),
        avg("ARR_DELAY").alias("average_arr_delay")
    ) \
    .orderBy("FL_DATE")


# Вывод результата
average_delay_by_date.show(60)


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Конвертация в Pandas DataFrame для визуализации
average_delay_df = average_delay_by_date.toPandas()

# Построение графика с помощью Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x="FL_DATE", y="average_dep_delay", data=average_delay_df, label="Средняя задержка вылета", marker="o")
sns.lineplot(x="FL_DATE", y="average_arr_delay", data=average_delay_df, label="Средняя задержка прибытия", marker="o")
plt.xlabel("Дата")
plt.ylabel("Средняя задержка (мин)")
plt.title("Средняя задержка вылета и прибытия по дням")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()





