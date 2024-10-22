import pytest
from main import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture(scope='function')
def client(app):
    # Test client
    return app.test_client()

@pytest.fixture
def form_data(): 
    return {
        'recipient_name': 'John Doe',
        'req_number': 'REQ123456',
        'date': '2023-08-29',
        'serial_number': 'SN12345',
        'item1': 'Item 1',
        'item1_qty': '1',
        'item2': 'Item 2',
        'item2_qty': '2',
    }

@pytest.fixture
def generated_pdf(client, form_data):

    response = client.post('/pdf/generate_pdf', data=form_data)
    assert response.status_code == 200
    return 'generated.pdf'  