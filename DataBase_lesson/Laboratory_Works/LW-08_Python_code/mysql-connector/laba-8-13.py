import mysql.connector

# Устанавливаем подключение к базе данных
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='python_db1'
)

try:
    cursor = conn.cursor()

    # 1. SELECT - Получение всех товаров с категориями
    select_query = """
    SELECT products.product_name, products.price, categories.category_name
    FROM products
    JOIN categories ON products.category_id = categories.id;
    """
    cursor.execute(select_query)
    results = cursor.fetchall()

    print("Список товаров и их категорий:")
    for row in results:
        print(f"Product: {row[0]}, Price: {row[1]}, Category: {row[2]}")

    # 2. UPDATE - Обновление цены товара "Smartphone"
    update_query = """
    UPDATE products
    SET price = 749.99
    WHERE product_name = 'Smartphone';
    """
    cursor.execute(update_query)
    conn.commit()  # Подтверждаем изменения
    print("Цена для товара 'Smartphone' обновлена до 749.99.")

    # 3. DELETE - Удаление товара "TV"
    delete_query = """
    DELETE FROM products
    WHERE product_name = 'TV';
    """
    cursor.execute(delete_query)
    conn.commit()  # Подтверждаем изменения
    print("Товар 'TV' успешно удален.")

except mysql.connector.Error as err:
    print(f"Ошибка: {err}")

finally:
    # Закрываем курсор и соединение
    cursor.close()
    conn.close()
