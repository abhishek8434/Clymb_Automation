Feature: Test the login and workflow across multiple tabs
  As a admin
  I want to execute the workflow for ask for help functionality
  So that admin will verify when student submit ask for help then it is getting displayed to admin correctly


  Scenario: Perform workflow in both main application and admin application
    Given I log in to the main application as student
    And I log in to the admin application
    When I switch back to the main application
    And I click "Ask For Help"
    Then I should be able to extract the name from the main application
    When I switch to the admin application
    Then I should verify the extracted name in the admin application


  # Negative Scenarios

  Scenario: Login failure due to invalid credentials
    Given When try to log into the application with invalid credentials
    Then Student should see a login failure message
