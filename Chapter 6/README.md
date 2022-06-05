# Chapter 6 - Markers

## Introduction

Markers are used to label or tag a test so that we can tell something about them. like we can mark them with `@pytest.mark.slow` or `@pytest.mark.smoke` and run only those markers.

`@pytest.mark.parametrize` is one type of marker we used in chapter 5.

## Tests

### Using Builtin Markers

* `@pytest.mark.filterwarnings(warning)` - adds a warning filter to the given test
* `@pytest.mark.skip(reason=None)` - this marker skips the test with an optional reason
* `@pytest.mark.skipif(condition,..,reason)` - skips on condition
* `@pytest.mark.xfail(condition, ... reason, run=true, raise=None, strict=xfail_strict)` - this test is expected to fail
* `@pytest.mark.parametrize(argnames, argvalues, indirect, ids, scope)` - This marker calls a test function muliple times passing different arguments
* `@pytest.mark.usefixture(fixtureName1, fixtureName2..)` - This marker marks tests as needeing all the specified fixtures

### Skipping with pytest.mark.skip

* skip tests given in @pytest.mark.skip(reason=None) anotation
* sympolised as s in normal or SKIPPED in verbose mode

### Skipping with pytest.mark.skipif

* skip if condifition is true
* if u need to run it anyway use xfail. Its most pbm used in cases where we have like muliple env, eg OS, and have different test for them.

### Expecting tests to fail with pytest.mark.xfail

* it runs anyway by default but we can set run=Fale to stop it.
* raise parameter allows to pass exception type or tuple of exceptions
* can give strict to signify if we need to be XPASS (strict false) or FAIL (strict true)

### Selecting tests with custom markers

* Custom markers are made with @pytest.mark.custom_marker_name
* its also important and good to add these markers in pytest.ini file

  * ```
    [pytest]
    markers=
        smoke: ...
        exception: ...
    ```
* Custom markers can be called with -m flag

### Marking files, classes & parameters

* to mark entire test module add pytestmark attibute with the pytest.mark.mark-name. If you have multiple, u can give it as a list
* Another way is to give a test class and give it as an anottation.
* To specify mark in parameter you can give as below

  ```
  @pytest.mark.parametrize("start_state", [
  "todo",
  pytest.param("in prog", marks=pytest.mark.smoke),
  "done"
  ])
  ```
* You can also mark fixtures as below

  ```
  @pytest.fixture(params=[
      "todo",
      pytest.param("in prog", marks=pytest.mark.smoke),
      "done"
  ])
  def start_state_fixture(request):
      return request.param
  ```
* Can add multiple marker by using mulitple @pytest.mark.marker1 \n @pytest.mark.marker1 etc...

### Using and , or , not and parentheses with Markers

* -m and - includes both
  * finish and exceptions
* -m and not - include one but not other
  * finish and not exception
* -m ( a or b) and ( not c) - include a or b but dont include c
  * (exception or smoke) and (not finish)
* -m smoke -k "not TestFinish" - run the smoke test not part of TestFinish
  * NOTE : -k accepts partial input

### Being Strict with Markers

* include flag --strict-markers will prevent unregisterd markers from running
* can also add this config permenantly in pytest.ini as
  ```
  addopts=
      --strict-markers
  ```
* This error is issued in collection time.. not run time. So it will get the feedback that something is wrong faster.

### Combining Markers with Fixtures

* To pass in dynamic arguents to fixtures we can use custom markers with arguments
* these dynamic arguments though markers can be fetched by fixtues using `request.node.get_closest_marker(marker-name)` from which we can get the arguments and loop though the data.

### Listing all Markers

* to list all markser available use `pytest --markers`

## Tips and tricks

Some flage to help tests

* -r flag tells pytest to report reasons for all reasons in session
* -f for failed tests
* -E errros
* -a for all except passed

We can parse version using packaging library. packageing.version.parse

dont missuse skip/skipif/xfail. always remember YAGNI (ya arent gonna need it). only build functions if nessesary

Faker is a third party library which can be used to generate fake data

Markers can have parameters which can be accessed with `.args` & `.kwargs` attributes
