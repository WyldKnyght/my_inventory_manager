# utils/create_app.py
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

def create_app(config_class=Config):
    # Go up one directory level from utils and then into templates
    templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')

    app = Flask(__name__, template_folder=templates_dir)
    app.config.from_object(config_class)
    app.debug = True  # Enable debugging

    db.init_app(app)
    migrate.init_app(app, db)

    try:
        register_blueprints(app)
    except ImportError as e:
        logger.error(f"Error importing routes: {e}")

    return app

def register_blueprints(app):
    logger.debug("Importing routes")
    from routes import inventory_routes, category_routes, brand_routes, supplier_routes, inventory_status_routes, admin_routes
    logger.debug("Registering routes")
    app.register_blueprint(inventory_routes)
    app.register_blueprint(category_routes)
    app.register_blueprint(brand_routes)
    app.register_blueprint(supplier_routes)
    app.register_blueprint(inventory_status_routes)
    app.register_blueprint(admin_routes)
    logger.debug("Routes registered")
