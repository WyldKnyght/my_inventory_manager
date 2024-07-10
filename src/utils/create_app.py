# src/utils/create_app.py
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os
from utils.render_pagination import render_pagination

db = SQLAlchemy()
migrate = Migrate()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os
from utils.render_pagination import render_pagination

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    # Go up one directory level from utils and then into templates
    templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')

    app = Flask(__name__, template_folder=templates_dir)
    app.config.from_object(config_class)
    app.debug = True 

    db.init_app(app)
    migrate.init_app(app, db)

    # Make render_pagination available to Jinja2 templates
    app.jinja_env.globals.update(render_pagination=render_pagination)

    try:
        register_blueprints(app)
    except ImportError as e:
        logger.error(f"Error importing routes: {e}")

    return app

def register_blueprints(app):
    logger.debug("Importing routes")
    from routes.admin_inventory_routes import inventory_routes
    from routes.admin_category_routes import category_routes
    from routes.admin_brand_routes import brand_routes
    from routes.admin_supplier_routes import supplier_routes
    from routes.admin_inventory_status_routes import inventory_status_routes
    from routes.admin_tab_routes import admin_routes
    from routes.inventory_tab_routes import inventory_tab_routes
    logger.debug("Registering routes")

    # Routes of admin functionality, hence prefixed with '/admin'
    app.register_blueprint(admin_routes, url_prefix='/admin')
    app.register_blueprint(inventory_routes, url_prefix='/inventory')
    app.register_blueprint(category_routes, url_prefix='/admin')
    app.register_blueprint(brand_routes, url_prefix='/admin')
    app.register_blueprint(supplier_routes, url_prefix='/admin')
    app.register_blueprint(inventory_status_routes, url_prefix='/admin')
    
    # Inventory tab routes, specific to viewing inventory details, kept separate
    app.register_blueprint(inventory_tab_routes, url_prefix='/inventory_tab')

    logger.debug("Routes registered")