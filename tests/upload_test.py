import time
import os

def test_upload_process(client, test_folder):
    test_pdf_file = os.path.join(test_folder, 'test_pdf.pdf')

    data = {
        'files[]': (open(test_pdf_file, 'rb'), 'test_pdf.pdf')
    }

    start_time = time.time()

    upload_response = client.post('/upload/upload_pdf', data=data, content_type='multipart/form-data')

    elapsed_time = time.time() - start_time

    assert upload_response.status_code == 200
    json_data = upload_response.get_json()

    assert json_data[0]['status'] == 'success', f"File processing failed: {json_data}"    

    assert elapsed_time < 10, f"Upload og behandling tog for lang tid: {elapsed_time:.2f} sekunder"

    print(f"Processen tog {elapsed_time:.2f} sekunder.")
    