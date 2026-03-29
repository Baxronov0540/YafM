from datetime import UTC, datetime

from fastapi import Request, Response
from sqlalchemy import select
from jose import JWTError
from starlette_admin.auth import AuthProvider
from starlette_admin.exceptions import LoginFailed

from app.database import async_session_maker
from app.models import User
from app.utils import verify_password, generate_jwt_tokens, decode_jwt_token

from app.config import settings


class JSONAuthProvider(AuthProvider):
    async def login(self, username, password, remember_me, request, response: Response):
        async with async_session_maker() as db:
            stmt = select(User).where(User.username == username.strip())
            user = (await db.execute(stmt)).scalars().first()

            if not user or not user.is_active:
                raise LoginFailed("User not found or inactive")

            if not user.is_admin:
                raise LoginFailed("User is not admin")

            if not verify_password(password, user.password):
                raise LoginFailed("Invalid Password.")

        access_token, refresh_token = generate_jwt_tokens(user.id)
        token = refresh_token if remember_me else access_token
        expire_delta = (
            settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60
            if remember_me
            else settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            max_age=expire_delta,
            secure=True,
            samesite="lax",
        )
        return response

    async def is_authenticated(self, request: Request):
        token = request.cookies.get("access_token")
        if not token:
            return None
        try:
            payload = decode_jwt_token(token=token)
            user_id = payload.get("user_id")
            if user_id is None:
                return None
            try:
                user_id = int(user_id)
            except ValueError:
                return None

            if payload.get("exp") < datetime.now(UTC).timestamp():
                return None

            async with async_session_maker() as db:
                stmt = select(User).where(User.id == user_id)
                user = (await db.execute(stmt)).scalars().first()
                if user is None or not user.is_admin or not user.is_active:
                    return None

            return user
        except JWTError:
            return None

    async def logout(self, request: Request, response: Response):
        response.delete_cookie("access_token")
        return response
