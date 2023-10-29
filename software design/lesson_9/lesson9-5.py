#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pprint import pprint
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text


# In[2]:


# создаем engine
# типCубд://пользователь:пароль@url/база

engine = create_engine("postgresql+psycopg2://demo:demo@localhost:5432/demo")


# In[3]:


# устанавливаем соединение
connection = engine.connect()


# In[ ]:


# Агрегирующие функции


# In[15]:


# Найдем максимальную стоимость проката
sel = connection.execute(text("""
SELECT MAX(rental_rate) FROM film;
""")).fetchall()
pprint(sel)


# In[16]:


# Найдем среднюю продолжительность фильма
sel = connection.execute(text("""
SELECT AVG(length) FROM film;
""")).fetchall()
pprint(sel)


# In[17]:


# сколько уникальных имен актеров?
sel = connection.execute(text("""
SELECT COUNT(DISTINCT first_name) FROM actor;
""")).fetchall()
pprint(sel)


# In[18]:


# Найдем сумму и средние продажи конкретного продавца
sel = connection.execute(text("""
SELECT SUM(amount), AVG(amount) FROM payment
WHERE staff_id = 1;
""")).fetchall()
pprint(sel)


# In[ ]:


# Вложенные запросы


# In[22]:


# Найдем фильмы с продолжительстью выше среднего
# так работать не будет. Агрегатные ф-ии применяются только с SELECT
sel = connection.execute(text("""
SELECT title, length FROM film
WHERE length > AVG(length);
""")).fetchall()
pprint(sel)


# In[24]:


# А так работает
sel = connection.execute(text("""
SELECT title, length FROM film
WHERE length > (
SELECT AVG(length) FROM film);
""")).fetchmany(5)
pprint(sel)


# In[21]:


# названия фильмов, стоимость проката которых ниже максимальной
sel = connection.execute(text("""
SELECT title, rental_rate FROM film
WHERE rental_rate < (
SELECT MAX(rental_rate) FROM film)
ORDER BY rental_rate DESC;
""")).fetchmany(10)
pprint(sel)


# In[ ]:


# Группировки


# In[30]:


# подсчет количества актеров в разрезе фамилий (однофамильцы). Сортировка по количеству совпадений
sel = connection.execute(text("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name
ORDER BY COUNT(*) DESC;
""")).fetchmany(10)
pprint(sel)


# In[35]:


# подсчет количества актеров в разрезе фамилий (однофамильцы). Сортировка по количеству совпадений
sel = connection.execute(text("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name
ORDER BY COUNT(*) DESC;
""")).fetchall()
pprint(sel)


# In[37]:


# подсчет количества фильмов в разрезе рейтингов (распределение рейтингов)
sel = connection.execute(text("""
SELECT rating, COUNT(title) FROM film
GROUP BY rating
ORDER BY COUNT(title) DESC;
""")).fetchall()
pprint(sel)


# In[38]:


# найдем максимальные продажи в разрезе продавцов (максимальные продажи каждого продавца)
sel = connection.execute(text("""
SELECT staff_id, MAX(amount) FROM payment
GROUP BY staff_id;
""")).fetchall()
pprint(sel)


# In[41]:


# найдем минимальные продажи каждого продавца каждому покупателю (группировка по нескольким столбцам)
sel = connection.execute(text("""
SELECT staff_id, customer_id, MIN(amount) FROM payment
GROUP BY staff_id, customer_id;
""")).fetchall()
pprint(sel)


# In[43]:


# средня продолжительность фильмов в разрезе рейтингов в 2006 году (ср. прод-ть для каждого рейтинга)
sel = connection.execute(text("""
SELECT rating, AVG(length) FROM film
WHERE release_year = 2006
GROUP BY rating;
""")).fetchall()
pprint(sel)


# In[ ]:


# Оператор HAVING


# In[54]:


# Актеры, чьи фамилии не повторяются
sel = connection.execute(text("""
SELECT last_name, COUNT(*) FROM actor
GROUP BY last_name
HAVING COUNT(*) = 1;
""")).fetchmany(10)
pprint(sel)


# In[53]:


# только актеры, чьи имена повторяются
sel = connection.execute(text("""
SELECT first_name, COUNT(*) FROM actor
GROUP BY first_name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;
""")).fetchall()
pprint(sel)


# In[65]:


# Фильмы, у которых есть "Super" в названии, и которые сдавались в прокат более чем на 5 дней, суммарно
sel = connection.execute(text("""
SELECT title, SUM(rental_duration) FROM film
WHERE title LIKE '%%Super%%'
GROUP BY title
HAVING SUM(rental_duration) > 5

""")).fetchall()
pprint(sel)


# In[ ]:


# Alias (Псевдонимы)


# In[67]:


# предыдущий запрос, но с псевдонимами
# Фильмы, у которых есть "Super" в названии, и которые сдавались в прокат более чем на 5 дней, суммарно
sel = connection.execute(text("""
SELECT title t, SUM(rental_duration) rt FROM film f
WHERE title LIKE '%%Super%%'
GROUP BY t
HAVING SUM(rental_duration) > 5

""")).fetchall()
pprint(sel)


# In[ ]:


# Объединение таблиц с помощью JOIN


# In[74]:


# выведем имена, фамилии и адреса всех сотрудников
sel = connection.execute(text("""
SELECT first_name, last_name, address FROM staff
LEFT JOIN address ON staff.address_id = address.address_id
""")).fetchall()
pprint(sel)


# In[75]:


# тоже самое, но с использованием псевдонимов
# выведем имена, фамилии и адреса всех сотрудников
sel = connection.execute(text("""
SELECT first_name, last_name, address FROM staff s
LEFT JOIN address a ON s.address_id = a.address_id
""")).fetchall()
pprint(sel)


# In[80]:


# определим количество продаж каждого продавца
sel = connection.execute(text("""
SELECT title, COUNT(actor_id) FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY title
""")).fetchmany(10)
pprint(sel)


# In[ ]:


# посчитаем сколько актеров играли в каждом фильме
sel = connection.execute(text("""
SELECT s.last_name, COUNT(amount) FROM payment p
LEFT JOIN staff s ON p.staff_id = s.staff_id
GROUP BY s.last_name
""")).fetchall()
pprint(sel)


# In[ ]:


# Более сложные запросы, с использованием JOIN, WHERE, группировки и сортировки


# In[81]:


# Сколько фильмов со словом "Super" есть в наличии
sel = connection.execute(text("""
SELECT title, COUNT(inventory_id) FROM film f
JOIN inventory i ON f.film_id = i.film_id
WHERE title LIKE '%%Super%%'
GROUP BY title
""")).fetchall()
pprint(sel)


# In[83]:


# список покупателей с количеством покупок в алфавитном порядке
sel = connection.execute(text("""
SELECT c.last_name, COUNT(amount) FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY last_name
ORDER BY last_name
""")).fetchall()
pprint(sel)


# In[97]:


# список покупателей с количеством покупок в алфавитном порядке
sel = connection.execute(text("""
SELECT c.first_name, c.last_name, c.email, co.country, ci.city FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE country = 'Kazakstan'
""")).fetchall()
pprint(sel)


# In[101]:


# фильмы, которые берут чаще всех
sel = connection.execute(text("""
SELECT f.title, COUNT(i.inventory_id) FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.title
ORDER BY count DESC;
""")).fetchall()
pprint(sel)


# In[102]:


# суммарные доходы магазинов
sel = connection.execute(text("""
SELECT s.store_id, SUM(p.amount) FROM store s
JOIN staff st ON s.store_id = st.store_id
JOIN payment p ON st.staff_id = p.staff_id
GROUP BY s.store_id;
""")).fetchall()
pprint(sel)


# In[106]:


# Найдем города и страны каждого магазина
sel = connection.execute(text("""
SELECT store_id, city, country FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city c ON a.city_id = c.city_id
JOIN country co ON c.country_id = co.country_id;
""")).fetchall()
pprint(sel)


# In[115]:


# Топ 5 жанров по доходу
sel = connection.execute(text("""
SELECT c.name, SUM(p.amount) profit FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name
ORDER BY profit DESC
LIMIT 5;
""")).fetchall()
pprint(sel)


# In[ ]:




