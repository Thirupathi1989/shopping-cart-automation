Feature: Add items to cart

  Scenario: Verify items are listed in cart in the order as added with price
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user adds 4 random items with Free shipping to the cart
    When the user adds 1 random items without Free shipping to the cart
    Then the total cart item count is "4"

  Scenario: Verify user can add same items using Add to cart button
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user adds 4 random items with Free shipping to the cart
    When the user adds 4 random items with Free shipping to the cart
    Then the total cart item count is "8"

  Scenario: Verify user can add item using + button in the cart
    Given launch the browser
    When open firebase homepage
    Then user validate shopping card page title
    When the user adds 4 random items with Free shipping to the cart
    Then add the "Cropped Stay Groovy off white" item using cart