from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, Session
from .database import engine

Base = declarative_base()

class OBOTerm(Base):
    __tablename__ = 'obo_terms'

    id = Column(String, primary_key=True)
    name = Column(String)
    namespace = Column(String)
    definition = Column(String)

Base.metadata.create_all(bind=engine)