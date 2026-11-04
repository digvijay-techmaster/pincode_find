from fastapi import FastAPI
from exception import(
     PinCodeNotFoundError,
     pincode_not_found_handeler,
     InvalidPinCodeError,
     invalid_pincode_handeler
)
from models import LocationResponse, BulkResponse, BulkRequest
from data import pincode_db
import uvicorn
app=FastAPI(
    title="Pincode lookup API",
    description="Auto fill city and state from Indian pincode durong checkout"
)

#register your custom exception handeler 
app.add_exception_handler(PinCodeNotFoundError,pincode_not_found_handeler)
app.add_exception_handler(InvalidPinCodeError,invalid_pincode_handeler)
@app.get("/")
def root():
    return {"message":"Pincode lookup api"}

@app.get("/pincode/{code}",response_model=LocationResponse)
def lookup_pincode(code:str):
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(code,"Must be exactly 6 digit")

    if code not in pincode_db:
        raise PinCodeNotFoundError(code)
    return pincode_db[code]

@app.post("/pincode/bulk",response_model=BulkResponse)
def bulk_lookup(request : BulkRequest):
    results = []
    missing = []

    for code in request.pincode:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)
    return BulkResponse(
        found =len(results),
        not_found=len(missing),
        results=results,
        missing=missing
    )
if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001,reload=True)