from flask import Flask
from app.frontend.templates import frontend_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(frontend_bp, url_prefix='/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)