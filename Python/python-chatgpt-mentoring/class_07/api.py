from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from class_07.validator import validate_bill_payload

app = FastAPI(title="Bill Payload Validator - Class 07", version="1.0.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

# Accepts any JSON payload, then applies our validator contract
# - 200 if ok=True
# - 422 if ok=False, with the error details in the response body
@app.post("/validate")
def validate(payload: dict[str, Any]):
    result = validate_bill_payload(payload)

    if result["ok"]:
        return result
    
    return JSONResponse(status_code=422, content=result)
