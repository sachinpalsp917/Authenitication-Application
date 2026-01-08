from datetime import datetime
from enum import Enum
from beanie import Document, PydanticObjectId
from pydantic import Field

class VerificationType(Enum):
    EMAIL_VERIFICATION = "email_verification"
    PASSWORD_RESET = "password_reset"

class VerificationCode(Document):
    user_id: PydanticObjectId
    type: VerificationType
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime

    class Settings:
        name = "verification_codes"
