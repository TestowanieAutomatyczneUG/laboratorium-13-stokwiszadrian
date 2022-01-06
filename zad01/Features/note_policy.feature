Feature: Note Policy

  Scenario: Note name none
    When you want to create a note with name none
    Then Note with a None value for a name won't be created

  Scenario: Note name empty
    When you want to create a note with empty name
    Then Note with an empty name won't be created

  Scenario: Note name not a string
    When you want to create a note with a name that's not a string
    Then Note with a name that's not a string won't be created

  Scenario: Note name string
    When you want to create a note with a name that's a string
    Then Note with given string will be created

  Scenario: Note note not a number
    When you want to create a note with note that's not an int or float
    Then Note with NaN note won't be created

  Scenario: Note note smaller than 2
    When you want to create a note with note smaller than 2
    Then Note with a note smaller than 2 won't be created

  Scenario: Note note bigger than 6
    When you want to create a note with note bigger than 6
    Then Note with a note bigger than 6 won't be created

  Scenario: Note note between 2 and 6
    When you want to create a note with note between 2 and 6
    Then Note with given note will be created


