from datetime import datetime, timedelta
from typing import Optional
from beanie import Document, PydanticObjectId
from pydantic import Field

class Session(Document):
    user_id: PydanticObjectId
    user_agent: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime = Field(default_factory=lambda: datetime.utcnow() + timedelta(days=30))

    class Settings:
        name = "sessions"