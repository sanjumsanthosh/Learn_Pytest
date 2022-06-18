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
