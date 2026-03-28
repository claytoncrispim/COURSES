# List of valid currencies and statuses
CURRENCIES: list[str] = ["USD", "EUR", "GBP", "BRL"]
STATUSES: list[str] = ["Paid", "Pending", "Unpaid"]

CONFIG: dict[str, list[str] | dict[str, str | dict[str, str]]] = { 
    "currencies": CURRENCIES,
    "statuses": STATUSES,

    # Error messages
    "err_type": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "type", 
            "reason": "must not be empty"
        }
    },
    "err_amount": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "amount", 
            "reason": "must be > 0"
        }
    },
    "err_currency": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "currency", 
            "reason": f"must be one of: {', '.join(CURRENCIES)}"
        }
    },
    "err_payment_method": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "paymentMethod", 
            "reason": "must not be empty"
        }
    },
    "err_status": {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": "status", 
            "reason": f"must be one of: {', '.join(STATUSES)}"
        }
    }
}

# Export as package-level variable
__all__: list[str] = ["CONFIG"]