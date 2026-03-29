from pydantic import BaseModel
from datetime import datetime


class MediaInResponse(BaseModel):
    id: int
    file_path: str


class NewsResponse(BaseModel):
    id: int
    title: str
    body: str
    image: MediaInResponse | None = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserCreateRequest(BaseModel):
    username: str
    password: str
    