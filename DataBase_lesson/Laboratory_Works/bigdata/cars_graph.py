# !pip install pyspark pandas matplotlib seaborn


from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql.functions import avg


# Создание SparkSession
spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("WordCount") \
    .getOrCreate()


# Чтение CSV файла
df = spark.read.csv("hdfs://namenode:8020/cars.csv", header=True, inferSchema=True)


df.show()


# Рассчитываем среднюю цену автомобилей по годам выпуска
average_price_by_year = df.groupBy("year_produced").agg(avg("price_usd").alias("average_price"))


# Округляем значения средней цены и сортируем по году
average_price_by_year = average_price_by_year.withColumn("average_price", average_price_by_year["average_price"].cast("int")) \
                                             .orderBy("year_produced")


# Выводим результат
average_price_by_year.show()


# Преобразуем результат в Pandas DataFrame
average_price_by_year_pd = average_price_by_year.orderBy("year_produced").toPandas()



# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(average_price_by_year_pd["year_produced"], average_price_by_year_pd["average_price"], marker='o', color='b')
plt.title("Средняя цена автомобилей по годам выпуска")
plt.xlabel("Год выпуска")
plt.ylabel("Средняя цена (USD)")
plt.grid(True)
plt.show()


# Посчитаем среднюю цену автомобилей конкретной марки
# Фильтруем данные для марки Porsche
porsche_df = df.filter(df["manufacturer_name"] == "Porsche")

# Рассчитываем среднюю цену автомобилей Porsche по годам выпуска
average_price_by_year_porsche = porsche_df.groupBy("year_produced").agg(avg("price_usd").alias("average_price"))

# Округляем значения средней цены и сортируем по году
average_price_by_year_porsche = average_price_by_year_porsche.withColumn("average_price", average_price_by_year_porsche["average_price"].cast("int")) \
 


# Выводим результат
average_price_by_year_porsche.show()


# Конвертируем результат в Pandas DataFrame
average_price_by_year_porsche_pd = average_price_by_year_porsche.orderBy("year_produced").toPandas()


# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(average_price_by_year_porsche_pd["year_produced"], average_price_by_year_porsche_pd["average_price"], marker='o', color='g')
plt.title("Средняя цена автомобилей Porsche по годам выпуска")
plt.xlabel("Год выпуска")
plt.ylabel("Средняя цена (USD)")
plt.grid(True)
plt.show()


# диаграмма рассеяния зависимости цены автомобиля от пробега
# Выбираем нужные столбцы и преобразуем данные в формат Pandas
price_odometer_df = df.select("price_usd", "odometer_value").toPandas()


# Фильтруем данные для удаления записей с нулевыми или отсутствующими значениями
price_odometer_df = price_odometer_df.dropna()
price_odometer_df = price_odometer_df[price_odometer_df["price_usd"] > 0]
price_odometer_df = price_odometer_df[price_odometer_df["odometer_value"] > 0]


# Построение диаграммы рассеяния с Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x="odometer_value", y="price_usd", data=price_odometer_df, alpha=0.6, color="b")
plt.title("Зависимость цены автомобиля от пробега")
plt.xlabel("Пробег (км)")
plt.ylabel("Цена (USD)")
plt.grid(True)
plt.show()


# диаграмма рассеяния для автомобилей марки Lexus


# Фильтруем данные для автомобилей марки Lexus
lexus_df = df.filter(df["manufacturer_name"] == "Lexus")

# Выбираем нужные столбцы и преобразуем в формат Pandas
price_odometer_lexus_df = lexus_df.select("price_usd", "odometer_value").toPandas()


# Фильтруем данные для удаления записей с нулевыми или отсутствующими значениями
price_odometer_lexus_df = price_odometer_lexus_df.dropna()
price_odometer_lexus_df = price_odometer_lexus_df[price_odometer_lexus_df["price_usd"] > 0]
price_odometer_lexus_df = price_odometer_lexus_df[price_odometer_lexus_df["odometer_value"] > 0]


# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))
sns.scatterplot(x="odometer_value", y="price_usd", data=price_odometer_lexus_df, alpha=0.6, color="red")
plt.title("Зависимость цены от пробега для автомобилей Lexus", fontsize=18, weight="bold", color="darkblue")
plt.xlabel("Пробег (км)")
plt.ylabel("Цена (USD)")
plt.grid(True)
plt.show()




