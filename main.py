from fastapi import FastAPI
from book_app.router import router as book_router

app = FastAPI()
app.include_router(book_router, prefix="")