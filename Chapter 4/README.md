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

## Tips & tricks
