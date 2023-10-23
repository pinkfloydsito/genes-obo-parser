from behave import given, when, then, step
from src.database import get_session
from src.repositories.obo_term_repository import OBOTermRepository
from src.obo_parser import parse_obo_file
from src.models import OBOTerm

@given("I have an OBO file with a parent term")
def step_given_obo_file(context):
    context.obo_file_path = "./features/parent_obo_term.obo"

    SessionLocal, _ = get_session()
    context.db = SessionLocal()

    context.repository : OBOTermRepository = OBOTermRepository(context.db)


@when("I parse the file with the parent term")
def step_when_parse_file(context):
    context.parsed_data = parse_obo_file(context.obo_file_path)

@then("I should be able to store its parent data in the database")
def step_then_store_in_database(context):
    db = context.db
    try:
        context.repository.store_obo_terms(context.parsed_data)
        db.commit()

    except Exception as e:
        context.db.rollback()
        raise e
    finally:
        context.db.close()

@then('I retrieve the OBOTerm with id "{term_id}" from the database')
def step_then_retrieve_obo_term(context, term_id: str):
    obo_term = context.repository.get_obo_term_by_id(id=term_id)
    context.obo_term = obo_term

@then("I validate the following attributes")
def step_then_validate_attributes(context):
    expected_is_root_value : bool = True
    expected_alternatives : str = 'GO:0000004, GO:0007582, GO:0044699'

    obo_term : OBOTerm = context.obo_term

    assert getattr(obo_term, 'alternatives') == expected_alternatives, f"Attribute alternatives does not match expected value {expected_alternatives}"
    assert obo_term.is_root == expected_is_root_value, f"Attribute is_root does not match expected value {expected_is_root_value}"