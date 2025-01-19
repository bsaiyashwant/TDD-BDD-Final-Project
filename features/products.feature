Scenario: Reading a product
    Given a product exists with ID 1
    When I send a GET request to "/products/1"
    Then I should receive the product details

Scenario: Updating a product
    Given a product exists with ID 1
    When I send a PUT request to "/products/1" with the updated details
    Then the product should be updated
    And I should receive the updated product details

Scenario: Deleting a product
    Given a product exists with ID 1
    When I send a DELETE request to "/products/1"
    Then the product should be deleted
    And I should receive a confirmation message

Scenario: Listing all products
    Given products exist in the database
    When I send a GET request to "/products"
    Then I should receive a list of all products

Scenario: Searching a product based on Category
    Given products exist in the database with categories
    When I send a GET request to "/products?category=electronics"
    Then I should receive a list of all products in the "electronics" category

Scenario: Searching a product based on Availability
    Given products exist in the database with availability status
    When I send a GET request to "/products?available=true"
    Then I should receive a list of all available products

Scenario: Searching a product based on Name
    Given products exist in the database with specific names
    When I send a GET request to "/products?name=Smartphone"
    Then I should receive the details of the product with the name "Smartphone"

