# Testing scripts & Applications

This includes scripts which cannot be installed with pip like cards. Some common definitions are provided for intro

* Script : single file intended to run direclty from python
* Importable scripts : no code executed when imported. Runs only when used directly
* Application: package / script that have external dependenies defined in requiremnt files/project files.

## Tests

### Testing a simple python script

To test a script we need some ways to run the file. Some options are

* using subprocess.run
  * run(["python","hello.py"], capture_output=True, text=True)
* using the same with tox it wont work
  * why? tox is trying to build something as first part so we need to tell it to not build anything
  * how to solve it? ass `skipsdist = true`

To test larger scripts we need to split it into seperate test codes and into seperate directories.
