from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(config_class='app.config.Config'):  # Adjust path if needed
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes import routes
    app.register_blueprint(routes)

    from app.errors import errors
    app.register_blueprint(errors)

    with app.app_context():
        db.create_all()  # Create all database tables

    return app
