from fastapi import APIRouter, HTTPException

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database import db_dep
from app.models import Slider
from app.schemas import SliderResponse

router = APIRouter(prefix="/slider", tags=["Slider"])


@router.get("/list", response_model=list[SliderResponse])
async def slider_list(db: db_dep):
    stmt = (
        select(Slider)
        .options(joinedload(Slider.image))
        .order_by(Slider.created_at.desc())
    )
    res = await db.execute(stmt)
    sliders = res.scalars().all()
    return sliders


@router.get("/{slider_id}", response_model=SliderResponse)
async def get_slider(slider_id: int, db: db_dep):
    stmt = (
        select(Slider).where(Slider.id == slider_id).options(joinedload(Slider.image))
    )
    res = await db.execute(stmt)
    slider = res.scalar_one_or_none()
    if not slider:
        raise HTTPException(status_code=404, detail="Surat topilmadi")
    return slider
