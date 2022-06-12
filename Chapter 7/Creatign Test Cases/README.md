# Creatign Test Cases

Start with a non-trivial, "happy path" test case, and look for

* interesting set of inputs
* intresting starting states
* interesting end states
* all possible error states

last chapter we evaluated all possibel core and risk test cases. so will create test cases for each

## Core

### Add

happy path is to add a card to a non-empty db. and based on the design the summary is required and owner is optional.

* add to non empty with summary
* add to an empty with summary
* add a card with summary & owner
* add with a missing summary
* add a duplicate card

### Count

happy will be have a list get the count back so

* count on empty = 0
* count on non-empty = count
  * one item
  * more than one item

### Delete

* remove a card from non empty
  * remove last card
* remove a card from empty
* remove a non existant card

Note : the last 2 points can be combined

### Finish

Happy path is to finish from in prog state

* finish from todo, in prog, done state
* finish with invalid id

### List

* list from a non empty
  * list one
  * list more than one
* list from empty

### Start

* start from todo, in prog, done state
* start with invalid id

### Update

* update details of an existing card
  * update card and id together
  * update card owner only
  * update summary only
* update with invalid id

### Config

* returns the correct db

### Version

* return correct version
