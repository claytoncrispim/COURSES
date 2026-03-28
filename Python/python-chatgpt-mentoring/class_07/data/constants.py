from typing import Final
from class_07.types import ValidationError

# Set of valid currencies and statuses
ALLOWED_BILL_TYPES = {"Energy", "Broadband", "Streaming", "Other"}
ALLOWED_CURRENCIES =  {"USD", "EUR", "GBP", "BRL"}
ALLOWED_PAYMENT_METHODS = {"Cash", "Credit Card", "Debit Card", "Bank Transfer"}
ALLOWED_STATUSES = {"Paid", "Pending", "Unpaid"}

# Export as package-level variable
__all__: list[str] = ["ALLOWED_CURRENCIES", "ALLOWED_PAYMENT_METHODS", "ALLOWED_STATUSES", "ALLOWED_BILL_TYPES"]