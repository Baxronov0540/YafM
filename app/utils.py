from datetime import datetime,timezone,timedelta
from fastapi import HTTPException
from passlib.context import CryptContext
from jose import jwt
from jose.exceptions import JWTError
from contextvars import ContextVar

current_lang = ContextVar("current_lang", default="uz")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from app.config import settings

def password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def generate_jwt_tokens(user_id: int, is_access_only: bool = False):
    access_token = jwt.encode(
        algorithm=settings.ALGORITHM,
        key=settings.SECRET_KEY,
        claims={
            "user_id": str(user_id),
            "exp": datetime.now(timezone.utc)
            + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        },
    )

    if is_access_only:
        return access_token
    refresh_token = jwt.encode(
        algorithm=settings.ALGORITHM,
        key=settings.SECRET_KEY,
        claims={
            "user_id": str(user_id),
            "exp": datetime.now(timezone.utc)
            + timedelta(settings.REFRESH_TOKEN_EXPIRE_DAYS),
        },
    )
    return access_token, refresh_token


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        print(payload)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def looks_hashed(p: str):
    return p.startswith("$argon2")
