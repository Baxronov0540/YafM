from .news import router as news_router
from .konfrensiya import router as seminar_router
from .labaratory import router as labaratory_router
from .managments import router as managment_router
from .slider import router as slider_router
from .workers import router as worker_router

__all__ = [
    "news_router",
    "seminar_router",
    "labaratory_router",
    "managment_router",
    "slider_router",
    "worker_router",
]
