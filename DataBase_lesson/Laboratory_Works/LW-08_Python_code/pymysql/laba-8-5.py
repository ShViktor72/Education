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
        # Выполнение DELETE запроса для удаления товара 'Samsung Galaxy'
        delete_query = """
        DELETE FROM products
        WHERE product_name = 'Samsung Galaxy';
        """
        cursor.execute(delete_query)

        print("Товар 'Samsung Galaxy' успешно удален.")

    # Подтверждаем изменения
    conn.commit()

except pymysql.MySQLError as e:
    print(f"Ошибка при выполнении DELETE запроса: {e}")

finally:
    # Закрываем соединение
    conn.close()
