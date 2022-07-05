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