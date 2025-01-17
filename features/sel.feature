Feature: Workflow for SEL Checkpoint
  As a student
  I want SEL checkpoint
  So that SEL will log on system 

  Scenario: Student can fill SEL Form
    Given Student is on login page to fill SEL form
    When Student clicks on SEL Checkpoint button
    And Student completes all questions and navigates through them
    Then Student successfully submits the SEL form
    And Will verify Success Message
