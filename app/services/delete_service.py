import os

class DeleteService:
    def __init__(self, upload_folder):
        self.upload_folder = upload_folder


    def delete_content(self):
        zip_filepath = os.path.join(self.upload_folder)
        for file_name in os.listdir(zip_filepath):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(self.upload_folder, file_name)
                os.remove(file_path)

        return