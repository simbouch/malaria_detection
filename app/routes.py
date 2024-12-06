from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import predict

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', title="Home")

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']  # Access the uploaded file
        if file:
            # Perform prediction without saving the file
            result = predict(file)
            
            # Redirect to the result page with the prediction
            return redirect(url_for('main.result', result=result))
    return render_template('upload.html', title="Upload")

@main.route('/result')
def result():
    result = request.args.get('result', 'No result')
    return render_template('result.html', title="Result", result=result)
