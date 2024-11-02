
# pip install pyspark


from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, regexp_replace, trim, lower, concat_ws, collect_list, udf
from pyspark.sql.types import FloatType

# Создание SparkSession
spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName("WordCount") \
    .getOrCreate()


# Проверка сессии
print(spark)


# Чтение текстового файла, где каждая строка файла - это строка DataFrame
df = spark.read.text("hdfs://namenode:8020/pilevin.txt").withColumnRenamed("value", "line") 


# Очистка текста
cleaned_df = df \
    .withColumn("line", trim(col("line"))) \
    .withColumn("line", regexp_replace(col("line"), r"[^a-zA-Zа-яА-Я0-9\s]", "")) \
    .withColumn("line", lower(col("line")))

# Удаление пустых строк
cleaned_df = cleaned_df.filter(col("line") != "")


# Вывод первых нескольких строк очищенного текста
cleaned_df.show(truncate=False)


# Вывод первых нескольких строк очищенного текста
cleaned_df.show(10)


# Разделение строк на отдельные слова
words_df = cleaned_df.withColumn("word", explode(split(col("line"), "\s+")))

# Удаление пустых значений (если есть)
words_df = words_df.filter(col("word") != "")

# Подсчет количества каждого слова
word_count_df = words_df.groupBy("word").count().orderBy(col("count").desc())


# Вывод результата
word_count_df.show(10, truncate=False)  # Покажем 10 самых частых слов


# Получение уникальных слов и сортировка их в алфавитном порядке
unique_words_df = words_df.select("word").distinct().orderBy("word")

# Количество уникальных слов
unique_words_df.count()


# Вывод результата
unique_words_df.show(10, truncate=False)  # Покажем первые 10 слов для примера


# Сохранение списка уникальных слов в файл
unique_words_df.coalesce(1).write.mode("overwrite").text("hdfs://namenode:8020/unique1.txt")


# Анализ тональности текста

# !pip install textblob


# Чтение файла из HDFS
df = spark.read.text("hdfs://namenode:8020/pilevin.txt")


# Собираем все строки в один текст
full_text = " ".join(row['value'] for row in df.collect())

# Анализ тональности всего текста
blob = TextBlob(full_text)
print(f"Полярность: {blob.sentiment.polarity}, Субъективность: {blob.sentiment.subjectivity}")


"""
Пояснение:
Полярность (Polarity: -0.6145833333333334):
Полярность отражает эмоциональный тон текста и принимает значения от -1 до 1:
-1 означает крайне негативную тональность.
0 означает нейтральную тональность.
1 означает крайне позитивную тональность.
В данном случае значение -0.614 указывает на довольно выраженную негативную тональность текста, то есть текст содержит много негативных слов или фраз.

Субъективность (Subjectivity: 0.5666666666666667):
Субъективность указывает, насколько текст субъективен или объективен:
Значение 0 означает полностью объективный, фактологический текст.
Значение 1 означает полностью субъективный, основанный на мнениях, чувствах и предположениях текст.
"""


