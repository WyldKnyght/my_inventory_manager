# Inventory Management System Documentation

## Suggested Folder Structure

The following folder structure is designed to keep the Inventory Management System organized, maintainable, and scalable. This structure adheres to best practices for Python project organization and supports the principles of Single Responsibility, Separation of Concerns, and DRY (Don't Repeat Yourself).

### Adjusted Folder Structure

```
InventoryManagementSystem/
│
├── src/                        
│   ├── main.py                 
│   ├── framework/              
│   │   ├── item.py             
│   │   └── category.py         
│   │
│   ├── user_interface/         
│   │   ├── main_window.py      
│   │   ├── item_view.py        
│   │   └── category_view.py    
│   │
│   ├── controllers/            
│   │   ├── item_controller.py  
│   │   └── category_controller.py 
│   │
│   ├── utils/                  
│   │   ├── logger.py           
│   │   └── helpers.py          
│   │
│   └── resources/              # Directory for styles and themes
│       ├── styles.qss          # Qt Style Sheets for consistent styling
│       └── themes/             # Theme files for UI customization
│           ├── light.qss
│           └── dark.qss
│
├── database/                   
│   ├── inventory.db            
│   ├── db.py                   
│   └── schema.sql              
│
├── tests/                      
│   ├── test_items.py           
│   └── test_categories.py      
│
├── docs/                       
│   ├── README.md               
│   └── user_guide.md           
│
├── config/                     # Directory for configuration files
│   └── settings.json           # Configuration file for layout parameters
│
├── requirements.txt            
└── .gitignore                  
```

### Key Adjustments and Suggestions

1. **Resources Directory**:
   - **Purpose**: Store all style-related files, such as Qt Style Sheets (QSS) and theme files, in a dedicated `resources/` directory. This helps maintain a consistent look and feel across the application and simplifies theme management.

2. **Configuration Directory**:
   - **Purpose**: Use a `config/` directory to store configuration files like `settings.json`. This allows for easy management of layout parameters and other settings without altering the code, enhancing flexibility.

3. **Framework Directory**:
   - **Clarification**: Ensure that the `framework/` directory contains only the data models and business logic related to items and categories, keeping it separate from UI and controller logic.

4. **User Interface Directory**:
   - **Clarification**: The `user_interface/` directory should focus solely on UI components. Consider using Qt Designer to create `.ui` files, which can be converted to Python code, for a cleaner separation of design and logic.

5. **Controllers Directory**:
   - **Clarification**: The `controllers/` directory should handle user input and interactions, acting as the intermediary between the UI and the data models.

6. **Utils Directory**:
   - **Purpose**: Continue to use this directory for utility functions and helpers that are utilized across different parts of the application.

### Folder Descriptions

- **src/**: Contains all the source code for the application.
  - **main.py**: The main entry point for running the application.
  - **framework/**: Contains data models that define the structure and behavior of items and categories.
    - **item.py**: Logic related to item management.
    - **category.py**: Logic related to category management.
  - **user_interface/**: Contains user interface components built with Qt.
    - **main_window.py**: The main application window UI.
    - **item_view.py**: UI for managing items.
    - **category_view.py**: UI for managing categories.
  - **controllers/**: Contains logic for handling user input and application flow.
    - **item_controller.py**: Functions for CRUD operations related to items.
    - **category_controller.py**: Functions for CRUD operations related to categories.
  - **utils/**: Contains utility functions and helper scripts.
    - **logger.py**: Utility for logging application events.
    - **helpers.py**: General helper functions used throughout the application.
  - **resources/**: Contains style sheets and theme files.
    - **styles.qss**: Qt Style Sheets for consistent styling.
    - **themes/**: Theme files for UI customization.

- **database/**: Contains all database-related files.
  - **inventory.db**: The SQLite database file where your data will be stored.
  - **db.py**: Handles database connections and interactions, such as connecting to the database and executing queries.
  - **schema.sql**: SQL script used to create the necessary tables and initial setup for the database.

- **tests/**: Contains test cases to ensure the functionality of the application.
  - **test_items.py**: Test cases specifically for item-related functionality.
  - **test_categories.py**: Test cases specifically for category-related functionality.

- **docs/**: Contains documentation for the project.
  - **README.md**: Provides an overview of the project, installation instructions, and usage.
  - **user_guide.md**: Detailed instructions on how to use the application.

- **config/**: Contains configuration files for the application.
  - **settings.json**: Configuration file for layout parameters and other settings.

- **requirements.txt**: Lists the Python packages required for the project.

- **.gitignore**: Specifies files and directories to be ignored by Git, preventing them from being tracked in version control.
