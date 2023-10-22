Feature: OBO File Processing

  Scenario: Parse and Store OBO File
    Given I have an OBO file
    When I parse the file
    Then I should be able to store its data in the database
