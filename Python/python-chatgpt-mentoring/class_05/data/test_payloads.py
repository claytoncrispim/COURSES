from typing import Any
from class_05.types import BillPayload


# 1. Valid payload
valid_payload: BillPayload = {
    "type": "   energy     ", # Testing string input with extra spaces
    "amount": 25,
    "currency": "brl", 
    "paymentMethod": " credit card ",
    "status": "pending"
}

# 2. Invalid currency
invalid_currency_payload: BillPayload = {
    "type": " broadband ",
    "amount": 25,
    "currency": "abc", # Invalid currency
    "paymentMethod": " debit card ",
    "status": "pending"
}

# 3. Invalid status
invalid_status_payload: BillPayload = {
    "type": " streaming ",
    "amount": 25,
    "currency": "eur",
    "paymentMethod": " debit card ",
    "status": "unknown" # Invalid status
}

# 4. Empty payment method
empty_payment_method_payload: BillPayload = {
    "type": " other ",
    "amount": 25,
    "currency": "usd",
    "paymentMethod": "   ", # Empty after stripping
    "status": "pending"
}

# 5. Invalid payment method
invalid_payment_method_payload: BillPayload = {
    "type": " energy ",
    "amount": 25,
    "currency": "eur",
    "paymentMethod": " bitcoin ", # Invalid payment method
    "status": "pending"
}

# 6. Extra field should be ignored
extra_field_payload: dict[str, Any] = {
    "type": " broadband ",
    "amount": 25,
    "currency": "usd",
    "paymentMethod": " credit card ",
    "status": "pending",
    "extraField": "This should be ignored"
}

# 7. Empty type field
empty_type_payload: BillPayload = {
    "type": "   ", # Empty after stripping
    "amount": 25,
    "currency": "usd",
    "paymentMethod": " credit card ",
    "status": "pending"
}

# 8. Invalid type field
invalid_type_payload: BillPayload = {
    "type": " subscription ", # Invalid type
    "amount": 25,
    "currency": "usd",
    "paymentMethod": " credit card ",
    "status": "pending"
}


__all__: list[str] = ["valid_payload", "invalid_currency_payload", "invalid_status_payload", "empty_payment_method_payload", "invalid_payment_method_payload", "extra_field_payload", "empty_type_payload", "invalid_type_payload"]