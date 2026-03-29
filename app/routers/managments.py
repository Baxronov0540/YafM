from fastapi import APIRouter
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

    res= await db.execute(stmt)
    managements=res.scalars().all()

    return managements

