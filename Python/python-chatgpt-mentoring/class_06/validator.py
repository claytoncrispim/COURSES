from __future__ import annotations
from class_06.types import BillPayload, ValidationResult
from class_06.data.constants import (
    ALLOWED_BILL_TYPES, 
    ALLOWED_CURRENCIES, 
    ALLOWED_PAYMENT_METHODS, 
    ALLOWED_STATUSES
)
from class_06.utils.normalizers import (
    normalize_bill_type, 
    normalize_amount, 
    normalize_currency, 
    normalize_payment_method, 
    normalize_status,
)

def validate_bill_payload(payload: BillPayload) -> ValidationResult:
    # BILL TYPE normalization and validation
    ok, bill_type_or_err = normalize_bill_type(payload.get("type"), field="type", allowed=ALLOWED_BILL_TYPES)
    if not ok:
        err = bill_type_or_err # ValidationError
        return {"ok": False, "error": err} 
    bill_type_or_err = bill_type_or_err # str
    
    # AMOUNT normalization and validation
    ok, amount_or_err = normalize_amount(payload.get("amount"), field="amount")
    if not ok:
        return {"ok": False, "error": amount_or_err}
    
    # CURRENCY normalization and validation
    ok, currency_or_err = normalize_currency(payload.get("currency"), field="currency", allowed=ALLOWED_CURRENCIES)
    if not ok:
        return {"ok": False, "error": currency_or_err}
    
    # PAYMENT METHOD normalization and validation
    ok, payment_or_err = normalize_payment_method(payload.get("paymentMethod"), field="paymentMethod", allowed=ALLOWED_PAYMENT_METHODS)    
    if not ok:
        return {"ok": False, "error": payment_or_err}
    
    # STATUS normalization and validation
    ok, status_or_err = normalize_status(payload.get("status"), field="status", allowed=ALLOWED_STATUSES)
    if not ok:
        return {"ok": False, "error": status_or_err}

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
