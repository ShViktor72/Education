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
        # Вставка данных в таблицу категорий
        insert_categories = """
        INSERT INTO categories (category_name)
        VALUES ('Audio'), ('TV'), ('Smartphones'), ('Accessories');
        """
        cursor.execute(insert_categories)

        # Вставка данных в таблицу товаров
        insert_products = """
        INSERT INTO products (product_name, price, category_id)
        VALUES 
        ('Наушники', 699.99, 1),
        ('Активные колонки', 499.99, 1),
        ('ЖК-телевизор', 299.99, 2),
        ('Smart TV', 899.99, 2),
        ('Apple iPhone', 1029.99, 3),
        ('Samsung Galaxy', 729.99, 3),
        ('Защитные стекла', 0.99, 4),
        ('Чехлы', 1.99, 4),
        ('Зарядные устройства', 3.99, 4);
        """
        cursor.execute(insert_products)

        print("Данные успешно вставлены в таблицы 'categories' и 'products'.")

    # Подтверждаем изменения
    conn.commit()

except pymysql.MySQLError as e:
    print(f"Ошибка при выполнении запроса: {e}")

finally:
    # Закрываем соединение
    conn.close()
