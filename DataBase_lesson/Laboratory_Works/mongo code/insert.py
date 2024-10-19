from pymongo import MongoClient

# Создаем подключение к MongoDB
client = MongoClient('mongodb://pythonUser:1111@localhost:27017/libraryDB')

# Создание документа
# Указываем базу данных, с которой будем работать
db = client.libraryDB

# Проверка подключения
print("Connected to MongoDB")

# Выбираем коллекцию
collection = db.books

# Создаем новый документ
new_book = {
    "title": "Animal Farm",
    "author": "George Orwell",
    "year": 1945,
    "genres": ["satire", "allegory", "novella"],
    "available": False
}
result = collection.insert_one(new_book)

# Выводим ID созданного документа
print(f"Book created with id: {result.inserted_id}")

# Добавление нескольких документов
# Список документов для добавления
books = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genres": ["Classic", "Romance"],
     "available": False, "price": 6.99},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "author": "J.R.R. Tolkien", "year": 1954,
     "genres": ["Fantasy", "Adventure"], "available": True, "price": 12.99},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997,
     "genres": ["Fantasy", "Young Adult"], "available": True, "price": 11.99},
]

# Добавление книг в коллекцию
result = collection.insert_many(books)
print(f"Добавлено документов: {len(result.inserted_ids)}")
