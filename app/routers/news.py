from sqlalchemy import select
from sqlalchemy.orm import joinedload
from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from app.database import db_dep
from app.models import News,User
from app.schemas import NewsResponse,UserCreateRequest

from app.utils import password_hash
router = APIRouter(prefix="/news", tags=["News"])


@router.get("/list", response_model=Page[NewsResponse])
async def news_list(db: db_dep):
    stmt = select(News).options(joinedload(News.image)).order_by(News.created_at.desc())
    return await paginate(db, stmt)


@router.get("/{news_id}", response_model=NewsResponse)
async def get_news(news_id: int, db: db_dep):
    stmt = select(News).where(News.id == news_id).options(joinedload(News.image))
    res = await db.execute(stmt)
    news_item = res.scalar_one_or_none()
    if not news_item:
        raise HTTPException(status_code=404, detail="Yangilik topilmadi")
    return news_item

@router.get("/search", response_model=Page[NewsResponse])
async def search_list(title: str, db: db_dep):
    stmt = select(News).options(joinedload(News.image)).where(News.title.ilike(f"%{title}%")).order_by(News.created_at.desc())
    return await paginate(db, stmt)


@router.post("/user")
async def create_user(db:db_dep,data:UserCreateRequest):
    stmt=select(User).where(User.username==data.username)
    stmt1=select(User)
    res1 = (await db.execute(stmt1)).scalars().first()
    res = (await db.execute(stmt)).scalar_one_or_none()

    if res:
       raise HTTPException(status_code=400, detail="User already exists")
  
    user=User(
    username=data.username,
    password=password_hash(data.password),
   )  

    if not res1:
        user.is_admin=True

    db.add(user)
    await db.commit()
    return {"message":"User created successfully"}        
