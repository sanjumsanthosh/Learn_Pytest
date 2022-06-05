---

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
