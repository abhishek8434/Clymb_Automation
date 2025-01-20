Feature: Workflow to submit appreciation log
  As a student
  I want to test the full workflow to submit appreciation
  So that I can ensure all steps are executed correctly

  @positive
  Scenario: Execute the full workflow in sequence (Positive Flow)
    Given I am logged into the application
    When I scroll to the end of the page
    And I click on the appreciation audio button
    And I click on the appreciation log audio button
    And I select an appreciation randomly
    Then I submit the appreciation

  
  @negative
  Scenario: Login failure due to invalid credentials
    Given I try to log into the application with invalid credentials
    Then I should see a login failure message

