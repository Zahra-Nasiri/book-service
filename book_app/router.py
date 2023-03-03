from fastapi import Header
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from .db import Database

router = InferringRouter()
db_client = Database()


@cbv(router)
class BookRouter:
    pass