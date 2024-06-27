# src/main.py

import sys
import os
from flask import Flask, render_template

# Append the path to the parent directory of src to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.create_app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
