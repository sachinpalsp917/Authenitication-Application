from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "Auth App"
    APP_ENV: str = "development"
    APP_ORIGIN: str
    
    # Auth
    JWT_SECRET: str
    JWT_REFRESH_SECRET: str
    
    # Database
    MONGO_URI: str
    
    # Email
    MAIL_CONSOLE_URL: str = "http://localhost:8025"
    MAIL_SERVER: str = "localhost"
    MAIL_PORT: int = 1025
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = "noreply@example.com"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_ignore_empty=True,
        extra="ignore" # Ignore extra fields in .env
    )

settings = Settings()