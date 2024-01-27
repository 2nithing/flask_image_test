import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key='12345'

@app.route('/', methods=['GET', 'POST'])


def upload_file():
    file_display = os.path.join(app.config['UPLOAD_FOLDER'], 'rock.png')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_display = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    return render_template('index.html',file_display=file_display)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__=='__main__':
    app.run()