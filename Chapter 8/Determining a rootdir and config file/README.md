# Determining a root directory and config file

### Below mentions the order in which the initilization goes in pytest

1. Before even starting the test, pytest want to read the config file
2. if we pass the test directory, it will look there. and if we pass muliple , it will go through the ansistory directories.
3. it will regess throught the tree until it finds the config file
   1. it sets this location as root dire
   2. this is also the relative root of test node ids
4. it would be a great idea to place an emtpy pytest.ini at top of the project. otherwise at best will cause slight delay or may even cause significant delay
5. Once it locates a config file, pytest will rpint out which rootdir and configuration files its using at the top of test run
