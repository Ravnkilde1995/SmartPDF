from flask import Flask
from layers.frontend.routes import frontend_bp
from layers.backend.pdf import pdf_bp
from layers.backend.upload import upload_bp

def create_app():
    app = Flask(__name__)

    app.config['OUTPUT_FOLDER'] = 'app/persistence/delivery_notes'

    app.register_blueprint(frontend_bp, url_prefix='/')
    app.register_blueprint(pdf_bp, url_prefix='/pdf')
    app.register_blueprint(upload_bp, url_prefix='/upload')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)