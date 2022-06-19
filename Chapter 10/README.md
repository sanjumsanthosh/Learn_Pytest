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

### Mocking a class & methods

* cards_db() is a context manager which returs a cards.cardsDB obj. and on the returning obj path is called.
* as card_db is always needed we can create a fixture

### Keeping Mock & Implementation in sync with autospec

* By default a mock can accept any arguments so its very flexible by default
* Mock drift can occure when you are mocking changes and test doesnot.
* Mock drift can be cured using autospec