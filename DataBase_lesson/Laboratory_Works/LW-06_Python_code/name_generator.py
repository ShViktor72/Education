import pymysql
from faker import Faker
import time

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    database='testdb',
    cursorclass=pymysql.cursors.DictCursor
)

# with connection.cursor() as cursor:
#     select_all_rows = "SELECT * FROM `users`"
#     cursor.execute(select_all_rows)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     print("#" * 20)

start_time = time.time()

# Генерация списка имен
faker = Faker("ru_RU")
names = [faker.name() for i in range(100)]

names_surnames_list = []
for user in names:
    names_surnames_list.append([user.split()[0], user.split()[1]])

# Начало транзакции
with connection.cursor() as cursor:
    cursor.execute("START TRANSACTION")

    # Формирование SQL-запроса для массовой вставки
    sql = "INSERT INTO users (name, surname) VALUES (%s, %s)"
    values = [(user_data[0], user_data[1]) for user_data in names_surnames_list]
    cursor.executemany(sql, values)

    # Завершение транзакции
    cursor.execute("COMMIT")

# Закрытие соединения
connection.close()

end_time = time.time()
print("Время выполнения:", end_time - start_time, "секунд")

"""
%s	Строка	Универсальный заполнитель для строк.

Основные методы faker:
Генерация персональных данных
name(): Генерирует случайное имя. Например, faker.name() может вернуть "Иван Петров".
last_name(): Генерирует случайную фамилию.
first_name(): Генерирует случайное имя.
address(): Генерирует полный адрес, включая улицу, город, штат и т.д.
city(): Генерирует название города.
country(): Генерирует название страны.
email(): Генерирует случайный email-адрес, комбинируя имя и фамилию с популярными доменами.
phone_number(): Генерирует случайный номер телефона в определенном формате.
"""
