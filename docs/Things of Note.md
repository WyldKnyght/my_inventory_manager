### Instructions to Use `logging_config.yaml`

1. **Create the YAML File**:
   - Ensure you have a file named `logging_config.yaml` in your project directory (e.g., `src/resources`).
   - The content should look like this:
     ```yaml
     logging:
       level: DEBUG
       ring_buffer_capacity: 100
     ```

2. **Install Required Library**:
   - Make sure the `pyyaml` library is installed. If not, run:
     ```bash
     pip install pyyaml
     ```

3. **Call the Setup Function**:
   - In your main application file (e.g., `main.py`), import and call the `setup_logging` function at the start of your script:
   ```python
   from src.utils.logger import setup_logging

   if __name__ == "__main__":
       setup_logging()  # Initialize logging
       # Your application code here...
   ```

4. **Log Messages**:
   - Use the logger in your code to log messages:
   ```python
   logger = logging.getLogger('my_inventory_manager')
   logger.info("This is an info message.")
   logger.error("This is an error message.")
   ```

### Summary
- Ensure the YAML file is correctly placed and formatted.
- Call `setup_logging()` in your main script to initialize logging.
- Use the logger to log messages throughout your application.