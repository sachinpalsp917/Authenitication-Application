from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from core.config import settings
from models.user import User
from models.session import Session
from models.verification_code import VerificationCode

async def init_db():
    client = AsyncIOMotorClient(settings.MONGO_URI)

    await init_beanie(
        database=client.get_default_database(),
        document_models=[
            User,
            Session,
            VerificationCode,
        ]
    )