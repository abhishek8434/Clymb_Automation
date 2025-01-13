Feature: Test workflow for appreciation station

  Scenario: User logs in and completes the appreciation workflow
    Given I am logged into the student application
    When I scroll the page to the end
    And I select an appreciation audio
    And I submit the appreciation log
    And I navigate to my journey tab
    Then I should see the appreciation log in my journey
