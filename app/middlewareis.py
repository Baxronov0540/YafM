from time import time

from fastapi import Request
from app.utils import current_lang
from starlette.middleware.base import BaseHTTPMiddleware


class LanguageMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        lang = request.headers.get("accept-language")
        if not lang:
            lang="uz"
        if lang not in ["uz", "en", "ru"]:
            lang = "uz"
        token = current_lang.set(lang)
        try:
            response = await call_next(request)
            return response
        finally:
            current_lang.reset(token)
class  TimeRequestMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        start_date=time()
        response = await call_next(request)
        end_date=time()
        response.headers["X-Process-Time"] = str(end_date - start_date)
        return response
        