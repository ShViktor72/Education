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
        # SQL-запрос для создания таблицы категорий
        create_categories_table = """
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            category_name VARCHAR(100) NOT NULL
        );
        """
        cursor.execute(create_categories_table)

        # SQL-запрос для создания таблицы товаров
        create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            category_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
        """
        cursor.execute(create_products_table)

        print("Таблицы 'categories' и 'products' успешно созданы.")

    # Подтверждаем изменения
    conn.commit()

except pymysql.MySQLError as e:
    print(f"Ошибка при выполнении запроса: {e}")

finally:
    # Закрываем соединение
    conn.close()