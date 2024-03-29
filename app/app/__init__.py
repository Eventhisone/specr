import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

from .routes.routes import app_routes
from .routes.racquets import app_racquets
from .routes.manufacturers import app_manufacturers
from .routes.pattern_types import app_pattern_types

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Include our Routes
        app.register_blueprint(app_routes)
        app.register_blueprint(app_racquets)
        app.register_blueprint(app_manufacturers)
        app.register_blueprint(app_pattern_types)

        # Migration
        # migrate = Migrate(app, db, compare_type=True)

        return app