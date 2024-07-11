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
logging.DEBUG

def create_app(config_class=Config):

    templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

    app = Flask(__name__, template_folder=templates_dir)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.jinja_env.globals.update(render_pagination=render_pagination)

    try:
        register_blueprints(app)
    except ImportError as e:
        logger.error(f"Error setting up the application: {e}")
        raise

    return app

def register_blueprints(app):
    try:
        logger.debug("Importing routes")
        # Tab routes
        from routes.tabs.admin_routes import admin_tab_routes
        from routes.tabs.inventory_routes import inventory_tab_routes
        from routes.tabs.purchase_routes import purchase_tab_routes
        from routes.tabs.report_routes import report_tab_routes
        from routes.tabs.sale_routes import sale_tab_routes  

        # Admin routes
        from routes.admin.inventory_routes import inventory_routes
        from routes.admin.category_routes import category_routes
        from routes.admin.brand_routes import brand_routes
        from routes.admin.supplier_routes import supplier_routes
        from routes.admin.inventory_status_routes import inventory_status_routes
        
        logger.debug("Registering routes")

        # Tab routes
        app.register_blueprint(inventory_tab_routes, url_prefix='/inventory')
        app.register_blueprint(purchase_tab_routes, url_prefix='/purchase')
        app.register_blueprint(report_tab_routes, url_prefix='/report')
        app.register_blueprint(sale_tab_routes, url_prefix='/sale')  
        app.register_blueprint(admin_tab_routes, url_prefix='/admin')

        # Admin routes
        app.register_blueprint(inventory_routes, url_prefix='/admin/inventory')
        app.register_blueprint(category_routes, url_prefix='/admin/category')
        app.register_blueprint(brand_routes, url_prefix='/admin/brand')
        app.register_blueprint(supplier_routes, url_prefix='/admin/supplier')
        app.register_blueprint(inventory_status_routes, url_prefix='/admin/inventory-status')    

        logger.debug("Routes registered")
    except Exception as e:
        logger.error(f"Error registering blueprints: {str(e)}")
        raise