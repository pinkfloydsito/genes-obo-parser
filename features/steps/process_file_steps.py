from behave import given, when, then
from src.database import SessionLocal, store_obo_terms

from src.obo_parser import parse_obo_file

@given("I have an OBO file")
def step_given_obo_file(context):
    context.obo_file_path = "./features/sample.obo"


@when("I parse the file")
def step_when_parse_file(context):
    parse_obo_file(context.obo_file_path)

@then("I should be able to store its data in the database")
def step_then_store_in_database(context):
    db = SessionLocal()

    try:
        store_obo_terms(db, context.parsed_data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()