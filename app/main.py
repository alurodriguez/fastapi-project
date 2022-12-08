from app.db.base_class import Base
from app.db.session import engine
from fastapi import FastAPI

from app.routers import items, users
from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(users.router)
app.include_router(items.router)
