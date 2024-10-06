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
        # Выполнение SELECT запроса для получения товаров и их категорий
        select_query = """
        SELECT products.product_name, products.price, categories.category_name
        FROM products
        JOIN categories ON products.category_id = categories.id;
        """
        cursor.execute(select_query)

        # Получаем и выводим результаты
        results = cursor.fetchall()
        for row in results:
            print(f"Product: {row[0]}, Price: {row[1]}, Category: {row[2]}")

except pymysql.MySQLError as e:
    print(f"Ошибка при выполнении SELECT запроса: {e}")

finally:
    # Закрываем соединение
    conn.close()
