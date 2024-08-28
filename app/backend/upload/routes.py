from flask import Blueprint, render_template, request, redirect, url_for, flash

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Her kan du håndtere filupload logikken
        file = request.files.get('file')
        if file:
            # Gem filen til temp-mappen eller processer den som ønsket
            flash('File successfully uploaded')
            return redirect(url_for('frontend.editor'))
        else:
            flash('No file selected')
    return render_template('index.html', view='upload')