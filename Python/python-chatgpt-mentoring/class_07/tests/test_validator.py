from __future__ import annotations

import pytest

from class_07.main import validate_bill_payload

def test_valid_payload_returns_ok_true():
    payload = {
        "type": "energy",
        "amount": 25.00,
        "currency": "brl",
        "paymentMethod": "credit card",
        "status": "pending",
    }

    result = validate_bill_payload(payload)
    
    # Assert that the validation result indicates success
    # and that the data contains the expected type
    # * The assert statement checks if the "ok" key in the result is True, indicating that the validation was successful.
    assert result["ok"] is True
    data = result["data"]
    assert data["type"] == "Energy"
    assert data["amount"] == 25.00
    assert data["currency"] == "BRL"
    assert data["paymentMethod"] == "Credit Card"
    assert data["status"] == "Pending"


@pytest.mark.parametrize(
    "payload, expected_field",
    [
        (
            {
                "type": "energy",
                "amount": 25.00,
                "currency": "zzz",  # Invalid currency
                "paymentMethod": "credit card",
                "status": "pending",
            },
            "currency", # The expected field that should be reported as invalid due to the unrecognized currency code
        ),
        (
            {
                "type": "energy",
                "amount": "-1", # Invalid amount (negative value)
                "currency": "eur",
                "paymentMethod": "credit card",
                "status": "pending",
            },
             "amount",
        ),
        (
            {
                "type": "energy",
                "amount": 10,
                "currency": "eur",
                "paymentMethod": "bitcoin", # Invalid payment method
                "status": "pending",
            },
             "paymentMethod",
        ),
        (
            {
                "type": "energy",
                "amount": 10,
                "currency": "brl",
                "paymentMethod": "credit card",
                "status": "unknown", # Invalid status
            },
            "status",
        ),
        (
            {
                "type": "", # Missing type
                "amount": 10,
                "currency": "eur",
                "paymentMethod": "credit card",
                "status": "pending",
            },
            "type",
        ),
        (
            {
                "type": "hogwarts", # Invalid type
                "amount": 10,
                "currency": "eur",
                "paymentMethod": "credit card",
                "status": "pending",
            },
             "type",
        ),
    ],
)    
def test_invalid_payloads_return_ok_false(payload, expected_field):
        result = validate_bill_payload(payload)
        
        # Assert that the validation result indicates failure
        assert result["ok"] is False
        
        # Assert that the error details contain the expected field that caused the validation to fail
        err = result["error"]
        assert err["code"] == "VALIDATION_ERROR"
        assert err["details"]["field"] == expected_field

def test_extra_fields_are_ignored():
        payload = {
            "type": "energy",
            "amount": 10,
            "currency": "eur",
            "paymentMethod": "credit card",
            "status": "pending",
            "extra": "ignored",
        }

        result = validate_bill_payload(payload)
        
        # Assert that the validation result indicates success
        assert result["ok"] is True

def test_amount_non_numeric_fails():
        payload = {
            "type": "energy",
            "amount": "abc", # Non-numeric amount
            "currency": "eur",
            "paymentMethod": "credit card",
            "status": "pending",
        }

        result = validate_bill_payload(payload)
        
        # Assert that the validation result indicates failure due to the non-numeric amount
        assert result["ok"] is False        
        assert result["error"]["details"]["field"] == "amount"

def test_currency_trims_and_normalizes():
        payload = {
            "type": "energy",
            "amount": "10",
            "currency": "EUR", 
            "paymentMethod": "credit card",
            "status": "pending",
        }

        result = validate_bill_payload(payload)
        
        # Assert that the validation result indicates success and that the currency is normalized to uppercase without whitespace
        assert result["ok"] is True
        assert result["data"]["currency"] == "EUR"