Feature: Set alarm
    As a member I want to set alarm using my Clock app

  Scenario: Set new alarm
    Given I verify_that 'current_title_screen' is 'Clock'
    When I click_on 'alarm_tab'
    And I set_alarm '3:15AM'
    Then I verify_alarm_set is '3:15AM'