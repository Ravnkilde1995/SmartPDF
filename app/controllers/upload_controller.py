from flask import render_template, request, redirect, url_for, flash
from . import upload_bp

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            flash('File successfully uploaded')
            return redirect(url_for('frontend.editor'))
        else:
            flash('No file selected')
    return render_template('index.html', view='upload')