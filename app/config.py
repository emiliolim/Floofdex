import os
"""
among other things, sets up sqlalchemy database
"""


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        'sqlite:///stuffed_animals.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg',
                          'gif'}  # Allowed file extensions

    # Ensure the upload folder exists
    @staticmethod
    def init_upload_folder(app):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for tests
    SQLALCHEMY_TRACK_MODIFICATIONS = False