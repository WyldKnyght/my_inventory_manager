import sqlite3
import os
from dotenv import load_dotenv
import msvcrt

# Load environment variables from .env file
load_dotenv()

# Get the database path from the environment variable
db_path = os.getenv("DB_PATH")

# Ensure the directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def get_input_with_cancel(prompt):
    print(prompt, end='', flush=True)
    user_input = []
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch()
            if char == b'\x1b':  # Esc key
                print("\nOperation canceled by the user.")
                exit()
            elif char in {b'\r', b'\n'}:  # Enter key
                print()  # Move to the next line
                return ''.join(user_input)
            else:
                user_input.append(char.decode())
                print(char.decode(), end='', flush=True)

# Check if the database file already exists
if os.path.exists(db_path):
    response = get_input_with_cancel(f"The database file '{db_path}' already exists. Do you want to overwrite it (o), rename it (r), or cancel (c)? ").strip().lower()
    if response == 'o':
        # Delete the existing database file
        os.remove(db_path)
        print(f"Existing database '{db_path}' has been removed.")
    elif response == 'r':
        print("Press [Esc] at any time to cancel the operation.")
        # Prompt for a new file name until a valid one is provided or user cancels
        while True:
            new_db_name = get_input_with_cancel("Enter a new name for the database file (without extension, e.g., 'inventory_v2'): ").strip()
            # Automatically append .db extension
            if not new_db_name.endswith('.db'):
                new_db_name += '.db'
            new_db_path = os.path.join(os.path.dirname(db_path), new_db_name)

            # Check if the new file name already exists
            if not os.path.exists(new_db_path):
                db_path = new_db_path
                break
            else:
                response = get_input_with_cancel(f"The file '{new_db_path}' already exists. Do you want to try another name (y) or cancel (c)? ").strip().lower()
                if response == 'c':
                    print("Operation canceled by the user.")
                    exit()
    elif response == 'c':
        print("Operation canceled by the user.")
        exit()
    else:
        print("Invalid option. Exiting without changes.")
        exit()

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Read the SQL schema from the schema.sql file
schema_file_path = "M:/dev_env/my_inventory_manager/database/schema.sql"
with open(schema_file_path, 'r') as schema_file:
    create_tables_sql = schema_file.read()

# Execute the SQL statements to create tables
cursor.executescript(create_tables_sql)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database and tables created successfully at '{db_path}'.")