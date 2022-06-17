# Chapter 8 - Configuration Files

##### Mainly those non-test files that affect how pytest runs. If one is constatnly using some configs we can tuck them away in some files.

## Sessions

### Understanding pytest configuration files

* getting to know abt pytest.ini, conftest.py, __init__.py, tox.ini, pyproject.toml & setup.cfg

### Saving settings and flags in pytest.ini

* add [pytest] so that the parser can identify if its pytest or tox.ini file.
* can add the following
  * addopts : additional runtime params e.g. --strict-markers
  * testpaths : the root directory of test... can help to speed up startup time
  * markers: defines the markers with definition. eg marker1:definition1
