from flask import render_template, redirect, url_for
from . import  routes_bp

@routes_bp.route('/')
def index():
    return render_template('index.html', view='editor')

@routes_bp.route('/<path:invalid_path>')
def catch_all(invalid_path):
    return redirect(url_for('routes.index'))