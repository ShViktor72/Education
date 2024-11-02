
#!pip install pyspark pandas matplotlib seaborn


from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Создание SparkSession
spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("WordCount") \
    .getOrCreate()


# Чтение CSV файла
df = spark.read.csv("hdfs://namenode:8020/cars.csv", header=True, inferSchema=True)


# Вывод схемы и типов данных для датасета 
print("Схема данных для датасета 'cars.csv':")
df.printSchema()


# Подсчет общего количества записей
total_records = df.count()

# Вывод результата
print(f"Общее количество записей: {total_records}")


# Удаление записей с отсутствующими значениями в ключевых полях 
cleaned_cars_df = df.dropna(subset=["price_usd", "odometer_value"])
# Проверка результатов
print("Количество записей в датасете 'cars.csv' после очистки:")
print(cleaned_cars_df.count())


from pyspark.sql.functions import col, avg, round as spark_round


# Вычисление средней цены для каждой марки автомобиля и округление до целого числа
average_price_by_manufacturer = df.groupBy("manufacturer_name") \
    .agg(spark_round(avg("price_usd"), 0).alias("average_price_usd"))


# Сортировка по средней цене в порядке убывания
average_price_by_manufacturer = average_price_by_manufacturer.orderBy(col("average_price_usd").desc()).limit(10)


# Вывод результата
average_price_by_manufacturer.show()


# Преобразование в Pandas DataFrame для визуализации
average_price_pandas = average_price_by_manufacturer.toPandas()


# Визуализация с помощью Seaborn: столбчатая диаграмма
plt.figure(figsize=(12, 6))
sns.barplot(data=average_price_pandas, x='manufacturer_name', y='average_price_usd', palette='viridis')
plt.title("Средняя цена автомобилей по маркам")
plt.xlabel("Марка автомобиля")
plt.ylabel("Средняя цена (USD)")
#plt.xticks(rotation=90)
plt.show()


# Сортировка по средней цене в порядке убывания
average_price_by_manufacturer = average_price_by_manufacturer.orderBy(col("average_price_usd").desc()).limit(10)


# Преобразование в Pandas DataFrame для визуализации
average_price_pandas = average_price_by_manufacturer.toPandas()


# Визуализация с помощью Matplotlib: круговая диаграмма
plt.figure(figsize=(8, 8))
plt.pie(
    average_price_pandas['average_price_usd'],
    labels=average_price_pandas['manufacturer_name'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("viridis", len(average_price_pandas))
)
plt.title('Распределение средней цены по маркам автомобилей')
plt.show()




