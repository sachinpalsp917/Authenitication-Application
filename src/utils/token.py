import jwt
from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from core.config import settings

ALGORITHM = 'HS256'

def create_token(
    payload: dict,
    secret: str,
    expires_delta: timedelta
) -> str:
    to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + expires_delta

    # Add standarized claims
    to_encode.update({"exp": expire, "iat": datetime.now(timezone.utc)})
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=ALGORITHM)
    return encoded_jwt

def create_access_token(user_id: str, session_id: str) -> str:
    return create_token(
        payload={"sub": user_id, "sessionId": session_id},
        secret=settings.JWT_SECRET,
        expires_delta=timedelta(minutes=15)
    )

def create_refresh_token(session_id: str) -> str:
    return create_token(
        payload={"sessionId": session_id},
        secret=settings.JWT_REFRESH_SECRET,
        expires_delta=timedelta(days=30)
    )

def decode_token(token: str, secret: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, secret, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None