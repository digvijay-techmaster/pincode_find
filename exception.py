from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFoundError(Exception):
    def __init__(self,pincode:str):
        self.pincode=pincode

class InvalidPinCodeError(Exception):
    def __init__(self,pincode:str,reason:str="Invalid format"):
        self.pincode=pincode
        self.reason=reason

#these are custome exception class for each of these class we need to create a custome exception handeler

async def pincode_not_found_handeler(request:Request,exc:PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"pincode not found",
            "message":f"No location for pincode:{exc.pincode}",
            "pincode":exc.pincode
        }
    )
async def invalid_pincode_handeler(request:Request,exc:invalid_pincode_handeler):
    return JSONResponse(
        status_code=404,
        content={
            "error":"invalid pincode",
            "message":f"Pincode '{exc.pincode}' is invalid : {exc.reason}",
            "pincode":exc.pincode
        }
    )
#
