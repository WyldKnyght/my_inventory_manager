# src/utils/validation_manager.py

from typing import Dict, Any, List
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.config_manager import config_manager

class ValidationManager:
    def __init__(self):
        self.validation_rules = config_manager.get('validations', {})
        self.errors = []
        logger.info("Initialized ValidationManager")

    @ErrorManager.handle_errors()
    def validate(self, data: Dict[str, Any], rule_set: str) -> bool:
        """
        Validate data against a specific rule set.
        
        Args:
            data (Dict[str, Any]): The data to validate.
            rule_set (str): The name of the rule set to use for validation.

        Returns:
            bool: True if validation passes, False otherwise.
        """
        self.errors = []
        rules = self.validation_rules.get(rule_set, {})

        validations = [
            self._check_required_fields,
            self._validate_field_types,
            self._validate_field_values,
            self._validate_custom_rules
        ]

        is_valid = all(validation(data, rules) for validation in validations)

        if is_valid:
            logger.debug(f"Validation successful for rule set: {rule_set}")
        else:
            logger.warning(f"Validation failed for rule set: {rule_set}")
            for error in self.errors:
                logger.warning(f"Validation error: {error}")

        return is_valid

    def _check_required_fields(self, data: Dict[str, Any], rules: Dict[str, Any]) -> bool:
        """Check if all required fields are present and not empty."""
        required_fields = rules.get('required_fields', [])
        for field in required_fields:
            if field not in data or not data[field]:
                self.errors.append(f"Required field '{field}' is missing or empty")
                return False
        return True

    def _validate_field_types(self, data: Dict[str, Any], rules: Dict[str, Any]) -> bool:
        """Validate the types of fields in the data."""
        type_rules = rules.get('field_types', {})
        for field, expected_type in type_rules.items():
            if field in data and not isinstance(data[field], eval(expected_type)):
                self.errors.append(f"Field '{field}' has incorrect type. Expected {expected_type}")
                return False
        return True

    def _validate_field_values(self, data: Dict[str, Any], rules: Dict[str, Any]) -> bool:
        """Validate the values of fields in the data."""
        value_rules = rules.get('field_values', {})
        for field, rule in value_rules.items():
            if field in data:
                if 'min' in rule and data[field] < rule['min']:
                    self.errors.append(f"Field '{field}' is less than minimum value {rule['min']}")
                    return False
                if 'max' in rule and data[field] > rule['max']:
                    self.errors.append(f"Field '{field}' is greater than maximum value {rule['max']}")
                    return False
                if 'allowed_values' in rule and data[field] not in rule['allowed_values']:
                    self.errors.append(f"Field '{field}' has invalid value. Allowed values: {rule['allowed_values']}")
                    return False
        return True

    def _validate_custom_rules(self, data: Dict[str, Any], rules: Dict[str, Any]) -> bool:
        """Validate using custom rules defined for the rule set."""
        custom_rules = rules.get('custom_rules', {})
        for rule_name, rule_func in custom_rules.items():
            if not rule_func(data):
                self.errors.append(f"Custom rule '{rule_name}' failed")
                return False
        return True

    def get_errors(self) -> List[str]:
        """Get the list of validation errors."""
        return self.errors

# Create a global instance of ValidationManager
validation_manager = ValidationManager()

# Helper function to easily validate data
@ErrorManager.handle_errors()
def validate_data(data: Dict[str, Any], rule_set: str) -> bool:
    """
    Validate data using the ValidationManager.

    Args:
        data (Dict[str, Any]): The data to validate.
        rule_set (str): The name of the rule set to use for validation.

    Returns:
        bool: True if validation passes, False otherwise.
    """
    return validation_manager.validate(data, rule_set)