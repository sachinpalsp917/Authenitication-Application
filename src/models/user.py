from datetime import datetime
from typing import Optional
from beanie import Document, Indexed
from pydantic import Field, EmailStr

class User(Document):
    email: Indexed(EmailStr, unique=True) # type: ignore
    password: str
    verified: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"