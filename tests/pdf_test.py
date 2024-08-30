import os

def test_generate_pdf(client, tmpdir):
    form_data = {
        'recipient_name': 'John Doe',
        'req_number': 'REQ123456',
        'date': '2023-08-29',
        'serial_number': '',
        'item1': 'Iphone 15',
        'item1_qty': '1'
    }

    client.application.config['OUTPUT_FOLDER'] = str(tmpdir)

    response = client.post('/pdf/generate_pdf', data=form_data)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'

    output_file = os.path.join(str(tmpdir), 'generated.pdf')
    
    assert os.path.exists(output_file)
    print(f"File '{output_file}' was successfully created.")