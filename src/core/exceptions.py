from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from utils.app_error import AppException

# 1. Handle our custom AppExceptions
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "errorCode": exc.error_code
        }
    )

# 2. Handle Pydantic Validation Errors (e.g. invalid email format)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Flatten the errors to a simple string or list
    errors = exc.errors()
    error_msg = f"{errors[0]['loc'][-1]}: {errors[0]['msg']}" if errors else "Validation error"

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "message": "Invalid request data",
            "errorCode": "VALIDATION_ERROR",
            "details": error_msg
        }
    )

# 3. Handle unexpected server errors
async def general_exception_handler(request: Request, exc: Exception):
    print(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Internal Server Error",
            "errorCode": "INTERNAL_SERVER_ERROR"
        }
    )