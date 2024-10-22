import os
import time

def test_upload_pdf(client, app, generated_pdf):
   
    output_folder = app.config['OUTPUT_FOLDER']
    generated_pdf_file = os.path.join(output_folder, generated_pdf)

    assert os.path.exists(generated_pdf_file), "Generated PDF file does not exist."
    
    start_time = time.time()

    with open(generated_pdf_file, 'rb') as pdf_file:
        data = {'files[]': (pdf_file, 'generated.pdf')}
        upload_response = client.post('/upload/upload_pdf', data=data)

    end_time = time.time()
    actual_time = end_time - start_time

    assert upload_response.status_code == 200
    print(f"Upload process took {actual_time:.2f} seconds.")
    assert actual_time < 5