from datetime import datetime
from pydantic import BaseModel
from .labaratory import ImageResponse

class ManaagementResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    reception_hours: str
    position: str | None = None
    email: str | None = None
    phone: str | None = None
    degree: str | None = None
    image: ImageResponse
    created_at: datetime
    updated_at: datetime