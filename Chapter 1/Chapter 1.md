# Chapter 1

### test one

* testing assert if passing

### test two

* testing assert if failing

### test three

* testing named tuples
* testing how to access them

### test four

* tesing _asdict()
* testing _replace()

## A short intro on the options available

* --help -> help
* --collect-only -> show all test without running it
* -k expressions -> run test by filtering with an expression
* -v --verbose -> get more info
* -m Markexpr -> mark a subset of test functions with anotation (`@pytest.mark.something_something`) and run with `pytest -m something_something`
* -x -exitfirst -> stop entire test immediately when a test fails
* -maxfail=number -> max number of tests to fail before exiting maxfail=1 == -x
* -s & -capture=method -> print debug statements with the stdout... good for debugging. same as `--capture=no`
  * other options include --capture=fd -> points to file descriptors 1 and 2 to a temp file
  * --capture=sys -> replaces sys.stdout/stderr
* -lf, --last-failed -> run the failing test
* -ff,--failed-first -> same as lf, and runs the rest of the test that passed last time
* -q, --quite -> opposite of -v, display minimal info
* -l,--showlocals -> print local variables and its vaules in tracebacks
* -tb = style
  * short -> short prints just the asser tline
  * E -> evaluated line with no context
  * line -> failure in one line
  * no -> remove the whole traceback
* -duration=N -> reports the slowest n number of tests (like slowest 3 or 4...etc)
* -version -> version
* -h, --help -> needed help incase u forget 👀️
