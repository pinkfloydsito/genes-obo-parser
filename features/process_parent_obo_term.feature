Feature: OBO Parent Term Processing

  Scenario: Retrieve and Validate OBOTerm from the Database
    Given I have an OBO file with a parent term
    When I parse the file with the parent term
    Then I should be able to store its parent data in the database
    Then I retrieve the OBOTerm with id "GO:0008150" from the database
    Then I validate the following attributes:
      | Attribute     | Expected Value         |
      | is_root       |  True                  |
      | alternatives  | GO:0000004,GO:0007582,GO:0044699  |