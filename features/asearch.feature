Feature: Search Functionality

  @valid_completed  # Passed
  Scenario: Search for valid product
    Given I got navigated to home page
    When I enter valid product into search box field
    And I click on search button
    Then Valid product should get displayed in search results

  @invalid_completed  # Passed
  Scenario: Search for an Invalid product
    Given I got navigated to home page
    When I enter Invalid product in search box field
    And I click on search button
    Then Proper message should be displayed in search results

  @without_prod_completed  # Passed
  Scenario: Search for without entering any product
    Given I got navigated to home page
    When I dont enter any product in search box field
    And I click on search button
    Then Proper message should be displayed in search results