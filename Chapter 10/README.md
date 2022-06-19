# Chapter 10 - Mocking

We will be using unittest.mock python standard library for mocking. It is shipped as standard from python 3.3. It swaps pieces of system code with our code. Mock objects are sometimes called test doubles, spies, fakes, or stubs. 

## Tests

### Isolating the commandline interface

* Want to keep all the real logic off the cards api.
* In cli.py, the rest of the card system are accessed using cards import
* most of the db workes using a context manager that created cards.cardDB obj
