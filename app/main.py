from app.db.base_class import Base

# from app.db.db import base
from app.models import Item, User
from fastapi import FastAPI

from .db.db import engine

# from .database.db import engine
from .routers import items, users

Base.metadata.create_all(bind=engine)

# models.Base.metadata.create_all(bind=engine)
item.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
