from class_03_1.types import BillPayload, ValidationResult
from class_03_1.utils.to_float import to_float
from class_03_1.data.constants import ERRORS, ALLOWED_CURRENCIES, ALLOWED_PAYMENT_METHODS, ALLOWED_STATUSES
from class_03_1.data.test_payloads import valid_payload, invalid_currency_payload, invalid_payment_method_payload, empty_payment_method_payload, extra_field_payload


def validate_bill_payload(payload: BillPayload) -> ValidationResult:
      
    raw_type = payload.get("type", "")
    raw_amount = payload.get("amount", 0)
    raw_currency = payload.get("currency", "")
    raw_payment_method = payload.get("paymentMethod", "")
    raw_status = payload.get("status", "")    

    normalized_bill_type = raw_type.strip()
    floated_amount = to_float(raw_amount)
    normalized_currency = raw_currency.strip().upper()
    normalized_status = raw_status.strip().capitalize()
    normalized_payment_method = "".join(raw_payment_method.strip()).title()

    if not normalized_bill_type:
        return {"ok": False, "error": ERRORS["err_type"]}

    if floated_amount <= 0.0:
        return {"ok": False, "error": ERRORS["err_amount"]}

    if normalized_currency not in ALLOWED_CURRENCIES:
        return {"ok": False, "error": ERRORS["err_currency"]}

    if not normalized_payment_method:
        return {"ok": False, "error": ERRORS["err_payment_method_empty"]}

    if normalized_payment_method not in ALLOWED_PAYMENT_METHODS:
        return {"ok": False, "error": ERRORS["err_payment_method_invalid"]}

    if normalized_status not in ALLOWED_STATUSES:
        return {"ok": False, "error": ERRORS["err_status"]}
    
    return {
        "ok": True,
        "data": {
            "type": normalized_bill_type,
            "amount": floated_amount,
            "currency": normalized_currency,
            "paymentMethod": normalized_payment_method,
            "status": normalized_status
        }
    }



# Test payloads
# Validating the payload and printing the result
print("Valid Payload: ", validate_bill_payload(valid_payload))
print("Invalid Currency Payload: ", validate_bill_payload(invalid_currency_payload)) 
print("Empty Payment Method Payload: ", validate_bill_payload(empty_payment_method_payload))

# Just testing the new rule for payment method validation
# print("Invalid Payment Method Payload: ", validate_bill_payload(invalid_payment_method_payload))

# Extra field payload should be ignored and validated successfully
# print("Extra Field Payload: ", validate_bill_payload(extra_field_payload))