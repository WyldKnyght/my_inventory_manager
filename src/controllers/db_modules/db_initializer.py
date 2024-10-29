# src/controllers/db_modules/db_initializer.py

from utils.custom_logging import logger

class DatabaseInitializer:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def initialize_database(self):
        """Create the initial database structure."""
        logger.info("Initializing database")
        
        if self.db_manager.table_exists('transactions'):
            return

        try:
            for schema_name in ['finance', 'inventory', 'global']:
                self._create_schema_tables(schema_name)

            # Execute INSERT statements for Global_Settings
            self._insert_global_settings()

            logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"An error occurred while initializing the database: {e}")
            raise

    def _create_schema_tables(self, schema_name):
        schema = self.db_manager.schema_manager.schemas[schema_name]
        for table_name, table_info in schema.items():
            if table_info['type'] == 'table':
                self._create_table(table_name, table_info['columns'])

    def _create_table(self, table_name, columns):
        columns_sql = ', '.join([f"{col} {info['type']} {' '.join(info['constraints'])}" for col, info in columns.items()])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})"
        self.db_manager.execute_command(create_table_sql)

    def _insert_global_settings(self):
        insert_sql = """
        INSERT OR IGNORE INTO Global_Settings (setting_name, setting_value, setting_type) VALUES
        ('default_dimension_unit', 'cm', 'string'),
        ('default_currency', 'CAD', 'string')
        """
        self.db_manager.execute_command(insert_sql)