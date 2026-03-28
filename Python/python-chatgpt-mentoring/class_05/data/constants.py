from typing import Final
from class_05.types import ValidationError

# Set of valid currencies and statuses
ALLOWED_CURRENCIES =  {"USD", "EUR", "GBP", "BRL"}
ALLOWED_PAYMENT_METHODS = {"Cash", "Credit Card", "Debit Card", "Bank Transfer"}
ALLOWED_STATUSES = {"Paid", "Pending", "Unpaid"}
ALLOWED_BILL_TYPES = {"Energy", "Broadband", "Streaming", "Other"}

ERRORS: Final[dict[str, ValidationError]] = {     
    "err_type_empty": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "type", 
            "reason": "Bill type field must not be empty"
        }
    },
    "err_type_invalid": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "type", 
            "reason": f"Bill type must be one of: {', '.join(sorted(ALLOWED_BILL_TYPES))}"
        }
    },
    "err_amount": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "amount", 
            "reason": "Amount must be greater than 0"
        }
    },
    "err_currency": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "currency", 
            "reason": f"Currency must be one of: {', '.join(sorted(ALLOWED_CURRENCIES))}"
        }
    },
    "err_payment_method_empty": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": "Payment method must not be empty"
        }
    },
    "err_payment_method_invalid": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": f"Payment method must be one of: {', '.join(sorted(ALLOWED_PAYMENT_METHODS))}"
        }
    },
    "err_status": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "status", 
            "reason": f"Status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}"
        }
    }
}

# Export as package-level variable
__all__: list[str] = ["ERRORS", "ALLOWED_CURRENCIES", "ALLOWED_PAYMENT_METHODS", "ALLOWED_STATUSES", "ALLOWED_BILL_TYPES"]