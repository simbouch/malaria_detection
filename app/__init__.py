# __init__.py

"""
__init__.py

This module initializes the Flask application and sets up the necessary configurations.

Author: Bouchaib Khribech
Version: 1.0
Date: December 2024
"""

import os
from flask import Flask

def create_app():
    """
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    # Set the secret key for the application
    # Note: It's better to use environment variables for sensitive information
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

    # Import and register the main blueprint
    from .routes import main
    app.register_blueprint(main)

    return app

# Error handling to ensure the application can handle any issues during creation
try:
    app = create_app()
except Exception as e:
    print(f"Error creating app: {e}")
    raise
