# models.py

"""
models.py

This module defines the database models for the Flask application using SQLAlchemy.

Author: Bouchaib Khribech
Version: 1.0
Date: December 2024
"""

from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

class User(db.Model):
    """
    User model representing a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user, which must be unique and not nullable.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)

# Example usage of the User model
# This part is not used in this app but is included for future reference
# user = User(username='example_user')
# db.session.add(user)
# db.session.commit()
