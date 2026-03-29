from pydantic import BaseModel
from datetime import datetime


class MediaInResponse(BaseModel):
    id: int
    file_path: str


class NewsResponse(BaseModel):
    id: int
    title_uz: str
    title_en: str | None = None
    title_ru: str | None = None
    body_uz: str
    body_en: str | None = None
    body_ru: str | None = None
    image: MediaInResponse | None = None
    created_at: datetime
    updated_at: datetime


class UserCreateRequest(BaseModel):
    username: str
    password: str
