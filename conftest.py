import pytest
from fastapi.testclient import TestClient

from main import run


@pytest.fixture()
def client():
    app = run()

    with TestClient(app) as client_:
        yield client_
