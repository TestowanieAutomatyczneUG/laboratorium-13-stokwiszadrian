Feature: Password Validation
    A valid password is required to have at least 8 characters,
    including at least 1 uppercase character, 1 digit and 1 special character


  @letters
  Scenario: a password with 5 letters
    Given there is a password
    And it has 5 letters
    When checking if password is valid
    Then the password is invalid

  @letters
  Scenario: a password with 9 letters
    Given there is a password
    And it has 9 letters
    When checking if password is valid
    Then the password is invalid

  @letters @digits
  Scenario: a password with 8 letters and 1 digit
    Given there is a password
    And it has 8 letters
    And it has 1 digits
    When checking if password is valid
    Then the password is invalid

  @letters @digits @chars
  Scenario: a password with 5 letters, 2 digits, 1 special character
    Given there is a password
    And it has 5 letters
    And it has 2 digits
    And it has 1 special characters
    When checking if password is valid
    Then the password is invalid

  @letters @uppercase @digit
  Scenario: a password with 9 letters, 1 uppercase letter, 1 digit
    Given there is a password
    And it has 9 letters
    And it has 1 uppercase letters
    And it has 1 digits
    When checking if password is valid
    Then the password is invalid

  @letters @uppercase @chars
  Scenario: a password with 7 letters, 2 uppercase letters, 2 special charactes
    Given there is a password
    And it has 7 letters
    And it has 2 uppercase letters
    And it has 2 special characters
    When checking if password is valid
    Then the password is invalid

  @uppercase @chars @digits
  Scenario: a password with 5 uppercase letters, 2 digits, 2 special characters
    Given there is a password
    And it has 5 uppercase letters
    And it has 2 special characters
    And it has 2 digits
    When checking if password is valid
    Then the password is valid

  @letters @uppercase @digits @chars
  Scenario: a password with 5 letters, 1 special character, 1 uppercase letter, 1 digit
    Given there is a password
    And it has 5 letters
    And it has 1 uppercase letters
    And it has 1 special characters
    And it has 1 digits
    When checking if password is valid
    Then the password is valid

  @letters @uppercase @digits @chars
  Scenario: a password with 3 letters, 1 special character, 2 uppercase letter, 1 digit
    Given there is a password
    And it has 3 letters
    And it has 2 uppercase letters
    And it has 1 special characters
    And it has 1 digits
    When checking if password is valid
    Then the password is invalid