from typing import Any
from class_04.types import BillPayload, ValidationResult
from class_04.data.constants import ERRORS, ALLOWED_CURRENCIES, ALLOWED_PAYMENT_METHODS, ALLOWED_STATUSES, ALLOWED_BILL_TYPES
from class_04.utils.normalizers import normalize_amount, normalize_currency, normalize_status, normalize_payment_method, normalize_bill_type, is_missing_or_empty
# Payload test data
from class_04.data.test_payloads import empty_type_payload, valid_payload, invalid_currency_payload, invalid_status_payload, empty_payment_method_payload, invalid_payment_method_payload, extra_field_payload, invalid_type_payload


def validate_bill_payload(payload: BillPayload) -> ValidationResult:

    # # Debugging
    # print("DEBUG type raw: ", payload.get("type"))
    # print("DEBUG allowed bill types: ", ALLOWED_BILL_TYPES)

    # BILL TYPE normalization and validation
    ok, bill_type_or_err = normalize_bill_type(payload.get("type"), ALLOWED_BILL_TYPES)
    # If payment method normalization fails, we need to determine if it's due to being empty or invalid
    # 1. Check if bill type is empty (after stripping) - this would be an "empty bill type" error
    # 2. If it's not empty, then it must be an "invalid bill type" error
    if not ok:
        raw_type = payload.get("type")
        if is_missing_or_empty(raw_type):
            return {"ok": False, "error": ERRORS["err_type_empty"]}
        
        return {"ok": False, "error": ERRORS["err_type_invalid"]}    
    
    # AMOUNT normalization and validation
    ok, amount_or_err = normalize_amount(payload.get("amount"))
    if not ok:
        return {"ok": False, "error": ERRORS["err_amount"]}
    
    # CURRENCY normalization and validation
    ok, currency_or_err = normalize_currency(payload.get("currency"), ALLOWED_CURRENCIES)
    if not ok:
        return {"ok": False, "error": ERRORS["err_currency"]}
    
    # PAYMENT METHOD normalization and validation
    ok, payment_or_err = normalize_payment_method(payload.get("paymentMethod"), ALLOWED_PAYMENT_METHODS)
    # If payment method normalization fails, we need to determine if it's due to being empty or invalid
    # 1. Check if payment method is empty (after stripping) - this would be an "empty payment method" error
    # 2. If it's not empty, then it must be an "invalid payment method" error
    if not ok:
        raw_payment = payload.get("paymentMethod")
        if is_missing_or_empty(raw_payment):
            return {"ok": False, "error": ERRORS["err_payment_method_empty"]}
        
        return {"ok": False, "error": ERRORS["err_payment_method_invalid"]}


    # STATUS normalization and validation
    ok, status_or_err = normalize_status(payload.get("status"), ALLOWED_STATUSES)
    if not ok:
        return {"ok": False, "error": ERRORS["err_status"]}

    return {
        "ok": True,
        "data": {
            "type": bill_type_or_err, # type: ignore[typeddict-item]
            "amount": amount_or_err, # type: ignore[typeddict-item]
            "currency": currency_or_err, # type: ignore[typeddict-item]
            "paymentMethod": payment_or_err, # type: ignore[typeddict-item]
            "status": status_or_err # type: ignore[typeddict-item]
        },
    }




# Test payloads
# Validating the payload and printing the result

if __name__ == "__main__":
    print("Valid Payload: ", validate_bill_payload(valid_payload))
    print("Invalid Currency Payload: ", validate_bill_payload(invalid_currency_payload)) 
    print("Empty Payment Method Payload: ", validate_bill_payload(empty_payment_method_payload))
    print("Invalid Payment Method Payload: ", validate_bill_payload(invalid_payment_method_payload))
    print("Invalid Status Payload: ", validate_bill_payload(invalid_status_payload))
    print("Empty Type Payload: ", validate_bill_payload(empty_type_payload))
    print("Invalid Type Payload: ", validate_bill_payload(invalid_type_payload))
    

