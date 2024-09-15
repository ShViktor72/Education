import pymysql
import random
import time

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='1234',
    database='testdb',
    cursorclass=pymysql.cursors.DictCursor
)

# поиск по ключу

start_time = time.time()
num = random.randint(1, 3000000)
print(f"поиск по ключу {num}")

with connection.cursor() as cursor:
    select_all_rows = "SELECT * FROM `users` WHERE id = %s"
    cursor.execute(select_all_rows, (num,))  # Передаем num как кортеж
    rows = cursor.fetchall()

#print(rows)
user_name = rows[0].get('surname')
print(f"user_name - {user_name}")


end_time = time.time()
print("Время выполнения:", end_time - start_time, "секунд")


# поиск по имени
print("поиск по имени")
start_time = time.time()

with connection.cursor() as cursor:
    select_all_rows = "SELECT * FROM `users` WHERE name = %s"
    cursor.execute(select_all_rows, (user_name,))  # Передаем user_name как кортеж
    rows = cursor.fetchall()
    #print(rows)

end_time = time.time()
print("Время выполнения:", end_time - start_time, "секунд")