from typing import Final
from class_06.types import ValidationError

# Set of valid currencies and statuses
ALLOWED_CURRENCIES =  {"USD", "EUR", "GBP", "BRL"}
ALLOWED_PAYMENT_METHODS = {"Cash", "Credit Card", "Debit Card", "Bank Transfer"}
ALLOWED_STATUSES = {"Paid", "Pending", "Unpaid"}
ALLOWED_BILL_TYPES = {"Energy", "Broadband", "Streaming", "Other"}

ERRORS: Final[dict[str, ValidationError]] = { 
    "err_type_invalid": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "type", 
            "reason": f"Bill type must be one of: {', '.join(sorted(ALLOWED_BILL_TYPES))}",
            "kind": "invalid"
        }
    },

    "err_type_empty": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "type", 
            "reason": "Bill type field must not be empty",
            "kind": "empty"
        }
    },

    "err_amount": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "amount", 
            "reason": "Amount must be greater than 0",
            "kind": "invalid"
        }
    },

    "err_currency": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "currency", 
            "reason": f"Currency must be one of: {', '.join(sorted(ALLOWED_CURRENCIES))}",
            "kind": "invalid"
        }
    },

    "err_payment_method": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": f"Payment method must be one of: {', '.join(sorted(ALLOWED_PAYMENT_METHODS))}",
            "kind": "invalid"
        }
    },

    "err_payment_method_empty": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": "Payment method must not be empty",
            "kind": "empty"
        }
    },    

    "err_status": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "status", 
            "reason": f"Status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}",
            "kind": "invalid"
        }
    }
}

# Export as package-level variable
__all__: list[str] = ["ERRORS", "ALLOWED_CURRENCIES", "ALLOWED_PAYMENT_METHODS", "ALLOWED_STATUSES", "ALLOWED_BILL_TYPES"]