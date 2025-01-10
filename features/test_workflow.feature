Feature: Test the login and workflow across multiple tabs

  Scenario: Perform workflow in both main application and admin application
    Given I log in to the main application
    And I log in to the admin application
    When I switch back to the main application
    And I click "Ask For Help"
    Then I should be able to extract the name from the main application
    When I switch to the admin application
    Then I should verify the extracted name in the admin application
