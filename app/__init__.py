from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""
Initializes flask app and sets up sqlalchemy
"""
# create app
app = Flask(__name__)

# load config
app.config.from_object('config.Config')

# database
db = SQLAlchemy(app)

# create database tables
with app.app_context():
    db.create_all()


# def create_app():
# Load configuration
# app.config.from_object('config.Config')

# initialize extensions
# db.init_app(app)

# Create database tables
# with app.app_context():
#     db.create_all()
#
# # register routes
# from .routes import main
#
# app.register_blueprint(main)
#
# from .errors import register_error_handlers
#
# register_error_handlers(app)
#
# return app
