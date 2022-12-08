from abc import abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base


class BaseDB:
    def __init__(self, db_uri):
        self.db_uri = db_uri
        self.create_engine()
        Base.metadata.create_all(bind=self.engine)

    @abstractmethod
    def create_engine(self):
        pass

    def get_session(self):
        session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        return session


class SQLiteDB(BaseDB):
    def create_engine(self):
        self.engine = create_engine(
            self.db_uri, connect_args={"check_same_thread": False}
        )


class PostgresDB(BaseDB):
    def create_engine(self):
        self.engine = create_engine(self.db_uri)
