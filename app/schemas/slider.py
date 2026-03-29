from datetime import datetime

from pydantic import BaseModel

from .labaratory import ImageResponse


class SliderResponse(BaseModel):
    id: int
    title_uz: str
    title_en: str | None = None
    title_ru: str | None = None
    description_uz: str | None = None
    description_en: str | None = None
    description_ru: str | None = None
    image: ImageResponse
    created_at: datetime
    updated_at: datetime
