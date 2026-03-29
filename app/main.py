from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.requests import Request
from app.utils import current_lang
from app.middlewareis import LanguageMiddleware,TimeRequestMiddleware



from app.routers import (
    news_router,
    seminar_router,
    labaratory_router,
    managment_router,
    slider_router,
    worker_router,
    
)
from app.admin import admin

app.include_router(slider_router)
app.include_router(news_router)
app.include_router(seminar_router)
app.include_router(labaratory_router)
app.include_router(managment_router)
app.include_router(worker_router)

admin.mount_to(app=app)

add_pagination(app)
app.add_middleware(LanguageMiddleware)
app.add_middleware(TimeRequestMiddleware)