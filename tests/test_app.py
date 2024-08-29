import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    with app.test_client() as client:
        yield client

def test_index(client):
    reponse = client.get('/')
    assert reponse.status_code == 200