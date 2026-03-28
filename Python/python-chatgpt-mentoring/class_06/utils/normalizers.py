from __future__ import annotations
from typing import Any, Literal

from class_06.types import ValidationError

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
# * normalize_bill_type() uses normalize_required_str() to validate the presence of a bill type string, then checks if it's in the allowed set, returning either the normalized bill type or an error
# * is_missing_or_empty() is a utility function to check if a value is either None or an empty/whitespace string, which can be used for quick validation checks in the route handlers

Kind = Literal["missing", "empty", "invalid"]

def err(field: str, reason: str, kind: Kind) -> ValidationError:
    return {
        "code": "VALIDATION_ERROR",
        "message": "Invalid payload",
        "details": {
            "field": field,
            "reason": reason,
            "kind": kind, # "missing",  "empty", "invalid"
        },
    }


def normalize_required_str(raw: Any, field: str) -> tuple[bool, str | ValidationError]:
    if raw is None:
        return False, err(field, f"is required but missing.", "missing")
    
    s = str(raw).strip()
    if not s:
        return False, err(field, f"must not be empty.", "empty")
    return True, s

def normalize_bill_type(raw: Any, field: str, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, field)
    if not ok:
        # Turn empty into a more specific code
        return False, s_or_err
        
    bill_type = " ".join(str(s_or_err).split()).title()

    if bill_type not in allowed:
        return False, err(field, f"must be one of {', '.join(sorted(allowed))}.", "invalid")
    return True, bill_type

def normalize_amount(raw: Any, field: str) -> tuple[bool, float | ValidationError]:
    # Accepts int, float, or numeric strings - e.g. 1, 1.0, "1", "1.0"
    try:
        amount = float(raw)
    except (TypeError, ValueError):
        return False, err(field, f"must be a number.", "invalid")
    if amount <= 0:
        return False, err(field, f"must be greater than zero.", "invalid")
    return True, amount


def normalize_currency(raw: Any, field: str, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, field)
    if not ok:
        return False, s_or_err
    currency = str(s_or_err).upper()
    if currency not in allowed:
        return False, err(field, f"must be one of {', '.join(sorted(allowed))}.", "invalid")
    return True, currency

def normalize_status(raw: Any, field: str, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, field)
    if not ok:
        return False, s_or_err
    status = str(s_or_err).strip().title()
    if status not in allowed:
        return False, err(field, f"must be one of {', '.join(sorted(allowed))}.", "invalid")
    return True, status

def normalize_payment_method(raw: Any, field: str, allowed: set[str]) -> tuple[bool, str | ValidationError]:
    ok, s_or_err = normalize_required_str(raw, field)
    if not ok:
        # Turn empty into a more specific code
        return False, s_or_err
    
    # Robust normalization: trim, collpase spaces, Title Case - e.g. " credit   card " -> "Credit Card"
    method = " ".join(str(s_or_err).split()).title()

    if method not in allowed:
        return False, err(field, f"must be one of {', '.join(sorted(allowed))}.", "invalid")
    return True, method



# Deprecated utility - we can use normalize_required_str() directly in the route handlers instead, which gives us more control over the error details (e.g. field name, reason, kind)
# def is_missing_or_empty(raw: Any) -> bool:
#     return raw is None or (isinstance(raw, str) and not raw.strip())

# Export as package-level utils
__all__: list[str] = ["normalize_required_str", "normalize_amount", "normalize_currency", "normalize_status", "normalize_payment_method", "normalize_bill_type"]