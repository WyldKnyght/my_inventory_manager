# src/main.py
from flask import render_template
from create_app import create_app
import webbrowser
import threading
import os
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

@app.route('/')
def home():
    """Return the rendered index.html template."""
    return render_template('index.html')

def open_browser():
    try:
        # Get the first available web browser
        browser = webbrowser.get()

        # Open the URL in the browser
        browser.open('http://127.0.0.1:5000/')
    except Exception as e:
        print(f"Failed to open browser: {e}")

if __name__ == '__main__':
    # Check if the script is running in the main process
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        threading.Timer(1, open_browser).start()  
    app.run(debug=True)
