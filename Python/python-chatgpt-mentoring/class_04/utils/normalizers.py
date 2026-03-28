from __future__ import annotations
from typing import Any

from class_04.types import ValidationError

# Helper functions for normalization and error handling
# * def err() creates a standardized ValidationError object
# * normalize_required_str() checks if a value is present and non-empty, returning either the normalized string or an error
# * normalize_amount() attempts to convert a value to a float and checks if it's greater than zero, returning either the
#   float or an error
# * normalize_currency() uses normalize_required_str() to validate the presence of a currency string, then checks if it's in 
#   the allowed set, returning either the normalized currency or an error
# * normalize_status() uses normalize_required_str() to validate the presence of a status string, then checks if it's in the 
#   allowed set, returning either the normalized status or an error
# * normalize_payment_method() uses normalize_required_str() to validate the presence of a payment method string, then 
#   checks if it's in the allowed set, returning either the normalized payment method or an error

def err(field: str, reason: str) -> ValidationError:
    return {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": field,
            "reason": reason
        }
    }


def normalize_required_str(raw: Any, field: str) -> tuple[bool, str | ValidationError]:
    if raw is None:
        return False, err(field, "is required but missing.")
    s = str(raw).strip()
    if not s:
        return False, err(field, "must not be empty.")
    return True, s


def normalize_amount(raw: Any) -> tuple[bool, float | ValidationError]:
    # Accepts int, float, or numeric strings - e.g. 1, 1.0, "1", "1.0"
    try:
        amount = float(raw)
    except (TypeError, ValueError):
        return False, err("amount", "must be a number.")
    if amount <= 0:
        return False, err("amount", "must be greater than zero.")
    return True, amount


def normalize_currency(raw: Any, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, "currency")
    if not ok:
        return False, s_or_err # type: ignore[return-value]
    currency = str(s_or_err).upper()
    if currency not in allowed:
        return False, err("currency", f"must be one of {', '.join(sorted(allowed))}.")
    return True, currency

def normalize_status(raw: Any, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, "status")
    if not ok:
        return False, s_or_err # type: ignore[return-value]
    status = str(s_or_err).strip().title()
    if status not in allowed:
        return False, err("status", f"must be one of {', '.join(sorted(allowed))}.")
    return True, status

def normalize_payment_method(raw: Any, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, "paymentMethod")
    if not ok:
        return False, s_or_err # type: ignore[return-value]
    
    # Robust normalization: trim, collpase spaces, Title Case - e.g. " credit   card " -> "Credit Card"
    method = " ".join(str(s_or_err).split()).title()

    # Debugging: print the normalized payment method and the allowed set to understand why a valid input might be failing
    # print("DEBUG normalized paymentMethod:", repr(method))
    # print("DEBUG allowed:", sorted(allowed))

    if method not in allowed:
        return False, err("paymentMethod", f"must be one of {', '.join(sorted(allowed))}.")
    return True, method

def normalize_bill_type(raw: Any, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, "type")
    if not ok:
        return False, s_or_err # type: ignore[return-value]
    # Robust normalization: trim, collpase spaces, Title Case - e.g. "  energy " -> "Energy"
    bill_type = " ".join(str(s_or_err).split()).title()

    if bill_type not in allowed:
        return False, err("type", f"must be one of {', '.join(sorted(allowed))}.")
    return True, bill_type

def is_missing_or_empty(raw: Any) -> bool:
    return raw is None or (isinstance(raw, str) and not raw.strip())

# Export as package-level utils
__all__: list[str] = ["normalize_required_str", "normalize_amount", "normalize_currency", "normalize_status", "normalize_payment_method", "normalize_bill_type", "is_missing_or_empty"]