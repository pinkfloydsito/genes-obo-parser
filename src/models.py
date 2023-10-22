from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .database import get_session

SessionLocal, engine = get_session()
Base = declarative_base()

class OBOTerm(Base):
    __tablename__ = 'obo_term'

    id = Column(String, primary_key=True)
    name = Column(String)
    namespace = Column(String)
    definition = Column(String)
    alternatives = Column(String)
    parents = Column(String)
    is_obsolete = Column(Boolean)
    is_root = Column(Boolean)


Base.metadata.create_all(bind=engine)