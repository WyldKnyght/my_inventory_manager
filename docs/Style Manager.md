# StyleManager

The StyleManager is responsible for loading, managing, and applying styles to the application. It provides a centralized way to handle the application's visual appearance using QSS (Qt Style Sheets).

## Features

- Loads styles from a QSS file
- Applies styles to the entire application
- Supports dynamic placeholder replacement for theming
- Provides access to raw style content

## Usage

### Initialization

To use the StyleManager, first import it in your Python file:

```python
from configs.style_manager import StyleManager
```

### Loading Styles

Load the styles from the QSS file:

```python
StyleManager.load_style()
```

This method should be called once at the application startup.

### Applying Styles

To apply the loaded styles to your application:

```python
StyleManager.apply_style()
```

If you need to replace placeholders in the style, you can pass keyword arguments:

```python
StyleManager.apply_style(
    BACKGROUND_COLOR="#A7C6ED",
    PRIMARY_COLOR="#4F8CC9",
    FONT_SIZE="12"
)
```

### Getting Raw Style Content

If you need access to the raw style content:

```python
raw_style = StyleManager.get_raw_style()
```

## Example

Here's a complete example of how to use the StyleManager in your application:

```python
from PyQt6.QtWidgets import QApplication
from configs.style_manager import StyleManager

def initialize_app():
    app = QApplication([])
    
    # Load the style
    StyleManager.load_style()
    
    # Apply the style with custom colors
    StyleManager.apply_style(
        BACKGROUND_COLOR="#A7C6ED",
        PRIMARY_COLOR="#4F8CC9",
        SECONDARY_COLOR="#B0D0E8",
        TEXT_COLOR="#003D7A",
        FONT_SIZE="12"
    )
    
    # Your other initialization code here
    
    return app

if __name__ == "__main__":
    app = initialize_app()
    # Rest of your application code
    app.exec()
```

## Notes

- The StyleManager uses a singleton pattern, so you don't need to create an instance of it.
- Make sure your QSS file uses placeholders (e.g., `{{BACKGROUND_COLOR}}`) for values you want to replace dynamically.
- The StyleManager does not handle theme switching itself. If you want to implement theme switching, you'll need to call `apply_style()` with new values when the theme changes.
```