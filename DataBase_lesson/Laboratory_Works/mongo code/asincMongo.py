import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# Подключение к MongoDB
client = AsyncIOMotorClient("mongodb://pythonUser:1111@localhost:27017/libraryDB")
db = client.libraryDB  # Указываем базу данных
collection = db.books   # Указываем коллекцию

# Проверяем подключение, читая список коллекций
async def test_connection():
    collections = await db.list_collection_names()
    print(f"Список коллекций: {collections}")

# Извлечение и вывод всех книг из коллекции
async def find_books():
    async for book in collection.find():
        print(book)

# Чтение документов с фильтром
async def find_books_by_author(author):
    # Фильтр: книги по конкретному автору
    query = {"author": author}

    # Выполняем запрос и выводим результаты
    async for book in collection.find(query):
        print(book)

# Основная асинхронная функция, объединяющая все вызовы
async def main():
    print("Проверяем подключение")
    await test_connection()  # Проверяем подключение
    print("Все книги:")
    await find_books()       # Читаем книги
    print("книги Оруэлла:")
    await find_books_by_author("George Orwell") # Чтение книг, написанных "J.R.R. Tolkien"

# Запускаем асинхронную функцию main
asyncio.run(main())

