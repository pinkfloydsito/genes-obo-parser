from sqlalchemy.orm import Session
from src.models import OBOTerm

class OBOTermRepository:
    def __init__(self, db: Session):
        self.db = db

    def store_obo_terms(self, obo_data: list[dict]):
        """
        Store a list of OBO terms in the database.

        Args:
            obo_data (list): List of dictionaries containing term data.
        """
        for term_data in obo_data:
            term = OBOTerm(
                id=term_data['id'],
                name=term_data['name'],
                namespace=term_data['namespace'],
                definition=term_data['definition'],
            )
            self.db.add(term)
        self.db.commit()