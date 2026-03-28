from __future__ import annotations

from fastapi.testclient import TestClient

from class_07.api import app

client = TestClient(app)

def post_validate(payload: dict):
    return client.post("/validate", json=payload)

def test_valid_payload_returns_200_ok_true():    
    payload = {
        "type": "energy",
        "amount": 150.75,
        "currency": "eur",
        "paymentMethod": " credit card ",
        "status": "pending",
        "extraField": "ignored"
    }

    r = post_validate(payload)
    assert r.status_code == 200

    body = r.json()
    assert body["ok"] is True
    data = body["data"]

    assert data["type"] == "Energy"
    assert data["amount"] == 150.75
    assert data["currency"] == "EUR"
    assert data["paymentMethod"] == "Credit Card"
    assert data["status"] == "Pending"



def test_missing_payment_method_returns_422_kind_missing():
    payload = {
        "type": "energy",
        "amount": 150.75,
        "currency": "eur",
        "status": "pending"
    }

    r = post_validate(payload)
    assert r.status_code == 422

    body = r.json()
    assert body["ok"] is False
    err = body["error"]
    assert err["details"]["field"] == "paymentMethod"
    assert err["details"]["kind"] == "missing"



def test_empty_payment_method_returns_422_kind_empty():
    payload = {
        "type": "energy",
        "amount": 150.75,
        "currency": "eur",
        "paymentMethod": "   ",
        "status": "pending"
    }

    r = post_validate(payload)
    assert r.status_code == 422

    body = r.json()
    assert body["ok"] is False
    err = body["error"]
    assert err["details"]["field"] == "paymentMethod"
    assert err["details"]["kind"] == "empty"



def test_invalid_currency_returns_422_field_currency():
    payload = {
        "type": "energy",
        "amount": 150.75,
        "currency": "ZZZ",
        "paymentMethod": "credit card",
        "status": "pending"
    }

    r = post_validate(payload)
    assert r.status_code == 422

    body = r.json()
    assert body["ok"] is False
    err = body["error"]
    assert err["details"]["field"] == "currency"
    assert err["details"]["kind"] == "invalid"



def test_invalid_status_returns_422_field_status():
    payload = {
        "type": "energy",
        "amount": 150.75,
        "currency": "eur",
        "paymentMethod": "credit card",
        "status": "unknown"
    }

    r = post_validate(payload)
    assert r.status_code == 422

    body = r.json()
    assert body["ok"] is False
    err = body["error"]
    assert err["details"]["field"] == "status"
    assert err["details"]["kind"] == "invalid"


def test_extra_fields_are_ignored_and_still_200():
    payload = {
        "type": "energy",
        "amount": 10,
        "currency": "eur",
        "paymentMethod": "credit card",
        "status": "paid",
        "foo": {"bar": [1, 2, 3]}
    }

    r = post_validate(payload)
    assert r.status_code == 200
    assert r.json()["ok"] is True
