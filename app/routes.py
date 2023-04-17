from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
import pyocr
import pyocr.builders
from app import app
from app.controllers import ocr_image, process_gpt

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            error = "ファイルがアップロードされていません。"
            return render_template('upload.html', error=error)

        file = request.files['file']
        if file.filename == '':
            error = "ファイルが選択されていません。"
            return render_template('upload.html', error=error)

        if not allowed_file(file.filename):
            error = "許可されていないファイル形式です。"
            return render_template('upload.html', error=error)

        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            extracted_text = ocr_image(image_path)
            summary = process_gpt(extracted_text, "summarize")
            corrected_text = process_gpt(extracted_text, "correct")
            return render_template("result.html", extracted_text=extracted_text, summary=summary, corrected_text=corrected_text)
        except Exception as e:
            error = str(e)
            return render_template('upload.html', error=error)
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def ocr_image(image_path):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        raise RuntimeError("No OCR tool found")

    tool = tools[0]
    img = Image.open(image_path)
    extracted_text = tool.image_to_string(
        img,
        lang='jpn+eng',
        builder=pyocr.builders.TextBuilder()
    )

    if not extracted_text:
        raise ValueError("No text could be extracted from the image")

    return extracted_text