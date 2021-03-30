# Testing

The ProVax team has decided to use Selenium for our testing needs. The success of the ProVax app is dependent on our users being able to access each element. Using Selenium to automate navigation of those elements ensures that all use cases are thoroughly covered during testing.

## Accessing tests:  
There are two test cases currently which are located in src -> pages -> tests.py file. In order to run the tests, Selenium and pytest must be added in your django_env virtual environment. 
## The tests
* The first test emulates a user navigating to the homepage and clicking the "Am I eligible?" button which will open /create. 
* The second test begins on the create page and demonstrates successful choices being selected on our drop down menus. The submit button was not tested this sprint since its functionality is still being developed.
