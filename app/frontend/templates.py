from flask import Blueprint, render_template, redirect, url_for

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    
    return render_template('index.html', view='editor')

@frontend_bp.route('/<path:invalid_path>')
def catch_all(invalid_path):
    return redirect(url_for('frontend.index'))