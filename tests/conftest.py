import pytest
import os
from run import create_app

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

@pytest.fixture(scope='session')
def test_folder():
    return os.path.join(os.path.dirname(__file__), 'test_data')