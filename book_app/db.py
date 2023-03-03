import configurations.base_db as base_db
from configurations.base_db import DatabaseConfiguration, start_db
from bson.objectid import ObjectId
from .models import Book, UpdateBook


class Database(DatabaseConfiguration):


    @start_db()
    async def get_book(self, book_id):
        query = await base_db.client.book_collection.find_one({"_id": book_id})
        query["_id"] = str(query["_id"])
        return query


    @start_db()
    async def create_book(self, book: Book):
        query = await base_db.client.book_collection.insert_one(book.dict())
        result = await self.get_book(query.inserted_id)
        return result

    @start_db()
    async def get_all_books(self):
        query = base_db.client.book_collection.find()
        book_list = []
        async for book in query:
            book["_id"] = str(book["_id"])
            book_list.append(book)
        return book_list