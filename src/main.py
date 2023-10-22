import argparse

from src.database import get_session
from src.repositories.obo_term_repository import OBOTermRepository
from src.obo_parser import parse_obo_file

parser = argparse.ArgumentParser(description='Process an OBO file and store its data in the database.')
parser.add_argument('file_path', type=str, help='Path to the OBO file')

args = parser.parse_args()
file_path = args.file_path


SessionLocal, engine = get_session()

db = SessionLocal()
obo_term_repo = OBOTermRepository(db)

obo_data = parse_obo_file(file_path)

obo_term_repo.store_obo_terms(obo_data)

db.commit()
db.close()