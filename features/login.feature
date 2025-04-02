Feature: Heroku Login Functionality

  Scenario: User logs into Heroku successfully
    Given I open the Heroku login page
    When I enter valid Heroku credentials
    Then I should be logged into Heroku successfully
