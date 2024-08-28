import os

UPLOAD_FOLDER = 'app/datalag/temp'

def handle_file_upload(file):
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))