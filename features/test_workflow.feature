Feature: Test Workflow with Multiple Tabs
  As a user
  I want to perform a workflow using multiple browser tabs
  So that I can validate interactions across both the main and admin applications

  Scenario: Execute the full workflow with tabs
    Given the user logs into the student application
    
    When the user logs into the admin application
    And the user switches back to the main application
    And the user extracts a name and performs "Ask For Help" actions
    Then the user verifies the extracted name in the admin tab
    And the workflow execution is completed
