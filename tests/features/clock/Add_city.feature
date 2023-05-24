Feature: Add city time
  As a member I want to add city time zone into my clock

  Scenario Outline:
    Given I 'verify_current_App_is_running_foreground_is_Clock' on 'clock_page'
    When I 'click_on' 'clock_tab' on 'clock_page'
    And I 'add_city' '<city>' on 'clock_page'
    Then I 'verify_result_current_city_time_zone' is '<city>' on 'clock_page'

    Examples:
    | city        |
    | New York    |
    | Bangkok     |
    | Ho Chi Minh |

