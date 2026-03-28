from typing import Final
from class_03.types import ValidationError

# Set of valid currencies and statuses
ALLOWED_CURRENCIES =  {"USD", "EUR", "GBP", "BRL"}
ALLOWED_PAYMENT_METHODS = {"Cash", "Credit Card", "Debit Card", "Bank Transfer"}
ALLOWED_STATUSES = {"Paid", "Pending", "Unpaid"}

ERRORS: Final[dict[str, ValidationError]] = {     
    "err_type": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "type", 
            "reason": "This field must not be empty"
        }
    },
    "err_amount": {
        "code": "AMOUNT_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "amount", 
            "reason": "Amount must be greater than 0"
        }
    },
    "err_currency": {
        "code": "CURRENCY_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "currency", 
            "reason": f"Currency must be one of: {', '.join(sorted(ALLOWED_CURRENCIES))}"
        }
    },
    "err_payment_method_empty": {
        "code": "PAYMENT_METHOD_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": "Payment method must not be empty"
        }
    },
    "err_payment_method_invalid": {
        "code": "PAYMENT_METHOD_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": f"Payment method must be one of: {', '.join(sorted(ALLOWED_PAYMENT_METHODS))}"
        }
    },
    "err_status": {
        "code": "STATUS_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "status", 
            "reason": f"Status must be one of: {', '.join(sorted(ALLOWED_STATUSES))}"
        }
    }
}

# Export as package-level variable
__all__: list[str] = ["ERRORS", "ALLOWED_CURRENCIES", "ALLOWED_PAYMENT_METHODS", "ALLOWED_STATUSES"]