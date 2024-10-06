import pymysql

# Устанавливаем подключение к базе данных
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='python_db1'
)

try:
    # Создаем курсор для выполнения SQL-запросов
    with conn.cursor() as cursor:
        # Выполнение UPDATE запроса для изменения цены товара
        update_query = """
        UPDATE products
        SET price = 929.99
        WHERE product_name = 'Apple iPhone';
        """
        cursor.execute(update_query)

        print("Цена для товара 'Apple iPhone' успешно обновлена.")

    # Подтверждаем изменения
    conn.commit()

except pymysql.MySQLError as e:
    print(f"Ошибка при выполнении UPDATE запроса: {e}")

finally:
    # Закрываем соединение
    conn.close()
