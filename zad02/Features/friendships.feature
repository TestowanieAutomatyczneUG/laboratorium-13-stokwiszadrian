Feature: Friendships

  Scenario: Add friend when dict is empty
    When adding friendship to an empty dictionary
    Then person 2 will be a friend of person 1
    And not the other way around

  Scenario: Add friend to someone's friend list
    Given person 1 and 2 have some friends
    When making person 2 a friend of person 1
    Then person 2 will be added to person 1 friendlist
    And person 1 friendlist will stay the same

  Scenario: Make friends when dict is empty
    When making friends in an empty dictionary
    Then person 1 will be a friend of person 2 and vice versa

  Scenario: Make friends when person1 already is a friend of person2
    Given person 1 is a friend of person 2
    When making friends of person 1 and person 2
    Then person 2 will be a friend of person 1 but person 2 friendlist won't change

  Scenario: Get a friends list when dict is empty
    When trying to get a friendslist from an empty dict
    Then this person's friendlist will be an empty set

  Scenario: Get a non-empty friendlist
    Given person 1 has some friends
    When trying to get his friendlist
    Then you'll get a set containing his friends

  Scenario: Person 1 is not a friend of person 2
    Given person 2 has some friends, but not person 1
    When checking if person 1 is a friend of person 2
    Then it returns false

  Scenario: Person 1 is a friend of person 2
    Given person 2 has some friends, including person 1
    When checking if person 1 is a friend of person2
    Then it returns true