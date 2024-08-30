def test_generate_pdf(client, tmp_path):
    form_data = {
        'recipient_name': 'John Doe',
        'req_number': 'REQ123456',
        'date': '2023-08-29',
        'serial_number': '',
        'item1': 'Iphone 15',
        'item1_qty': '1'
    }

    client.application.config['OUTPUT_FOLDER'] = str(tmp_path)

    response = client.post('/pdf/generate_pdf', data=form_data)

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/pdf'

    output_file = tmp_path / 'generated.pdf'
    
    assert output_file.exists()
    print(f"File '{output_file}' was successfully created.")