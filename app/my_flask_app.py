from flask import Flask, render_template, request
import os
from config.conf import UPLOAD_FOLDER
from main.entry_handler import aud_text, sentiment_trigger

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def trigger_summariser_sentiment_analyser(file_path):
    summary = aud_text(file_path)
    sentiment_trigger(summary)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')

        file = request.files['file']

        # If the user does not select a file, browser submits an empty part without filename
        if file.filename == '':
            return render_template('index.html', message='No selected file')

        # Save the uploaded file to the uploads folder
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        trigger_summariser_sentiment_analyser(file_path)
        return render_template('index.html', message=f'File successfully uploaded. Path: {file_path}')
    return render_template('index.html', message='')


if __name__ == '__main__':
    app.run(debug=True)

