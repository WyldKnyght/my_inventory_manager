# src/config.py
import os
from pathlib import Path

basedir = Path(__file__).resolve().parent.parent
DATABASE_URL = f"sqlite:///{os.path.join(basedir, 'database', 'small_business.db')}"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# TODO: Consider adding more configuration options as needed, such as logging configurations.