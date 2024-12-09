# main.py

"""
main.py

This module initializes and runs the Flask application.

Author: Bouchaib Khribech
Version: 1.0
Date: December 2024
"""

from app import create_app

# Initialize the app using the factory function
app = create_app()

if __name__ == "__main__":
    # Run the app with the specified host and port
    app.run(host="0.0.0.0", port=5000)
