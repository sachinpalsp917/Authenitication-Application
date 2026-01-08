from fastapi import FastAPI
from core.config import settings
from contextlib import asynccontextmanager
from db import init_db

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