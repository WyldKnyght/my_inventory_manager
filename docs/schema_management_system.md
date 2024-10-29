# Schema Management System

## Overview

The Schema Management System is a crucial component of our application that provides access to the database schema definition. This system ensures that the schema serves as the single source of truth for the database structure across the entire application, without directly interacting with the database itself.

## Purpose

The primary purposes of the Schema Management System are:

1. To load and store the database schema from an SQL file.
2. To provide a centralized, consistent reference for the database structure.
3. To offer an interface for querying schema information without directly interacting with the database.

## Components

The Schema Management System consists of the following components:

1. **SchemaManager**: The main class that provides an interface to the schema.
2. **Loader Module**: Responsible for loading and parsing the schema from an SQL file.
3. **Query Module**: Contains functions for querying different aspects of the schema.

## Key Concepts

- **Schema as Source of Truth**: The schema SQL file is the definitive reference for the database structure. Any changes to the database should start with updating this file.
- **Read-Only Operations**: The Schema Management System does not modify the schema or interact with the database directly. It only provides read access to the schema information.
- **Separation of Concerns**: Database operations and schema management are kept separate. The Schema Management System focuses solely on providing schema information.

## Usage

### Initializing the SchemaManager

```python
from src.controllers.schema_manager import SchemaManager

manager = SchemaManager()
manager.load_schema()
```

### Querying Schema Information

```python
# Get all table names
table_names = manager.get_table_names()

# Get schema for a specific table
table_schema = manager.get_table_schema("transactions")

# Get column names for a table
column_names = manager.get_column_names("transactions")

# Get the type of a specific column
column_type = manager.get_column_type("transactions", "amount")

# Get constraints for a specific column
constraints = manager.get_column_constraints("transactions", "id")
```

## Best Practices

1. **Single Instance**: Use a single instance of SchemaManager throughout your application to ensure consistency.
2. **Early Initialization**: Load the schema early in your application's startup process.
3. **Error Handling**: Implement proper error handling when querying schema information, as the requested table or column might not exist.
4. **Schema Updates**: When updating the schema, ensure all parts of your application that rely on schema information are updated accordingly.

## Schema File Format

The schema should be defined in an SQL file with standard CREATE TABLE and CREATE VIEW statements. For example:

```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
);

CREATE VIEW recent_transactions AS
SELECT * FROM transactions
WHERE date >= date('now', '-30 days');
```

## Limitations

- The Schema Management System does not handle database migrations or schema changes at runtime.
- It does not validate the actual database structure against the schema. This should be handled separately if required.
- It does not create, modify, or interact with the actual database in any way.

## Conclusion

The Schema Management System provides a robust way to manage and access your database schema information. By centralizing schema management and treating the schema as the source of truth, it helps maintain consistency across your application and simplifies database-related operations, all while maintaining a clear separation from actual database interactions.
