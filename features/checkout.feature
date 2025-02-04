Feature: Update and checkout to complete order

  Scenario: Verify user can delete items in cart
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user adds 4 random items with Free shipping to the cart
    Then remove all the product from cart item

  Scenario: Verify user can place order and cart resets
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user selects size "S"
    Then user click checkoutx
    Then an alert message should be displayed with the correct price as the cart total
    When the user refreshes the page
    Then the items in the cart should be reset
