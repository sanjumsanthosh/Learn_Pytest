# Cards

* [ ]  `cards add message --owner owner_name` -> add a new card
* [ ]  `cards` -> display all cards
* [ ]  `cards update id --owner new_name` -> ability to update fields
* [ ]  `cards start id` -> start a card task
  * [ ]  status changes to in Progress
* [ ]  `cards finish id` -> finish a card
  * [ ]  status changes to done

## Development details

### pyproject.toml file

* used to install as a package

### Api.py

* controlles the api cals for the cli interface
* uses dataclass

### db.py

* class DB with initilization of db_path & db_file_prefix
