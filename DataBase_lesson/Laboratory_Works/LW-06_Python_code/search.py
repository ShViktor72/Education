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

try:
    # Поиск по ключу
    start_time = time.time()
    num = random.randint(1, 3000000)
    print(f"поиск по ключу {num}")

    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `users` WHERE id = %s"
        cursor.execute(select_all_rows, (num,))
        rows = cursor.fetchall()

        if rows:
            user_name = rows[0].get('surname')
            print(f"user_name - {user_name}")
        else:
            print(f"Пользователь с id {num} не найден.")

    end_time = time.time()
    print("Время выполнения:", end_time - start_time, "секунд")

    # Поиск по имени
    print("поиск по имени")
    start_time = time.time()

    if rows:  # Проверяем, есть ли значение для user_name
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users` WHERE name = %s"
            cursor.execute(select_all_rows, (user_name,))
            rows = cursor.fetchall()

            if rows:
                print(f"Найдено {len(rows)} пользователей с именем {user_name}")
            else:
                print(f"Пользователь с именем {user_name} не найден.")
    else:
        print("Поиск по имени пропущен, так как пользователь не найден по id.")

    end_time = time.time()
    print("Время выполнения:", end_time - start_time, "секунд")

except pymysql.MySQLError as err:
    print(f"Ошибка при выполнении запроса: {err}")

finally:
    connection.close()