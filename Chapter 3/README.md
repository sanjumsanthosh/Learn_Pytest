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

### Dynamically declaring fixture scope

* Fixture scopes can be declared dynamically uring the following steps
  * declare fixture scope as a variable
    `@pytest.fixtures(scope=db_scope)`
  * declare function db_scope with 2 parameters, fixture_name& config
    * should return the fixture type
  * write a hook to allow pytest to use a command-line flag to control this

### autouse

* autouse is a parameter defined in fixtures which asks it to run the fixture all the time. Like for instance print the time elapsed for each tests.

### Renaming fixtures

* we can use name argument of @pytest.fixtures anotation to rename the fixtures.
* ## Tips & tricks
* If the test result is "Fail", then its something wrong with the test function. But if its an "Error" then its something related to fixture.
* you can use --setup-show command line flag to show details of when the fixture was setup and tore down.
* --fixture flag can be used to find all the fixtures.
* use --fixtures-per-test to see what fixtures are used by each test and where the fixtues are defined.
* -s flag is a shotcut for --capteru=no. It tells pytest to turn off output capture. Without truning off output capture, pytest only prints the output of tests that fail.
