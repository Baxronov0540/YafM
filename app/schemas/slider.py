from datetime import datetime

from pydantic import BaseModel

from .labaratory import ImageResponse

class SliderResponse(BaseModel):
    id:int
    title:str
    description:str|None=None
    image:ImageResponse
    created_at:datetime
    updated_at:datetime
    
    class Config:
        from_attributes = True
