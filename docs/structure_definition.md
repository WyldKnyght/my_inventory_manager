## Structure:
Recommended Structure
Controllers: This directory is typically used for classes that handle the logic and interaction between the UI and the database.
Dialogs: is directory is used for classes that define the UI components of your application.
Utilities: These should be placed in the utils directory, which is intended for reusable code that can be used throughout the application.

Directory Structure
src/
├── controllers/
│   ├── placeholder_controller.py
│   └── ...
├── user_interface/
│   ├── dialogs/
│   │   ├── placeholder_dialog.py
│   │   └── ...
│   └── ...
├── utils/
│   ├── util_placeholder.py
│   └── ...

## controllers
### database
- data_formatter.py
This code defines a function format_data that takes a list of column headers and a list of raw data rows, and formats the raw data into a list of dictionaries. Each dictionary corresponds to a row of data, with keys derived from the column headers.

- data_preparation.py
This code defines a set of functions to prepare data for insertion into different database tables, specifically for products, categories, brands, and companies. It includes validation for certain fields and provides safe conversion functions for numeric values.

- database_controller.py
The DatabaseController class follows the Single Responsibility Principle by encapsulating all database-related operations. Each method has a clear purpose, and there are no obvious candidates for extraction into separate functions.

- field_creators.py
This code defines several functions for creating and populating user interface components in a PyQt application, specifically combo boxes and input fields. It includes functionality to fetch data from a SQLite database to populate these components.

- query_builder.py
This code defines a function construct_query that generates SQL queries based on the specified data type and table name. It returns a specific query for predefined data types (Categories, Brands, Companies) or a generic query for other table names.

- validation.py

### inventory
- inventory_controller.py
This code defines an InventoryController class that manages interactions with a database for inventory-related data. It provides methods to fetch, add, update, and delete data based on specified data types, mapping these types to corresponding database tables.

### user_interface
 dialogs
- inventory_management_dialog.py
This code defines an InventoryManagementDialog class that provides a user interface for managing inventory data. It allows users to view, add, edit, and delete entries for various data types such as products, categories, brands, and companies.

- purchases_dialog.py

-record_dialog
 - base_record_dialog.py
This code defines a RecordDialog class that creates a dialog for adding or editing records in a specified database table. It dynamically generates input fields based on the table's non-autoincrement columns and allows users to save or cancel their changes.

 - inventory_record_dialog.py
This code defines an InventoryRecordDialog class that extends a base dialog for managing inventory records in a GUI application using PyQt. It dynamically creates input fields based on the column types of a specified database table and handles data population and retrieval for those fields.

### framework

- main_window.py
This code defines a MainWindow class for a simple PyQt application that serves as the main interface. It sets up a window with a tabbed layout, allowing users to navigate between different sections: Home, Inventory, and Settings.

- base_widget.py
This code defines a BaseWidget class that extends QtWidgets.QWidget and provides utility methods for creating common UI components in a PyQt application. It includes methods for creating group boxes, layouts, labels, buttons, and line edits, along with helper methods for setting properties and connecting signals.

- home_tab.py

-inventory_tab.py

-purchases_tab.py

-reports_tab.py

-sales_tab.py

-settings_tab.py
This code defines a SettingsTab class that creates a settings interface for a PyQt application. It sets up a grid layout containing buttons that, when clicked, open various configuration dialogs related to different aspects of the application, such as inventory management and user interface settings.