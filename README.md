# RP To-do application

Command line application to create a to-do's list. This application is created following [Real python's tutorial](https://realpython.com/python-typer-cli/)

## Start the project

Once you've downloaded the project in order to configure the project properly, you need to do the following steps:

1) Create virtual enviroment folder in your root project's folder: `python -m venv venv`
2) [Install required dependencies](#install-required-dependencies)

## Run tests

To run test execute the following command: `python -m pytest tests/`

## Install required dependencies

In order to install required dependencies from `requirements.txt` file. Run the following command `python -m pip install -r requirements.txt`


## Commands

### Init

Creates database file : `python -m rptodo init`. You can use the default location path or provide new one using --db-path or -db options, note that using this option you need to provide filename too.

###  Add

Adds new todo to the database. Valid commands samples:

`python -m rptodo add Get some milk -p 1`

`python -m rptodo add Clean the house --priority 3`

`python -m rptodo add Wash the car`. Add task with priority 2


### List

List all to-do tasks stored in current database.

`python -m rptodo list`


### Remove

Remove a to-do task by id.

`python -m rptodo remove <id_todo>` -> Requires user confirmation

`python -m rptodo remove --force <id_todo>` -> Doesn't require user confirmation

`python -m rptodo remove -f <id_todo>` -> Doesn't require user confirmation


## Clear

Remove all to-dos from database

`python -m rptodo clear`

`python -m rptodo clear --force`