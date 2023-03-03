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

