from fastapi import Header
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .db import Database
from .models import Book, UpdateBook

router = InferringRouter()
db_client = Database()


@cbv(router)
class BookRouter:

    @router.post("/")
    async def create_book(self, book: Book):
        return await db_client.create_book(book)

    @router.get("/")
    async def get_all_books(self):
        return await db_client.get_all_books()

    @router.get("/{book_id}")
    async def get_single_book_by_id(self, book_id: str):
        return await db_client.get_single_book_by_id(book_id)

    @router.delete("/{book_id}")
    async def delete_book(self, book_id: str):
        return await db_client.delete_book(book_id)

    @router.patch("/{book_id}")
    async def partial_update_book(self, book_id:str, book: UpdateBook):
        return await db_client.partial_update_book(book_id, book)