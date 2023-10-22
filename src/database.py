from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .config import config

DATABASE_URL = config('DATABASE_URL')

def get_session():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal, engine