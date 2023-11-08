from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import select, or_

from src.models import OBOTerm

class OBOTermRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_obo_term_by_id(self, id: str) -> OBOTerm:
        query = select(OBOTerm).filter_by(id=id)

        term = self.db.execute(query).fetchone()
        if term is None:
            return None

        return term[0]

    def get_obo_terms_by_ids(self, ids: list[str]) -> list[OBOTerm]:
        query = select(OBOTerm).where(OBOTerm.id.in_(ids))

        terms = self.db.execute(query).fetchall()

        return terms

    def get_obo_term_by_patterns(self, patterns: list[str]):
        query = select(OBOTerm).where(or_(*[OBOTerm.id.like(f"%{pattern}%") for pattern in patterns]))

        results = self.db.execute(query).fetchall()

        return results

    def store_obo_terms(self, obo_data: list[dict]):
        """
        Store a list of OBO terms in the database.

        Args:
            obo_data (list): List of dictionaries containing term data.
        """
        for term_data in obo_data:
            alternatives : list[str] = term_data.get('consider') + term_data.get('alt_id') + term_data.get('replaced_by')
            parents : list[str] = term_data.get('is_a')

            str_alternatives = ', '.join(alternatives) if alternatives else None
            str_parents = ', '.join(parents) if parents else None

            is_root = False

            if parents == [] and term_data['is_obsolete'] is False:
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