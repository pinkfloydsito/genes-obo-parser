import argparse
import csv

from src.database import get_session
from src.repositories.obo_term_repository import OBOTermRepository

import sys
sys.setrecursionlimit(500)

parser = argparse.ArgumentParser(description='Choose the csv file to process')
parser.add_argument('file_path', type=str, help='Path to the csv file')
parser.add_argument('output_file_path', type=str, help='Path to the csv file for the output')
parser.add_argument('counting_file_path', type=str, help='Path to the csv file for the counting')

args = parser.parse_args()
file_path = args.file_path
output_file_path = args.output_file_path
counting_file_path = args.counting_file_path


SessionLocal, engine = get_session()

db = SessionLocal()
obo_term_repo = OBOTermRepository(db)

import csv

def get_parent_from_term(term_id: str):
    result = []
    term = obo_term_repo.get_obo_term_by_id(term_id)
    if term is None:
        return result

    if term.is_root:
        # result.append(term_id)
        return result

    if term.parents: 
        if term.alternatives:
            alternatives = term.alternatives.split(', ')
            for alternative in alternatives:
                result += get_parent_from_term(alternative)

        parents = term.parents.split(', ')

        if 'GO:0005575' in parents or 'GO:0003674' in parents or 'GO:0008150' in parents:
            result.append(term.id)

            return result

        for parent in parents:
            result += get_parent_from_term(parent)

        return result

    if term.is_obsolete and term.alternatives is None and term.parents is None:
        return result

    if term.is_obsolete or term.alternatives:
        alternatives = term.alternatives.split(', ')
        for alternative in alternatives:
            result += get_parent_from_term(alternative)
    
    return result
    
        
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader, None)

    new_data = []
    for row in csvreader:
        if any("GO:" in field for field in row):
            filtered_row = [field for field in row if field.strip() != '' and 'GO:' in field]
            
            new_row = []
            for field in filtered_row:
                new_row += get_parent_from_term(field)

            new_data.append(new_row)
    
count_result = {
} 

for row in new_data:
    ids = list(set(row))
    terms = obo_term_repo.get_obo_terms_by_ids(ids)
    for term in terms:
        key = f'{term[0].id}-{term[0].namespace}'
        count_result[key] = count_result.get(key, 0) + 1

with open(counting_file_path, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    for key, count in count_result.items():
        csvwriter.writerow([key, count])


with open(output_file_path, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    for row in new_data:
        csvwriter.writerow(list(set(row)))


db.commit()
db.close()