from sqlalchemy import Column, String, ForeignKey, Boolean, Integer, Sequence
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

class OBOTermMap(Base):
    __tablename__ = 'obo_term_map'

    id = Column(Integer, Sequence('obo_term_map_id'), primary_key=True)
    from_term = Column(String)
    to_term = Column(String)

Base.metadata.create_all(bind=engine)