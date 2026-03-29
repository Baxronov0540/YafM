from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.database import db_dep
from app.models import Seminar
from app.schemas import SeminarResponse

router = APIRouter(prefix="/seminar", tags=["Seminar"])


@router.get("/list", response_model=list[SeminarResponse])
async def seminar_list(db: db_dep):
    stmt = select(Seminar).order_by(Seminar.start_date.desc())
    res = await db.execute(stmt)
    seminars = res.scalars().all()
    return seminars


@router.get("/{seminar_id}", response_model=SeminarResponse)
async def get_seminar(seminar_id: int, db: db_dep):
    stmt = select(Seminar).where(Seminar.id == seminar_id)
    res = await db.execute(stmt)
    seminar = res.scalar_one_or_none()
    if not seminar:
        raise HTTPException(status_code=404, detail="Seminar topilmadi")
    return seminar
