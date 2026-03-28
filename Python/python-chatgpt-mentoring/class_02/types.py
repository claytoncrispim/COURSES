from __future__ import annotations
from typing import TypedDict, Literal, overload, Any, NotRequired,Union

Number = Union[int, float, str]

class BillPayload(TypedDict, total=False):
    type: str
    amount: Number
    currency: str
    paymentMethod: str
    status: str

class ErrorDetails(TypedDict):
    field: str
    reason: str

class ValidationError(TypedDict):
    code: str
    message: str
    details: ErrorDetails

class ValidatedPayload(TypedDict):
    # Clean output (guaranteed)
    type: str
    amount: float
    currency: str
    paymentMethod: str
    status: str


ValidateResult = tuple[Literal[True], ValidatedPayload] | tuple[Literal[False], ValidationError]

# Export as package-level Types
__all__: list[str] = ["ValidationError", "BillPayload", "ValidatedPayload", "ValidateResult"]