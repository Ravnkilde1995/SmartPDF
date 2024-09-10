import os
from flask import Flask
from app.controllers.pdf_controller import pdf_bp
from app.controllers.upload_controller import upload_bp
# from app.controllers.download_controller import download_bp
from app.views.routes import frontend_bp

def create_app():
    app = Flask(__name__, template_folder='app/views/html_templates')

    app.config['PDF_TEMPLATE_FOLDER'] = os.path.join(app.static_folder, 'template_file')
    app.config['OUTPUT_FOLDER'] = 'app/models/delivery_notes'
    app.config['UPLOAD_FOLDER'] = 'app/models/upload_folder'

    app.register_blueprint(frontend_bp)
    app.register_blueprint(pdf_bp, url_prefix='/pdf')
    app.register_blueprint(upload_bp, url_prefix='/upload')
    # app.register_blueprint(download_bp, url_prefix='/download')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)