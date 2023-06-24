# import uvicorn
from app.core.config import settings

# from app.db.base_class import Base
# from app.db.session import engine
from app.routers import items, login, users
from fastapi import FastAPI

# Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
