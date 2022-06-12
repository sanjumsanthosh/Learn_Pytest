# Evalutaign the features to Test

When we have a lot of functionality and features to test, you have to prioritize the order of developing tests. Like below

* Recent - new features or code/ recently modified
* Core - core funcitonalities of the project
* Risk - Areas with risk for like 3p libraries
* Problematic - Functionality that frequently breaks
* Expertis - Feaures / algo understood by some subset of people

In card case

* Core
  * add
  * count
  * delete
  * finish
  * list
  * start
  * update
  * config ( less imp )
  * version (less imp)
* Risk
  * Typer
  * tinydb
