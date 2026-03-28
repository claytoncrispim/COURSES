from typing import Any
from class_03.types import BillPayload


# 1. Valid payload
valid_payload: BillPayload = {
    "type": "   invoice     ", # Testing string input with extra spaces
    "amount": 25,
    "currency": "brl", 
    "paymentMethod": "cash",
    "status": "pending"
}

# 2. Invalid currency
invalid_currency_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "abc", # Invalid currency
    "paymentMethod": "cash",
    "status": "pending"
}

# 3. Invalid status
invalid_status_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "eur",
    "paymentMethod": "debit card",
    "status": "unknown" # Invalid status
}

# 4. Empty payment method
empty_payment_method_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "usd",
    "paymentMethod": "   ", # Empty after stripping
    "status": "pending"
}

# 5. Invalid payment method
invalid_payment_method_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "eur",
    "paymentMethod": "Bitcoin", # Invalid payment method
    "status": "pending"
}

# 6. Extra field should be ignored
extra_field_payload: dict[str, Any] = {
    "type": "invoice",
    "amount": 25,
    "currency": "usd",
    "paymentMethod": "cash",
    "status": "pending",
    "extraField": "This should be ignored"
}

__all__: list[str] = ["valid_payload", "invalid_currency_payload", "invalid_status_payload", "empty_payment_method_payload", "invalid_payment_method_payload", "extra_field_payload"]