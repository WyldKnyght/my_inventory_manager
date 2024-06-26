# src/utils/create_app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from routes import inventory_routes, category_routes, brand_routes, supplier_routes, inventory_status_routes
    app.register_blueprint(inventory_routes.bp)
    app.register_blueprint(category_routes.bp)
    app.register_blueprint(brand_routes.bp)
    app.register_blueprint(supplier_routes.bp)
    app.register_blueprint(inventory_status_routes.bp)

    return app
