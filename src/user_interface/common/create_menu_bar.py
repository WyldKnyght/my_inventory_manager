# src/user_interface/main_window_modules/create_menu_bar.py
from PyQt6.QtWidgets import QMenuBar

def create_menu_bar(main_window, menu_config):
    menu_bar = QMenuBar(main_window)
    
    for menu_name, menu_items in menu_config.items():
        menu = menu_bar.addMenu(menu_name)
        for item in menu_items:
            if item == 'separator':
                menu.addSeparator()
            else:
                action = menu.addAction(item['label'])
                action.triggered.connect(getattr(main_window, item['method']))
    
    return menu_bar
