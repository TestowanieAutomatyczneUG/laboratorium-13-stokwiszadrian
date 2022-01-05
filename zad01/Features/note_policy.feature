Feature: Note Policy

  Scenario: Note name none
    Given you want to create a note with name none
    Then it won't work

  Scenario: Note name empty
    Given you want to create a note with empty name
    Then it won't work

  Scenario: Note name not a string
    Given you want to create a note with a name that's not a string
    Then it won't work

  Scenario: Note name string
    Given you want to create a note with a name that's a string
    Then it will work

  Scenario: Note note not a number
    Given you want to create a note with note that's not an int or float
    Then it won't work

  Scenario: Note note smaller than 2
    Given you want to create a note with note smaller than 2
    Then it won't work

  Scenario: Note note bigger than 6
    Given you want to create a note with note bigger than 6
    Then it won't work

  Scenario: Note note between 2 and 6
    Given you want to create a note with note between 2 and 6
    Then it will work


