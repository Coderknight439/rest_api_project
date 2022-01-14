
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .config import settings
import os


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}'


TEST_DATABASE_URL = f"{SQLALCHEMY_DATABASE_URL}_test"

engine = create_engine(TEST_DATABASE_URL if os.getenv('TESTING') else SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=0)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session():
    return scoped_session(SessionLocal)
