from fastapi import APIRouter

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database  import db_dep
from app.models import Slider
from app.schemas import SliderResponse

router=APIRouter(prefix="/slider",tags=["Slider"])

@router.get("/list",response_model=list[SliderResponse])
async def slider_list(db:db_dep):
    stmt=select(Slider).options(joinedload(Slider.image)).order_by(Slider.created_at.desc())
    res=await db.execute(stmt)
    sliders=res.scalars().all()
    return sliders

