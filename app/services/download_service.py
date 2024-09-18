import os
import zipfile

class DownloadService:
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder

    def download_zip(self):
        zip_filename = 'processed_delivery_notes.zip'
        zip_filepath = os.path.join(self.upload_folder, zip_filename)
        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for file_name in os.listdir(self.upload_folder):
                if file_name.endswith('.pdf'):
                    file_path = os.path.join(self.upload_folder, file_name)
                    zipf.write(file_path, arcname=file_name)
                
        return zip_filepath
