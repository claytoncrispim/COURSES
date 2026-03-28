from class_02.types import BillPayload


# 1. Valid payload
valid_payload: BillPayload = {
    "type": "   invoice     ", # Testing string input with extra spaces
    "amount": 25,
    "currency": "brl", 
    "paymentMethod": "Cash",
    "status": "pending"
}

# 2. Invalid currency
invalid_currency_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "abc", # Invalid currency
    "paymentMethod": "Cash",
    "status": "pending"
}

# 3. Invalid status
invalid_status_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "USD",
    "paymentMethod": "Cash",
    "status": "unknown" # Invalid status
}

# 4. Empty payment method
empty_payment_method_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "USD",
    "paymentMethod": "   ", # Empty after stripping
    "status": "pending"
}

# 5. Extra field should be ignored
extra_field_payload: BillPayload = {
    "type": "invoice",
    "amount": 25,
    "currency": "USD",
    "paymentMethod": "Cash",
    "status": "pending",
    "extraField": "This should be ignored"
}

__all__: list[str] = ["valid_payload", "invalid_currency_payload", "invalid_status_payload", "empty_payment_method_payload", "extra_field_payload"]