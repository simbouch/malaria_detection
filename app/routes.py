# routes.py

"""
routes.py

This module defines the routes for the Flask application.

Author: Bouchaib Khribech
Version: 1.0
Date: December 2024
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import predict

# Create a Blueprint for the main routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html', title="Home")

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Handle file upload and perform prediction.
    """
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
    """
    Display the prediction result.
    """
    result = request.args.get('result', 'No result')
    return render_template('result.html', title="Result", result=result)
