import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# Подключение к MongoDB
client = AsyncIOMotorClient("mongodb://pythonUser:1111@localhost:27017/libraryDB")
db = client.libraryDB  # Указываем базу данных
collection = db.books   # Указываем коллекцию

# Создание документа (Create)
async def insert_book():
    book = {"title": "Dune", "author": "Frank Herbert", "year": 1965}
    result = await collection.insert_one(book)
    print(f"Книга добавлена с id: {result.inserted_id}")

# Обновление документа (Update)
async def update_book():
    result = await collection.update_one(
        {"title": "Dune"}, {"$set": {"year": 1984}}
    )
    print(f"Модифицировано документов: {result.modified_count}")

# Удаление документа (Delete)
async def delete_book():
    result = await collection.delete_one({"title": "Dune"})
    print(f"Удалено документов: {result.deleted_count}")

# Основная асинхронная функция, объединяющая все вызовы
async def main():
    # await insert_book()  # Добавляем книгу
    await update_book()    # Обновление документа
    await delete_book()    # удаление документа

# Запускаем асинхронную функцию main
asyncio.run(main())