Feature: Test workflow for appreciation station
  As a student
  I want to test the full workflow of appreciation
  So that I can ensure correct appreciation is getting logged

  Scenario: Student logs in and completes the appreciation workflow
    Given I am logged into the student application
    When I scroll the page to the end
    And I select an appreciation audio
    And I submit the appreciation log
    And I navigate to my journey tab
    Then I should see the appreciation log in my journey
