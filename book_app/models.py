from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    uid: str | None = None


class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    uid: str | None = None