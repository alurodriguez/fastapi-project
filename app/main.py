from app.db.base_class import Base
from app.db.session import engine
from fastapi import FastAPI

from .routers import items, users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
