from datetime import datetime
from  pydantic import BaseModel


class ImageResponse(BaseModel):
    id:int
    file_path:str
    created_at:datetime
    updated_at:datetime
    
class WorkerResponse(BaseModel):
    id:int
    first_name:str
    last_name:str
    position:str
    email:str|None=None
    phone:str|None=None
    image:ImageResponse
    created_at:datetime
    updated_at:datetime 
    
    

class LabaratoryResponse(BaseModel):
    id:int
    name_uz:str
    name_ru:str |None=None
    name_en:str|None=None
    body_uz:str
    body_ru:str|None=None
    body_en:str|None=None
    image:ImageResponse
    worker:WorkerResponse
    created_at:datetime
    updated_at:datetime

class SectionResponse(BaseModel):
    id:int
    name_uz:str
    name_ru:str |None=None
    name_en:str|None=None
    body_uz:str
    body_ru:str|None=None
    body_en:str|None=None
    image:ImageResponse
    worker:WorkerResponse
    created_at:datetime
    updated_at:datetime