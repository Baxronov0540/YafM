from sqlalchemy import select
from fastapi import HTTPException, APIRouter

from sqlalchemy.orm import joinedload

from app.database import db_dep
from app.models import Labaratory,Section
from app.schemas import LabaratoryResponse,SectionResponse

router=APIRouter(prefix="/labaratory",tags=["Labaratory"])

@router.get("/list", response_model=list[LabaratoryResponse])
async def labaratory_list(db: db_dep):
    stmt = (
        select(Labaratory)
        .options(joinedload(Labaratory.image), joinedload(Labaratory.worker))
        .order_by(Labaratory.created_at.desc())
    )
    res= await db.execute(stmt)
    labaratories=res.scalars().all()

    return labaratories

@router.get("/section/list", response_model=list[SectionResponse])
async def section_list(db: db_dep):
    stmt = (
        select(Section)
        .options(joinedload(Section.worker), joinedload(Section.image))
        .order_by(Section.created_at.desc())
    )
    res= await db.execute(stmt)
    sections=res.scalars().all()

    return sections

    

