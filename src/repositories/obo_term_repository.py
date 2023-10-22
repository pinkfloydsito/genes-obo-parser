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
            alternatives : list[str] = term_data.get('consider')
            parents : list[str] = term_data.get('is_a')
            str_alternatives = ', '.join(alternatives) if alternatives else None
            str_parents = ', '.join(parents) if parents else None

            is_root = False

            if parents is None and alternatives is None:
                is_root = True

            term = OBOTerm(
                id=term_data['id'],
                name=term_data['name'],
                namespace=term_data['namespace'],
                definition=term_data['definition'],
                is_obsolete=term_data['is_obsolete'],
                alternatives = str_alternatives,
                parents = str_parents,
                is_root = is_root,
            )
            self.db.add(term)
        self.db.commit()