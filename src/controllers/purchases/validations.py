# src/controllers/purchases/validations.py

from typing import Dict, Any
from utils.custom_logging import logger
from utils.error_manager import ErrorManager
from configs.config_manager import config_manager

class PurchaseValidations:
    def __init__(self):
        self.validation_rules = config_manager.get('validations.purchases', {})
        logger.info("Initialized PurchaseValidations")

    @ErrorManager.handle_errors()
    def validate_purchase_data(self, purchase_data: Dict[str, Any]) -> bool:
        """Validate purchase data before adding or updating."""
        required_fields = self.validation_rules.get('required_fields', [
            'vendor_id', 'purchase_order_number', 'purchase_date', 'purchase_amount'
        ])
        
        is_valid = self._check_required_fields(purchase_data, required_fields)
        is_valid = is_valid and self._validate_field_types(purchase_data)
        is_valid = is_valid and self._validate_field_values(purchase_data)
        
        if is_valid:
            logger.debug("Purchase data validation successful")
        else:
            logger.warning("Purchase data validation failed")
        return is_valid

    def _check_required_fields(self, data: Dict[str, Any], required_fields: list) -> bool:
        """Check if all required fields are present and not empty."""
        for field in required_fields:
            if field not in data or not data[field]:
                logger.warning(f"Required field '{field}' is missing or empty")
                return False
        return True

    def _validate_field_types(self, data: Dict[str, Any]) -> bool:
        """Validate the types of fields in the purchase data."""
        type_rules = self.validation_rules.get('field_types', {})
        for field, expected_type in type_rules.items():
            if field in data and not isinstance(data[field], eval(expected_type)):
                logger.warning(f"Field '{field}' has incorrect type. Expected {expected_type}")
                return False
        return True

    def _validate_field_values(self, data: Dict[str, Any]) -> bool:
        """Validate the values of fields in the purchase data."""
        value_rules = self.validation_rules.get('field_values', {})
        for field, rule in value_rules.items():
            if field in data:
                if 'min' in rule and data[field] < rule['min']:
                    logger.warning(f"Field '{field}' is less than minimum value {rule['min']}")
                    return False
                if 'max' in rule and data[field] > rule['max']:
                    logger.warning(f"Field '{field}' is greater than maximum value {rule['max']}")
                    return False
                if 'allowed_values' in rule and data[field] not in rule['allowed_values']:
                    logger.warning(f"Field '{field}' has invalid value. Allowed values: {rule['allowed_values']}")
                    return False
        return True

@ErrorManager.handle_errors()
def validate_purchase_data(purchase_data: Dict[str, Any]) -> bool:
    """Validate purchase data before adding or updating."""
    validator = PurchaseValidations()
    return validator.validate_purchase_data(purchase_data)