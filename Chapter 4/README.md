# Chapter 4 - Builtin Fixtures

## Introduction

In the previous chapter we learnt about fixtures and how to use them. This chapter deals with a list of inbuilt fixtures which we can use. like for example

* handle temporary directory & files
* access command-line options
* comunicate between test sessins
* validate output streams
* modify environment variables
* interrogate warnings

## Tests

### Using tmp_path & tmp_path_factory

#### 1. tmp_path

* It has a function scope and return a pathlib.Path object with the temp path
* will be available some time even after a fail

### 2. tmp_path_factory

* it has a session scope and uses mktemp() function to create temp file. can make mulitple temporary file with mktemp
* mktemp return a pathlib.Path object with temp path
* it will also be available after some time event after completing the session

### Using capsys

* read error and output from command line. outputs two named tupes out & error.
* can also temporarly disable normal output capture without using -s or --capture=no flag.
  * for this functionality use with `capsys.disabled()...`
* related builtin functions
  * capfd - like capsys but captures file descriptors 1& 2
  * capsysbinary - captures binary
  * capfdbinary - captures file descriptors binary
  * caplog - captures output written with the logger package

### MonkeyPath

monkey patch can be used to dynamically modify test classes during runtime. It can be used to take over part of the runtime environment of the application ocde and replace eithe rinput dependencies or output dependencies wit  objeceets or variables, python search path or current direcotry. its like a mini version of mockeing. Some of the function are:

* setattr/delattr - sets/deletes an attribute
* setitem/delitem - sets/deletes a dictionary entry
* setenv/delenv - sets/deletes an environment variable
* syspath_prepend - prepends path to sys.path
* chdir - changes the current working directory

Arguments (target, name, value, raising=True)

* raising parameter tells whether or not to raise an exception if the item doesn't already exist
* setenv has prepend argument is used to set value of env as value + prepend + old-value


## Tips & tricks

* its a good idea to make the code easy for testing ... like in this case there is an env variable to pass the directory through which makes our life much more simple.
