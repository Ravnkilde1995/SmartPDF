import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture(scope='function')
def client(app):
    """A test client for the app."""
    return app.test_client()