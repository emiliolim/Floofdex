import os
from urllib.parse import quote_plus  # For encoding special characters in passwords
from dotenv import load_dotenv
"""
Set up SQL database and image storage paths
"""

load_dotenv()

class Config:
    # postgres DB details
    DB_USER = os.getenv('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    DB_PORT = os.getenv('POSTGRES_PORT', '5432')
    DB_DATABASE = os.getenv('POSTGRES_DATABASE', 'floofdex_db')

    encoded_password = quote_plus(DB_PASSWORD)

    # build sql database
    SQLALCHEMY_DATABASE_URI = f'postgresql+pg8000://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
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