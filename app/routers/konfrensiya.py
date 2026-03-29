from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from app.database import db_dep
from app.models import Seminar,Defense
from app.schemas import SeminarResponse,DefenseResponse

router = APIRouter(prefix="/konfrensiya", tags=["Konfrensiya"])


@router.get("/list", response_model=Page[SeminarResponse])
async def seminar_list(db: db_dep):
    stmt = select(Seminar).order_by(Seminar.start_date.desc())
    
    return await paginate(db,stmt)


@router.get("/{seminar_id}", response_model=SeminarResponse)
async def get_seminar(seminar_id: int, db: db_dep):
    stmt = select(Seminar).where(Seminar.id == seminar_id)
    res = await db.execute(stmt)
    seminar = res.scalar_one_or_none()
    if not seminar:
        raise HTTPException(status_code=404, detail="Seminar topilmadi")
    return seminar

@router.get("/list",response_model=Page[DefenseResponse])
async def defense_list(db:db_dep):
    stmt=select(Defense).order_by(Defense.start_date.desc())
    return await paginate(db,stmt)


@router.get("/{defense_id}/",response_model=DefenseResponse)
async def defense_one(defense_id:int,db:db_dep):
    stmt=select(Defense).where(Defense.id==defense_id)
    res= (await db.execute(stmt)).scalars().first()

    if not res:
        raise HTTPException(status_code=404,detail="Defense topilmadi")
    return res