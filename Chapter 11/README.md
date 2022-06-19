# Chapter 11 - tox & continuous integration

Continuous integration reefers to the practice of merging all developers code chanes into a shared repo on a regular basic. Tox is an automation tool that works a lot like a ci tool but can be run both locally and on server.

## Sessions

### What is CI

* Earlier there was integration, which is like a group merge when muliple code changes were available
* CI is a tool which build an drun tests all on their own, ususally triggered by an MR
* This frequency makes it so that the code changes is smaller and reduces the chance of Merge conflicts
* CI tools have the ability to merge automaticaly but usually merging is done manually after code reviews

### Introducing tox

* CI helps to run the complete test suits in muliple env. python as well as os
* tox uses info from setup.py / pyproject.toml to create an installable distribution and looks in tox.ini for a list of environments.
* for each it will
  * create a virtual env in a .tox direcotry
  * pip install some dependencies
  * builds your packages
  * pip install you pacakge
  * runs the test
* after the run it will give a summary of hwo they all did

### Setting up tox

* cards_proj
  * pyproject.toml
  * pytest.ini
  * tox.ini
    * src ...
    * tests...
* tox.ini file have following parameters
  * [tox]
    * **envlist = py310** --> shorthand to tell tox to run in python 3.10
    * **isolated_build = True** --> for pyproject.toml we need this .. but optional in setup.py
  * [testenv]
    * **deps =** --> install both there tools for testing can also specify version
      pytest == 6.2.4 -> can also specify version
      faker
    * **commands = pytest** --> tells tos to run pytest in each env
* Build instructions in **pyproject.toml** file

### Running tox

* tox can be run by changing to the directory and executing tox

### Testing multiple python versions

* The following changes should be made to tox.ini file
  * [tox]
    * envlist = python3.7, python3.8, python3.9
    * isolated_build = True
    * skip_missing_interpreters = True -> with it set to true, tox will skip in case of missing versions

### Running tox environments in Parallel

* We can run in parallel by adding -p flag
* `tox -c .\tox_mulitple_pythons.ini -p`

### Adding a coverage Report to tox

* To add a coverage report we need to include pytest-cov to deps which will add all the dependent packages
* When using coverage with tox it is good to set up `.coveragerc` file to let coverage know ehich source should be considerd
  * in `.coveragerc` including `src`will work with local & for the for other CI it will look for `.tox` folder
  * `tox -c .\tox_coverage.ini -e python3.10`

## Tips & Tricks

* you can run a custom `tox -c tox_mulitple_pythons.ini`
