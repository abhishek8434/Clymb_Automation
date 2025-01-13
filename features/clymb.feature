Feature: Full Workflow Execution
  As a user
  I want to execute the workflow steps sequentially
  So that I can validate the complete flow

  Scenario: Execute the full workflow
    Given the user logs into the application
    When the user interacts with the Compass Dashboard Audio
    And the user clicks on the audio button
    And the user selects a random emotion
    And the user interacts with a random slider
    And the user clicks the first 'Next' button
    And the user selects a random mood
    And the user selects audio emotions
    And the user clicks the second 'Next' button
    And the user checks for the 'Ask For Help' popup
    And the user selects responsible decision making
    And the user clicks the third 'Next' button
    And the user handles self-management actions
    And the user clicks the fourth 'Next' button
    And the user selects a social awareness option
    And the user clicks the fifth 'Next' button
    And the user selects relationship skills options
    Then the user submits the form
    And the user interacts with the final modal or resource popup


  # Negative Scenarios

  Scenario: Login failure due to invalid credentials
    Given I try to log into the application with invalid credentials
    Then I should see a login failure message
