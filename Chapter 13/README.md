# Chapter 13 - debugging test failures

python provides many ways to debug problem faster like using editable installes and pdb.

## Tests

### Adding a new feature to the cards project

Lets say we modify a piece of code and would like to test it in real time. But if we directly call the API's via import it would use the older installed version and not the new version. To accomplish something like this, we need to install package in editable mode

### Installing card in Editable Mode

* Installing package in editable format is built in to pip & Flit
* for pip its available for versions above 21.3.1
* Just add -e flag to pip install like `pip install -e ./package_directory`
* We can install package in editable mode and install additonal dependencies using following format
  * `pip install -e "./proj/[test]"`
* This works because all of these dependencies have been defined in pyproject.toml, in a optional dependencies section

### Debugging with pytest Flags

Pytest includes a few command line flags that are useful for debugging like

* Flags to select which all tests to run
  * -lf/--last-failed --> run last failed tests
  * -ff/--failed-first --> Runs all the tests, starting with the last failed
  * -x/--exitfirst --> stop test after first failure
  * --maxfail=num --> stop test after num failures
  * -nf/--new-first --> Runs all the tests, ordered by file modification time
  * --sw/--stepwise --> stops test after first failure, starts at the last failure
  * --sw-skip/--stepwire-skip --> same as --sw but skips the first failure
* Flags to control output
  * -v/--verbose
  * --tb=[auto/long/short/line/native/no] --> controls traceback
  * -l/ --showlocals --> Displays local variables alongside the stacktrace
* Flags to start command line debugger
  * --pdb --> intefactive debugging session at point of failure
  * --trace --> starts the pdb source-code debugger immediately when running each tests
  * --pdbcls --> uses alternative pdb, like ipython's debugger
