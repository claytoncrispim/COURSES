from typing import Any, Union
from class_02.types import BillPayload, ValidationError, ValidatedPayload, ValidateResult
from class_02.utils.strip_str import strip_str
from class_02.utils.to_float import to_float
from class_02.utils.normalize_currency import normalize_currency
from class_02.utils.normalize_status import normalize_status
from class_02.data.constants import ERRORS, ALLOWED_CURRENCIES, ALLOWED_STATUSES
from class_02.data.test_payloads import valid_payload, invalid_currency_payload, invalid_status_payload, empty_payment_method_payload, extra_field_payload

# ValidationResult = tuple[bool, Union[ValidatedPayload, ValidationError]]

def validate_bill_payload(payload: BillPayload) -> ValidateResult:
      
    raw_type = payload.get("type", "")
    raw_amount = payload.get("amount", 0)
    raw_currency = payload.get("currency", "")
    raw_payment_method = payload.get("paymentMethod", "")
    raw_status = payload.get("status", "")    

    stripped_bill_type = strip_str(str(raw_type))
    floated_amount = to_float(raw_amount)
    normalized_currency = normalize_currency(str(raw_currency))
    normalized_status = normalize_status(str(raw_status))
    stripped_payment_method = strip_str(str(raw_payment_method))

    if not stripped_bill_type:
        return False, ERRORS["err_type"]

    if floated_amount <= 0.0:
        return False, ERRORS["err_amount"]

    if normalized_currency not in ALLOWED_CURRENCIES:
        return False, ERRORS["err_currency"]

    if not stripped_payment_method:
        return False, ERRORS["err_payment_method"]

    if normalized_status not in ALLOWED_STATUSES:
        return False, ERRORS["err_status"]
    
    return True, {
        "type": stripped_bill_type,
        "amount": floated_amount,
        "currency": normalized_currency,
        "paymentMethod": stripped_payment_method,
        "status": normalized_status
    }



# Test payloads
# Validating the payload and printing the result
print("Valid Payload: ", validate_bill_payload(valid_payload)) # (True, {'type': 'invoice', 'amount': 25.0, 'currency': 'USD', 'paymentMethod': 'Cash', 'status': 'Pending'})
print("Invalid Currency Payload: ", validate_bill_payload(invalid_currency_payload)) # (False, {'code': 'CURRENCY_ERROR', 'message': 'Invalid payload', 'details': {'field': 'currency', 'reason': 'must be one of: USD, EUR, GBP, BRL'}})
print("Invalid Status Payload: ", validate_bill_payload(invalid_status_payload)) # (False, {'code': 'STATUS_ERROR', 'message': 'Invalid payload', 'details': {'field': 'status', 'reason': 'must be one of: Paid, Pending, Unpaid'}})
print("Empty Payment Method Payload: ", validate_bill_payload(empty_payment_method_payload)) # (False, {'code': 'PAYMENT_METHOD_ERROR', 'message': 'Invalid payload', 'details': {'field': 'paymentMethod', 'reason': 'must not be empty'}})
print("Extra Field Payload: ", validate_bill_payload(extra_field_payload)) # (True, {'type': 'invoice', 'amount': 25.0, 'currency': 'USD', 'paymentMethod': 'Cash', 'status': 'Pending'}) - Extra field is ignored, validation still passes