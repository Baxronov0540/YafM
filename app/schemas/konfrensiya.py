from datetime import datetime
from pydantic import BaseModel

class SeminarResponse(BaseModel):
    id:int
    full_name:str
    description:str
    duration:int
    start_date:datetime

class DefenseResponse(BaseModel):
    id:int
    full_name:str
    description:str
    duration:int
    start_date:datetime

