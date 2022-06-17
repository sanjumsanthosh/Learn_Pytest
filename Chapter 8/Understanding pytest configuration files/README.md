# Understanding pytest configuration files

### pytest.ini

* Primary pytest config file
* Changes default ehaviour
* location defines the pytest root directory or **rootdir**

### Conftest.py

* contains fixtures & hook functions.
* exist at rootdir or any subdirectories

### __init__.py

* When put into test subdirectory, this file allows you to have identical test file names in multiple test directories.

### tox.ini, pyproject.toml & setup.cfg

* can be used like pytest.ini
* tox.ini:
  * used by tox ( a commandline automated testing tool )
* pyproject.toml:
  * packaging pthon proects and used to save setting for various tools like pytest
* setup.cfg
  * also a packaging module like pyproject.toml

## General order

cards.py

> - top level project files, src,docs....
> - pytest.ini
> - tests
>   - conftest.py
>   - api
>     - __init__.py
>     - conftest.py
>     - test files for api
>   - cli
>     - init.py
>     - conftest.py
>     - test files for cli
