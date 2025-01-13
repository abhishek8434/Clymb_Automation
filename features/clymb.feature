Feature: Workflow for mood reporting of student with all 5 steps 
  As a student
  I want to execute the workflow steps sequentially
  So that I can validate the complete flow

  Scenario: Execute the full workflow
    Given the student logs into the application
    When the student interacts with the Compass Dashboard Audio
    And the student clicks on the audio button
    And the student selects a random emotion
    And the student interacts with a random slider
    And the student clicks the first 'Next' button
    And the student selects a random mood
    And the student selects audio emotions
    And the student clicks the second 'Next' button
    And the student checks for the 'Ask For Help' popup
    And the student selects responsible decision making
    And the student clicks the third 'Next' button
    And the student handles self-management actions
    And the student clicks the fourth 'Next' button
    And the student selects a social awareness option
    And the student clicks the fifth 'Next' button
    And the student selects relationship skills options
    Then the student submits the form
    And the student interacts with the final modal or resource popup


  # Negative Scenarios

  Scenario: Login failure due to invalid credentials
    Given Student try to log into the application with invalid credentials
    Then Student should see a login failure message on screen
