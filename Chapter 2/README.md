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

## Best practices

* Seperating unit test from the src as a seperte file like `Root/src` & `Root/tests`
* Seperate functional and unit test as functional test only break if overall function is changed.
*
