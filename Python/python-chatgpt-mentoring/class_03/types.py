from __future__ import annotations
from typing import TypedDict, Literal, Union

Number = Union[int, float, str]


# class BillPayload (TypedDict, input shape)
class BillPayload(TypedDict):
    type: str
    amount: Number
    currency: str
    paymentMethod: str
    status: str

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



ValidationResult = tuple[Literal[True], BillData] | tuple[Literal[False], ValidationError]

# Export as package-level Types
__all__: list[str] = ["ValidationError", "BillPayload", "BillData", "ValidationResult", "ErrorDetails"]