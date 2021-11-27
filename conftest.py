import pytest
from fastapi.testclient import TestClient

from main import init_app


@pytest.fixture()
def client():
    app = init_app()

    with TestClient(app) as client_:
        yield client_
