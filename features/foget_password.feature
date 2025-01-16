Feature: Workflow for appreciation station to check correct appreciation is logged or not
  As a student
  I want reset my password
  So that I can login with new password

  Scenario: Student reset password successfully
    Given Student is on login page
    When Student click on forget password link
    And Student enter email on the field
    And Student click on reset password button
    Then Student should see the success message for reset password