from fastapi.testclient import TestClient
from main import app
import time
from .test_setup import TestSetup

test_client = TestClient(app)


class TestRouter(TestSetup):

    def test_admin_can_add_book(self):
        response = test_client.post("/", json=self.fake_book)
        response = response.json()
        book = self.get_book(response["_id"])
        assert book["title"] == self.fake_book["title"]
        assert book["author"] == self.fake_book["author"]
        assert book["uid"] == self.fake_book["uid"]

    def test_user_can_get_all_books(self):
        query = self.create_fake_book()
        response = test_client.get("/")
        response = response.json()
        assert response[-1]["_id"] == str(query.inserted_id)
        assert response[-1]["title"] == self.fake_book["title"]

    def test_user_can_get_single_book_by_id(self):
        query = self.create_fake_book_to_get()
        book = self.get_book(query.inserted_id)
        book["_id"] = str(book["_id"])
        response = test_client.get(f'/{book["_id"]}')
        response = response.json()
        assert response["title"] == book["title"]
        assert response["author"] == book["author"]
        assert response["uid"] == book["uid"]

    def test_admin_can_delete_book(self):
        book_dict = {
            "title": "tobe deleted book",
            "author": "tobe delted author",
            "uid": "tobe dleted uid"
        }
        query = self.create_book_by_inforamation(book_dict)
        test_client.delete(f"/{query.inserted_id}")
        book =  self.get_book(query.inserted_id)
        assert not book
