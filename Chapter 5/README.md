# Chapter 5  - Parametrization

## Introduction

Parametrization helops to reuse one test function in may test cases to test more thoroughly with less work. It can accomplised mainly in 3 ways

1. Parametrizing fucntions
2. Parametrizing fixures
3. Using a hook function called pytest_generate_tests

## Tests

### Testing without parametrize

* using 3 different functions
* using a loop to go the the options ... but finally only one funciton. and if one fail we cannot identify which one was the culprit

### Parametrizing Functions

* add parametres to the test definition using `@pytest.mark.parametrize(variables,values)`

### Parametrizing Fixtures

* Here the parametres are passed in fixtures as `@pytest.fixture(params=[...])`
* and the funtion must have a request fixture which returns request.param

### Parametrizing with pytest_generate_tests

* Example of how to use the hook

  ```
  def pytest_generate_tests(metafunc):
      if "start_state" in metafunc.fiturenames:
          metafunc.parametrize("start_stae",[....])

  ```
* few possibilities on how to use this in more scenarios

  * we could parametrization based on command-lien flag as metafunc.config.getopeions(flag) is possible and we can add a --excessive flag or --quick flag to monify the parametres
  * can be based on the presesnce of other parameters.
  * parametrize more that one value like
    * metafunc.parametrize("planet,moon",[(v1,m1),(v2,m2)..]

### using keywords to Select Test Cases

we use -k to select test cases. some examples are listed below

* `pytest -v -k todo` : run all of the todo cases
* `pytest -v -k "todo and not (play or create)"` - eleimiate the test cases with play or create
* `pytest -v "test_func_param.py::test_finish"` - running single test with all params
* `pytest -v "test_func_param.py::test_finish[write a book-done]"` - a single param test case

## Tips & tricks

* when using -k its better to enclose in quotes as dashes, brackets and spaces can mess with the command shell
