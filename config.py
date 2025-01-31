import os
"""
among other things, sets up sqlalchemy database
"""


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        'sqlite:///stuffed_animals.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
