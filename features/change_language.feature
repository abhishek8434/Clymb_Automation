Feature: Workflow to submit appreciation log
  As a student
  I want to test the full workflow to submit appreciation
  So that I can ensure all steps are executed correctly

  # Positive Scenario
  Scenario: Execute the full workflow in sequence (Positive Flow)
    Given I am logged into the application1
    When I scroll to the end of the page1
    And I click on the appreciation audio button1
    And I click on the appreciation log audio button1
    And I select an appreciation randomly1
    Then I submit the appreciation1
