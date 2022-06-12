# Considering Software architecture

If the software under test is designed as apython package with lotsof submodules, we can still test at the CLI level or we can zoom a bin into the modules. so during this we must consider the following

* At what level sould we be testing
* How to test and its dificulty ( usually ui is difficult )
* Who is responsible for the different levels and the tests

**Note** : Its better to isolate third-party packages. so if we need any change we many need to only change that file/module.

in project cards:

* as CLI is thin we can move almost all testing to API
* Testing cli can be achieved by seeing if api mapping is good
* As database layer is iso
