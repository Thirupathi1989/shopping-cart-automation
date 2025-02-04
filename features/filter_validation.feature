Feature: Filter Validations

  Scenario Outline: Verify user is able to filter items using different size filters
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user selects different size "<Sizes>"
    Then the items displayed should be filtered by size "<Sizes>"
  Examples:
    | Sizes |
    | XS    |
    | S     |
    | M     |
    | ML    |
    | L     |
    | XL    |
    | XXL   |

  Scenario: Verify user is able to apply multiple filters at once
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user selects size "S"
    Then the total items count is "2"
    When the user selects size "M"
    Then the total items count is "1"
    When the user filtered multiple size "L" and "XL"
    Then the total count based on filtered by sizes is "16"