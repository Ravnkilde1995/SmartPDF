from flask import current_app, send_file
from app.services.download_service import DownloadService
from app.services.delete_service import DeleteService
from . import download_bp

@download_bp.route('/zip', methods=['GET'])
def download_zip():
    download_service = DownloadService(current_app.config['UPLOAD_FOLDER'])
    zip_filepath = download_service.download_zip()

    response = send_file(zip_filepath, as_attachment=True)
    
    delete_service = DeleteService(current_app.config['UPLOAD_FOLDER'])
    delete_service.delete_content()

    return response
     
