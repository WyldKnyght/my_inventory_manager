# src/routes/init.py
from flask import Blueprint

bp = Blueprint('main', __name__)

from routes import inventory_routes, category_routes, brand_routes, supplier_routes, status_routes
