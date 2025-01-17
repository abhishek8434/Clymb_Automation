Feature: Student Mood Interaction
  As a grade 5 student,
  I want to interact with the mood selection and submission process
  So that I can complete the flow and interact with the audio and emotions.

  Scenario: Grade 5 student mood selection and submission flow
    Given Student is on login page for grade 5 student
    When Student clicks on compass dashboard audio button
    And Student click on audio button for mood
    And Student select any mood emotion randomly
    And Student select focused slider randomly
    And Student click on submit button to submit mood
    Then Student can select sub mood randomly
    And Student clicks on sub mood audio
    And Student click on submit button of sub mood selection
    And Student can fill ask for help pop or close if visible
    And Student can close or submit after mood
