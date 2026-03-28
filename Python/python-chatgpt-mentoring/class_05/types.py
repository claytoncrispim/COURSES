from __future__ import annotations
from typing import NotRequired, TypedDict, Literal, Union

Number = Union[int, float, str]

# class BillPayload (TypedDict, input shape)
class BillPayload(TypedDict, total=False):
    type: NotRequired[object]
    amount: NotRequired[object]
    currency: NotRequired[object]
    paymentMethod: NotRequired[object]
    status: NotRequired[object]

# BillData (TypedDict, normalized/validated output shape)
class BillData(TypedDict):
    type: str
    amount: float
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

class OkResult(TypedDict):
    ok: Literal[True]
    data: BillData

class ErrResult(TypedDict):
    ok: Literal[False]
    error: ValidationError

ValidationResult = OkResult | ErrResult


# Export as package-level Types
__all__: list[str] = ["ValidationError", "BillPayload", "BillData", "ValidationResult", "ErrorDetails"]