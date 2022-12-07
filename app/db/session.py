from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    # required for sqlite
    connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
