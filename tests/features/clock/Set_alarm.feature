Feature: Set alarm
    As a member I want to set alarm using my Clock app

  Scenario: Set new alarm
    Given I 'verify_current_App_is_running_foreground_is_Clock' on 'clock_page'
    When I 'click_on' 'alarm_tab' on 'clock_page'
    And I 'set_alarm' '3:15PM' on 'clock_page'
    Then I 'verify_alarm_set' is '3:15PM' on 'clock_page'

