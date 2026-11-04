from fastapi import FastAPI
from exception import(
     PinCodeNotFoundError,
     pincode_not_found_handeler,
     InvalidPinCodeError,
     invalid_pincode_handeler
)

import uvicorn
app=FastAPI(
    title="Pincode lookup API",
    description="Auto fill city and state from Indian pincode durong checkout"
)

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001,reload=True)