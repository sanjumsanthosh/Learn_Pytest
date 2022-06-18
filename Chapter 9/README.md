# Chapter 9 - Covereage

### Introduction

It is a tool that measures code coverge watch your code whiel a test suite is being run and keep track of which lines are hit and which are not

* line coverage : calculated by dividing the total number of lines run by total lines in code
* branch coverage : can tell if all paths are taken in control statements

prefred method is to use pytest-cov with coverage.py

## Tests

### Using coverage.py with pytest-cov

* Running test with coverage.py
  * --cov flag and provider either a path to code or the installed pacakge for testing
  * eg : pytest --cov=cards
* pytest-cov runs in conjuction with coverage so example
  * pytest --cov=cards ch7 will
    * run `coverage run --source=cards -m pytest ch7`
    * `coverage report`
* Also we can use `.coveragerc` file to specify the working package directory instead of card directory so that they we can get a better idea of coverage from source

```
[paths]
source =
   cards_proj/src/cards
   */site-packages/cards
```

* we can also add missing lines to report by re-running with following
  * pytest --cov=cards --cov-report=term-missing ch7
  * coverage report --show-missing
* even if we run pytest we can get report by coverage report

### Generating HTML Report

* use cov-report=html or coverage html to generate html report
* The report htmlcov/ is placed in the directory where the test is run

### Excluding code from coverage

* exclude some lines from being tested
* example if(__name__=="__main__") blocks
* for ignoring we can use `#pragma: no cover`. eg
* ```
  if __name__ == "__main__": #pragma: no cover
      main()
  ```
* ️ ***Beware that never add tests just to make the coverage 100%***  🚀️

### Running coverage on tests

* adding test directory on our coverage report like
  * pytest --cov=cards --cov=. --cov-report=html
  * pytest --cov=cards --cov=test_dir test
* Why?
  * To find test with duplicate names, as sometimes only one will be executed
  * we forgot all the function names to make it unique
  * can help to fix unused or dead code inside fixtures

### Running coverage on a directory

* can pass a directory with --cov=ch9/some_code or even a parent directory
* why?
  * this can help in paying attention to group of files instead of a single package
