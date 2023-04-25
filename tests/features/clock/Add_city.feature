Feature: Add city time
  As a member I want to add city time zone into my clock

  Scenario Outline:
    Given I verify_that 'current_title_screen' is 'Clock'
    When I click_on 'clock_tab'
    And I add_city '<city>'
    Then I verify_result_current_city_time_zone is '<city>'

    Examples:
    | city        |
    | New York    |
    | Bangkok     |
    | Ho Chi Minh |

