from behave import given, when, then
from src.database import get_session
from src.repositories.obo_term_repository import OBOTermRepository
from src.obo_parser import parse_obo_file

@given("I have an OBO file")
def step_given_obo_file(context):
    context.obo_file_path = "./features/sample.obo"


    SessionLocal, _ = get_session()
    context.db = SessionLocal()

    context.repository = OBOTermRepository(context.db)


@when("I parse the file")
def step_when_parse_file(context):
    context.parsed_data = parse_obo_file(context.obo_file_path)

@then("I should be able to store its data in the database")
def step_then_store_in_database(context):

    try:
        context.repository.store_obo_terms(context.parsed_data)
        context.db.commit()
    except Exception as e:
        context.db.rollback()
        raise e
    finally:
        context.db.close()