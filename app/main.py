from fastapi import FastAPI
from fastapi_pagination import add_pagination

app = FastAPI()

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
