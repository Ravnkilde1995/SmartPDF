from flask import current_app, request, jsonify
from app.services.file_service import FileService
from app.services.rename_service import FileRenamer
from . import upload_bp

@upload_bp.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    files = request.files.getlist('files[]')
    if not files:
        return jsonify({'error': 'No files part'}), 400

    file_service = FileService(current_app.config['UPLOAD_FOLDER'])
    file_renamer = FileRenamer()
    results = []

    for file in files:
        if file.filename == '':
            results.append({'filename': 'Unknown', 'error': 'No selected file'})
            continue

        if file_service.allowed_file(file.filename):
            try:
                file_path = file_service.save_file(file)
                
                new_filename = file_renamer.rename_file(file_path)

                results.append({'filename': new_filename, 'status': 'success'})
            except Exception as e:
                results.append({'filename': file.filename, 'error': f"Error processing file: {e}"})
        else:
            results.append({'filename': file.filename, 'error': 'File type not allowed'})

    return jsonify(results), 200