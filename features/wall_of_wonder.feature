Feature: Wall of Wonder photo upload and post creation
  As a student
  I want to create wall of wonder post
  So that it will reflect on wall of wonder section after approval by admin

  Scenario: Student logs in and creates a post on the Wall of Wonder
    Given the student is logged into the application
    When the student creates a new wall of wonder
    And the student enters text on the wall
    And the student adds a photo to the wall
    And the student selects a random photo
    And the student makes a post
    Then the post should be successfully created
