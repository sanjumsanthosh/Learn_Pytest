# Chapter 2

### Package details

A new package called cards is develped to write the unit tests. more details are available [Here](cards_proj/README.md).

use `pip install <file-loc> ` to install the package

### Test cards

* Adding basic test cases to test the package we developed

### Test cards fail

* Failing an assertion will give much more info on where the assertion failed and why
* we can run test by calling function under `if __name__ == "__main__"`

### Test alternative fail

* Failure of test occures in case of an uncaught excepiton
  * like assert used in above example
  * can use `pytest.fail(msg)` for adding custom fail logic ( given in example test_alt_fail.py )
  * or any other uncaught excepitons

### Test assertion helper

* A wrapper function to wrap upon a complecated assertion function

### Test experiment

* trigger fail of db as required arguments not passed

### Test excepiton

* Capture error with `pytest.raises`
* Capture more info with `as excepiton` and later assert using `excepiton.value`
* Capturing error with regex

### Test stucture

* Stucturing test into Arrange/Given - Act/when - Assert/Then format

### Test classes

* classes can be used to group together tests and run them at once
* we can also inherit a test class with specific utilities for testing

### Running subset of tests

* single test method : test_module::Test_class::test_method
* all tests in a class : test_module::Test_class
* singel test function : test_module::Test_function
* all tests in a module : test_module
* all test in a directory : pytest path
* test matching a name pattern pytest -k pattern

## Best practices

* Seperating unit test from the src as a seperte file like `Root/src` & `Root/tests`
* Seperate functional and unit test as functional test only break if overall function is changed.
* -vv command line flag shows even more inforamtion during test failures.

## Tips and tricks

* when using -k, we can build complex expressions with the help of an d, not , or and parentheses. Example
  * -k "(dict or ids) and not TEstEquality"
  * -k "equality and not equality_fail"
