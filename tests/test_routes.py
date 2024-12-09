# test_routes.py

"""
test_routes.py

This module contains test routes for the Flask application.

Author: Bouchaib Khribech
Version: 1.0
Date: December 2024
"""

from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import predict

# Create a Blueprint for the test routes
test_routes = Blueprint('test_routes', __name__)

@test_routes.route('/test')
def test():
    """
    Render the test page.
    """
    return render_template('test.html', title="Test")

@test_routes.route('/test_upload', methods=['GET', 'POST'])
def test_upload():
    """
    Handle file upload and perform prediction for testing purposes.
    """
    if request.method == 'POST':
        file = request.files['file']  # Access the uploaded file
        if file:
            # Perform prediction without saving the file
            result = predict(file)

            # Redirect to the test result page with the prediction
            return redirect(url_for('test_routes.test_result', result=result))
    return render_template('test_upload.html', title="Test Upload")

@test_routes.route('/test_result')
def test_result():
    """
    Display the prediction result for testing purposes.
    """
    result = request.args.get('result', 'No result')
    return render_template('test_result.html', title="Test Result", result=result)
