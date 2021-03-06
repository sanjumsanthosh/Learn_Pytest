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

### Using tox.ini, pyproject.toml or setup.cfg

* tox.ini : identical to pytest.ini. only diff is the [tox] session
* pyproject.toml : Used for packaging python projects
  * however peotry & filt uses it for project settings
  * pytest is supported in pyproject.toml
* setup.cfg : more like .ini file.
  * here .cfg parser is different than .ini file parser so debuggin will be an issue

### Determining a root directory & config file

* looks for the config file in the directory or regess down the tree until one is find and made the rootDir.
* root directory is the relative root of test node ids
* even if we dont have any config data, its best to keep an empty pytest.ini file at top. It can prevent some delays
* Once done it will print out the rootdir and config files.

### Sharing local fixtures and hook functions with conftest.py

* we can define conftest.py at vaious levels.like if 2 independent test need to share some fixtures we can use a common config at parent folder.
* it would be a good ida to have a single conftest.py file. it may otherwise cause confution on the location of a fixture. otherwise we can use -v

### Avoiding test file name collision

* __init__.py file can be used in pytest to allow to use fuplicate test names.
* so for each directory adding an init.py will forego the presence of same tests.
* Duplicated file names is a confusing error
