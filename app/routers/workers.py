from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from app.database import db_dep
from app.models import Worker
from app.schemas.labaratory import WorkerResponse

router = APIRouter(prefix="/workers", tags=["Workers"])


@router.get("/list", response_model=list[WorkerResponse])
async def worker_list(db: db_dep):
    stmt = (
        select(Worker)
        .options(joinedload(Worker.image))
        .order_by(Worker.created_at.desc())
    )
    res = await db.execute(stmt)
    workers = res.scalars().all()
    return workers


@router.get("/{worker_id}", response_model=WorkerResponse)
async def get_worker(worker_id: int, db: db_dep):
    stmt = (
        select(Worker).where(Worker.id == worker_id).options(joinedload(Worker.image))
    )
    res = await db.execute(stmt)
    worker = res.scalar_one_or_none()
    if not worker:
        raise HTTPException(status_code=404, detail="Xodim topilmadi")
    return worker
