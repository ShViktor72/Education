# pip install pymongo
from pymongo import MongoClient

# Создаем подключение к MongoDB
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient('mongodb://pythonUser:1111@localhost:27017/libraryDB')

# Указываем базу данных, с которой будем работать
db = client.libraryDB

# Проверка подключения
print("Connected to MongoDB")

collection = db.books    # Указываем на коллекцию books

# Извлечение всех документов из коллекции
books = collection.find()  # Получаем все документы

# Перебираем и выводим каждый документ
for book in books:
    print(book)


# Перебираем и выводим все названия книг
books = collection.find()  # Получаем все документы
for book in books:
    print(book["title"])

# Чтение одного документа по условию
book = collection.find_one({"title": "The Hobbit"})
print(book)

# Обновляем статус книги
collection.update_one({"title": "The Hobbit"}, {"$set": {"available": False}})

# Проверяем обновление
updated_book = collection.find_one({"title": "The Hobbit"})
print(updated_book)

# Удаляем книгу "Animal Farm"
collection.delete_one({"title": "Animal Farm"})
print("Book deleted")

# Закрытие подключения
client.close()
print("Connection to MongoDB closed")

