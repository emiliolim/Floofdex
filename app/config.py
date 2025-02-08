import os
"""
among other things, sets up sqlalchemy database
"""


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        'sqlite:///stuffed_animals.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for tests
    SQLALCHEMY_TRACK_MODIFICATIONS = False