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
    name:str
    body:str
    image:ImageResponse
    worker:WorkerResponse
    created_at:datetime
    updated_at:datetime
    
    class Config:
        from_attributes = True

class SectionResponse(BaseModel):
    id:int
    name:str
    body:str
    image:ImageResponse
    worker:WorkerResponse
    created_at:datetime
    updated_at:datetime
    
    class Config:
        from_attributes = True