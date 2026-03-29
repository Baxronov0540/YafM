from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database import db_dep
from app.models import Manaagement
from app.schemas import ManaagementResponse

router = APIRouter(prefix="/managments", tags=["Managments"])


@router.get("/list", response_model=list[ManaagementResponse])
async def managment_list(db: db_dep):
    stmt = (
        select(Manaagement)
        .options(joinedload(Manaagement.image))
        .order_by(Manaagement.created_at.desc())
    )

    res = await db.execute(stmt)
    managements = res.scalars().all()

    return managements


@router.get("/{management_id}", response_model=ManaagementResponse)
async def get_management(management_id: int, db: db_dep):
    stmt = (
        select(Manaagement)
        .where(Manaagement.id == management_id)
        .options(joinedload(Manaagement.image))
    )
    res = await db.execute(stmt)
    management = res.scalar_one_or_none()
    if not management:
        raise HTTPException(status_code=404, detail="Boshqaruv ma'lumoti topilmadi")
    return management
