import time
import os

def test_upload_process(client, test_folder):

    test_pdf_file = os.path.join(test_folder, 'generated_1.pdf')
    generated_pdf_file = os.path.join(test_folder, 'generated.pdf')

    data = {
        'files[]': [
            (open(test_pdf_file, 'rb'), 'generated_1.pdf'),
            (open(generated_pdf_file, 'rb'), 'generated.pdf')
        ]
    }

    start_time = time.time()

    upload_response = client.post('/upload/upload_pdf', data=data, content_type='multipart/form-data')

    elapsed_time = time.time() - start_time

    assert upload_response.status_code == 200  

    assert elapsed_time < 10, f"Upload og behandling tog for lang tid: {elapsed_time:.2f} sekunder"

    print(f"Processen tog {elapsed_time:.2f} sekunder.")