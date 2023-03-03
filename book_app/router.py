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