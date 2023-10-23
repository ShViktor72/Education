from pprint import pprint
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

# восстановление БД из архива
# C:\Users\Viktor\Downloads>pg_restore -d demo dvdrental.tar

# установка библиотек
# pip install sqlalchemy psycopg2-binary

# создаем engine
# типCубд-пользователь-пароль-url-база

engine = create_engine("postgresql+psycopg2://demo:demo@localhost:5432/demo")

# устанавливаем соединение
connection = engine.connect()

# какие таблицы есть в БД
# pprint(sqlalchemy.inspect(engine).get_table_names())

# Список полей таблицы film
# column_ls = connection.execute(text("""
#     SELECT COLUMN_NAME
#         FROM INFORMATION_SCHEMA.COLUMNS
#         WHERE table_name = 'film'
# """))
# print(list(column_ls))

# выберем названия фильмов из таблицы film, первые 10 записей
# sel = connection.execute(text("select title from film;")).fetchmany(10)
# pprint(sel)

# выберем первые 10 записей из таблицы film
# sel = connection.execute(text("select * from film;")).fetchmany(10)
# pprint(sel)
# print(type(sel))

# выберем название и год выхода фильмов из таблицы film, первые 10 записей
# sel = connection.execute(text("select title, release_year from film;")).fetchmany(10)
# pprint(sel)

# выберем имена и фамилии актеров из таблицы actor, первые 10 записей
# sel = connection.execute(text("select first_name, last_name from actor;")).fetchmany(10)
# pprint(sel)

# DISTINCT- только уникальные значения
# sel = connection.execute(text("select rating from film;")).fetchmany(10)
# pprint(sel)
#
# sel = connection.execute(text("select DISTINCT rating from film;")).fetchmany(10)
# pprint(sel)

# Арифметика
# переведем оплату в тенге
# sel = connection.execute(text("SELECT amount * 475 from payment;")).fetchmany(10)
# pprint(sel)
# pprint(float(sel[0][0]))

# вычислим время аренды
# sel = connection.execute(text("SELECT return_date - rental_date from rental;")).fetchmany(10)
# pprint(sel)
# print(sel[0][0])
# print(sel[0][0].days)
# print(sel[1][0].seconds)

# Оператор WHERE
# sel = connection.execute(text("""SELECT title, release_year  from film
#     WHERE release_year > 2000;
#     """)).fetchmany(10)
# pprint(sel)
# exit(0)

# критерий не обязан входить в выборку
# найдем всех действующих сотрудников
# sel = connection.execute(text("""SELECT first_name, last_name  from staff
#     WHERE active = true;
#     """)).fetchmany(10)
# pprint(sel)

# найдем всех действующих сотрудников, кроме магазина № 1
# sel = connection.execute(text("""SELECT first_name, last_name  from staff
#     WHERE active = true AND NOT store_id = 1;
#     """)).fetchmany(10)
# pprint(sel)

# найдем фильмы, прокат которых стоит меньше 4.99 и стоимость возмещения меньше 14.99
# sel = connection.execute(text("""SELECT title, rental_rate, replacement_cost  from film
#     WHERE rental_rate < 4.99 AND replacement_cost < 14.99;
#     """)).fetchmany(10)
# pprint(sel)

# найдем фильмы с рейтингом "R", "NC-17"
# sel = connection.execute(text("""SELECT title, description  from film
#     WHERE rating IN ('R', 'NC-17');
#     """)).fetchmany(10)
# pprint(sel)

# BETWEEN
# найдем фильмы со стоимостью проката от 2.99 до 4.99
# sel = connection.execute(text("""SELECT title, description, rental_rate from film
#     WHERE rental_rate BETWEEN 2.99 AND 4.99;
#     """)).fetchmany(10)
# pprint(sel)

# LIKE
# найдем фильмы, в описании которых есть scientist
# sel = connection.execute(text("""SELECT title, description from film
#     WHERE description LIKE '%%Scientist%%';
#     """)).fetchmany(10)
# pprint(sel)

# сортировка, LIMIT
# отсортируем фильмы по цене проката и длительности
# sel = connection.execute(text("""SELECT title, description, rental_rate, length from film
#     WHERE rental_rate BETWEEN 2.99 AND 4.99
#     ORDER BY rental_rate, length
#     LIMIT 10;
#     """)).fetchall()
# pprint(sel)

# самый длинный фильм
# sel = connection.execute(text("""SELECT title, length from film
#     ORDER BY length DESC
#     LIMIT 1;
#     """)).fetchall()
# pprint(sel)

# INSERT
# Список полей таблицы rental
# column_ls = connection.execute(text("""
#     SELECT COLUMN_NAME
#         FROM INFORMATION_SCHEMA.COLUMNS
#         WHERE table_name = 'rental'
# """))
# print(list(column_ls))

# примеры записей
# sel = connection.execute(text("SELECT * FROM rental;")).fetchmany(10)
# pprint(sel)

# sel = connection.execute(text("""INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
#     VALUES(now(), 1525, 459, 2);
#     """))
#
# sel = connection.execute(text("SELECT * FROM rental ORDER BY rental_id DESC;")).fetchmany(1)
# pprint(sel)