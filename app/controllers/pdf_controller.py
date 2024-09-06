from flask import request, send_from_directory, current_app
from app.services.pdf_service import PDFService
import os
from . import pdf_bp

@pdf_bp.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    form_data = request.form

    pdf_service = PDFService(output_folder=current_app.config['OUTPUT_FOLDER'],
                             template_folder=current_app.config['PDF_TEMPLATE_FOLDER'])
    
    output_file = pdf_service.generate_pdf(form_data)

    return send_from_directory(current_app.config['OUTPUT_FOLDER'], os.path.basename(output_file))