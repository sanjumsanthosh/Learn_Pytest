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

### Testing an importable python script

we can make the scripts importable and move it inside a function. like with a main function and using `__name__ == __main__` to check it

in this case we could use capsys to capture output

### Separating code into src & tests directories

* if we move everying into seperate directories like src and test it wont work as it will give a no module named "hello" error
* i.e. it doesnot know to look in src for hello.
* generally it uses the sys.path to track which all places to look for so we could add it in pythonpath (v>7) else pytest-srcpaths (v 6.2.x)
