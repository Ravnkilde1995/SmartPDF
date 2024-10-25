import os
from werkzeug.utils import secure_filename

class FileService:
    ALLOWED_EXTENSIONS = {'pdf'}

    def __init__(self, upload_folder):
        self.upload_folder = upload_folder

    def allowed_file(self, filename):
        has_dot = '.' in filename

        if not has_dot:
            return False

        file_extension = filename.rsplit('.', 1) [1].lower()
        is_allowed = file_extension in self.ALLOWED_EXTENSIONS

        return is_allowed

    def save_file(self, file):
        if not self.allowed_file(file.filename):
            raise ValueError("file type not allowed")
        
        filename = secure_filename(file.filename)
        os.makedirs(self.upload_folder, exist_ok=True)
        file_path = os.path.join(self.upload_folder, filename)
        file.save(file_path)
        return file_path