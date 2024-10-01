import mysql.connector

# Устанавливаем подключение к базе данных
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='python_db1'
)

try:
    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

    # Вставка данных в таблицу categories (Категории)
    insert_categories = """
    INSERT INTO categories (category_name) 
    VALUES (%s), (%s), (%s);
    """
    categories_data = ('Electronics', 'Furniture', 'Books')
    cursor.execute(insert_categories, categories_data)

    # Вставка данных в таблицу products (Товары)
    insert_products = """
    INSERT INTO products (product_name, price, category_id) 
    VALUES (%s, %s, %s), (%s, %s, %s), (%s, %s, %s), (%s, %s, %s), (%s, %s, %s);
    """
    products_data = (
        'Smartphone', 699.99, 1,
        'TV', 499.99, 1,
        'Sofa', 299.99, 2,
        'Bookshelf', 89.99, 2,
        'Python Programming Book', 29.99, 3
    )
    cursor.execute(insert_products, products_data)

    # Подтверждаем изменения
    conn.commit()

    print("Данные успешно вставлены в таблицы 'categories' и 'products'.")

except mysql.connector.Error as err:
    print(f"Ошибка при вставке данных: {err}")

finally:
    # Закрываем курсор и соединение
    cursor.close()
    conn.close()
