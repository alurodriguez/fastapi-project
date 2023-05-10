from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    # SQLALCHEMY_DATABASE_URL
    # required for sqlite
    # connect_args={"check_same_thread": False},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
