from fastapi.testclient import TestClient
from main import app
import time
from .test_setup import TestSetup

test_client = TestClient(app)


class TestRouter(TestSetup):

    def test_admin_can_add_book(self):
        response = test_client.post("/", json=self.fake_book)
        response = response.json()
        assert self.get_book(response)["title"] == self.fake_book["title"]
        assert self.get_book(response)["author"] == self.fake_book["author"]
        assert self.get_book(response)["uid"] == self.fake_book["uid"]

        