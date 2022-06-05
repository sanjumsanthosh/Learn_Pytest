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

## Tips and tricks

* -r flag tells pytest to report reasons for all reasons in session
* -f for failed tests
* -E errros
* -a for all except passed
