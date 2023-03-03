from bson import ObjectId
from configurations.base_test import TestConfiguration


class TestSetup(TestConfiguration):
    fake_book = {
        "title": "test book",
        "author": "test author",
        "uid": None
    }

    def get_book(self, book_id):
        return self.book_collection.find_one({"_id": ObjectId(book_id)})