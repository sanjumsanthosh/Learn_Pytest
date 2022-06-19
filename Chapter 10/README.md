# Chapter 10 - Mocking

We will be using unittest.mock python standard library for mocking. It is shipped as standard from python 3.3. It swaps pieces of system code with our code. Mock objects are sometimes called test doubles, spies, fakes, or stubs. 

## Tests

### Isolating the commandline interface

* Want to keep all the real logic off the cards api.
* In cli.py, the rest of the card system are accessed using cards import
* most of the db workes using a context manager that created cards.cardDB obj

### Testing with typer

* Typer provides a testing intreface. with it , we can call our aplication without using subprocess.run
* Create a helper function called cards_cli for generating result for the cli

### Mocking an Attribute

* There are several **patch** methods within the mock package. here we will be using mock.patch.object
* mock.patch.object() uses a context manager within a **with** block returns a mock obj that is cleaned up after the **with** block
* with mock objects, we can set attribute values, return values for callable , and event look at how callables are called.
