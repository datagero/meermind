import os, json
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'rsp', 'rtf', 'png', 'jpeg', 'jpg'])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Downloads'))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

@app.route('/upload', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'GET':
        return '<p> GET request </p>';

    if request.method == 'POST':
        file = request.files.getlist('files')
        filename = ""

        print(request.files, "....")
        for f in file:
            if f.filename is not None:
                print(f.filename)
                filename = secure_filename(f.filename)
                print(allowedFile(filename))

                if allowedFile(filename):
                    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                else:
                    return jsonify({'message': 'File type not allowed'}), 400

        return jsonify({"name": filename, "status": "success"})
    else:
        return jsonify({"status": "Upload API GET Request Running"})


@app.route('/get-notes', methods=['GET'])
def upload_transcript():
    return "<p> Hello World </p>";

if __name__ == '__main__':
   app.run(port=5000)
