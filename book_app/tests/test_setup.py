from bson import ObjectId
from configurations.base_test import TestConfiguration


class TestSetup(TestConfiguration):
    fake_book = {
        "title": "test book",
        "author": "test author",
        "uid": None
    }
    fake_book_to_get = {
        "title": "test get book",
        "author": "test get author",
        "uid": "1244q57923597982953"
    }

    def get_book(self, book_id):
        return self.book_collection.find_one({"_id": ObjectId(book_id)})

    def create_fake_book(self):
        return self.book_collection.insert_one(self.fake_book)

    def create_fake_book_to_get(self):
        return self.book_collection.insert_one(self.fake_book_to_get)

    def create_book_by_inforamation(self, book):
        return self.book_collection.insert_one(book)