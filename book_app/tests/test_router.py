from fastapi.testclient import TestClient
from main import app
import time
from .test_setup import TestSetup

test_client = TestClient(app)


class TestRouter(TestSetup):
    pass