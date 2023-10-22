from src.database import get_session
from src.repositories.obo_term_repository import OBOTermRepository
from src.obo_parser import parse_obo_file

SessionLocal, engine = get_session()

db = SessionLocal()
obo_term_repo = OBOTermRepository(db)

obo_data = parse_obo_file('./files/go-basic.obo')

obo_term_repo.store_obo_terms(obo_data)

db.commit()
db.close()