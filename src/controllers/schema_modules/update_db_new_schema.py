import sqlite3

def update_schema(db_path, schema_file_path):
    with open(schema_file_path, 'r') as schema_file:
        schema_sql = schema_file.read()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Execute the schema update SQL
        cursor.executescript(schema_sql)
        conn.commit()
        print("Schema updated successfully")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

# Usage
update_schema('financial_db.sqlite', 'updated_schema.sql')