from class_01.utils.strip_str import strip_str
from class_01.utils.to_float import to_float
from class_01.utils.upper_str import upper_str
from class_01.data.config_data import CONFIG


def validate_bill_payload(payload: dict) -> tuple[bool, dict]:

    
    raw_type = payload.get("type", "")
    raw_amount = payload.get("amount", 0)
    raw_currency = payload.get("currency", "")
    raw_payment_method = payload.get("paymentMethod", "")
    raw_status = payload.get("status", "")    

    stripped_type: str = strip_str(str(raw_type))
    floatAmount: float = to_float(raw_amount)
    upperCurrency: str = upper_str(str(raw_currency))
    normalized_status: str = strip_str(str(raw_status)).capitalize()  # Normalize status to match the format in the list
    payment_method: str = strip_str(str(raw_payment_method))

    if not stripped_type:
        return False, CONFIG["err_type"]

    if not floatAmount or floatAmount <= 0:
        return False, CONFIG["err_amount"]

    if upperCurrency not in CONFIG["currencies"]:
        return False, CONFIG["err_currency"]

    if not payment_method:
        return False, CONFIG["err_payment_method"]

    if normalized_status not in CONFIG["statuses"]:
        return False, CONFIG["err_status"]
    
    return True, {
        "type": stripped_type,
        "amount": floatAmount,
        "currency": upperCurrency,
        "paymentMethod": payment_method,
        "status": normalized_status
    }



# Example usage
payload: dict[str, str | float] = {
    "type": "   invoice     ", # Testing string input with extra spaces
    "amount": 150.75,
    "currency": "BRL",
    "paymentMethod": "Cash",
    "status": "Paid"
}

# Validating the payload and printing the result
print(validate_bill_payload(payload))