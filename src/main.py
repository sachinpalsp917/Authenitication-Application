from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from core.config import settings
from db import init_db
from utils.app_error import AppException
from core.exceptions import (
    app_exception_handler,
    validation_exception_handler,
    general_exception_handler
)
from services.email import EmailService

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connecting to DB...")
    await init_db()
    print("Database Connected")
    yield

app = FastAPI(
    title=settings.APP_NAME,
    description="A robust authentication API with FastAPI",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.APP_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

@app.get("/health", tags=["health"])
def healthCheck():
    return {"message": "server running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )