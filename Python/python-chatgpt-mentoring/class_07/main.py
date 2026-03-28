from class_07.validator import validate_bill_payload

# Main now is just a local runner
# We are removing server concerns and keeping only a "manual test runner"

if __name__ == "__main__":
    payload = {
        "type": "Energy",
        "amount": 150.75,
        "currency": "EUR",
        "paymentMethod": " credit card ",
        "status": "Paid",
        "extraField": "This should be ignored by the validator"
        }

    

print(validate_bill_payload(payload))
