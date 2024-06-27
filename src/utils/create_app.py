# src/utils/create_app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from routes import inventory_routes, category_routes, brand_routes, supplier_routes, inventory_status_routes, admin_routes
    app.register_blueprint(inventory_routes)
    app.register_blueprint(category_routes)
    app.register_blueprint(brand_routes)
    app.register_blueprint(supplier_routes)
    app.register_blueprint(inventory_status_routes)
    app.register_blueprint(admin_routes)

    return app
