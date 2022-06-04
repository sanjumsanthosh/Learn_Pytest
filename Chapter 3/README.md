# Chapter 3

### test fixture

* intro to fixture

### test count initial with fixtures

* fixtures can be used to initilize and destroy objects like here used to manage cardsDB
* use yield to pass execution from fixtures to test function.

### test fixture scope

* fixtures can have muliple scopes... default is function scope

  * function : run once per test function
  * class : run once per test class
  * package : run once per package or directory
  * session : run once per session
* Use conftest to specify larger scope

### test multiple fixture levels

* one can use multiple fixture levels to control the value of fixtures. for example
  * if we use only session fixture all data will be added up
  * so we use a new session fixture to initilize db & a function fixture to delete all records when called. This way we reduce the initization time once per session as well as get a new empty db for each function.

### using Multiple fixtures per test or fixture

* we can use multiple fixtures for each test function as well as for each new fixtures. Make sure that the new fixture have a equal/tighter narrow scope that the once used.
  * test_multiple_1 uses two fixtures to populate the db
  * test_multiple_2 uses a single new fixture to populate. The new fixtuer populates the data from its side.
* ## Tips & tricks
* If the test result is "Fail", then its something wrong with the test function. But if its an "Error" then its something related to fixture.
* you can use --setup-show command line flag to show details of when the fixture was setup and tore down.
* --fixture flag can be used to find all the fixtures.
* use --fixtures-per-test to see what fixtures are used by each test and where the fixtues are defined.
