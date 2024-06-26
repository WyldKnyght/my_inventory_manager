# src/main.py
from utils.create_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
