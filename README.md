# iReporter2

[![Build Status](https://travis-ci.com/HabibSentongo/iReporter2.svg?branch=feature)](https://travis-ci.com/HabibSentongo/iReporter2)        [![Coverage Status](https://coveralls.io/repos/github/HabibSentongo/iReporter2/badge.svg?branch=feature)](https://coveralls.io/github/HabibSentongo/iReporter2?branch=feature)      [![Maintainability](https://api.codeclimate.com/v1/badges/e58dcbe4f07898eb7ce0/maintainability)](https://codeclimate.com/github/HabibSentongo/iReporter2/maintainability)

## Project Overview
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter.
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

# iReporter API Endpoints
This project is about a set of API endpoints for the iReporter app to create, manage and store users and incidents in memory using Data Structures.
## The Features Include:
* Sign-up a user.
* Login a user.
* Create an incident (red-flag / intervention).
* Get an incident by id.
* Get all incidents.
* Update an incident's location by id.
* Update an incident's status by id.
* Delete an incident by id.
* Get all users.
* Update a user's role by id.

## Table of Contents
- [Project Description](#iReporter2)
- [Project Planning](#project-planning)
- [Language and Tools used](#language-and-tools-used)
- [Installing](#installing)
- [Running the application](#running-the-application)
- [Unit Testing the app](#unit-testing-the-application)
- [Available Version](#url-versioning)
- [Deployed Version](#deployed-version)

## Project Planning
PivotalTracker was used for project Planning and Management. You can find this project's PivotalTracker Board [here](https://www.pivotaltracker.com/n/projects/2232420 "iReporter2 on PivotalTracker")

## Language and Tools Used
### Tools used include:
* [Python 3.7](https://www.python.org)
* [Flask](http://flask.pocoo.org/)
* [Pip - A python package installer](https://pypi.org/project/pip/)
* [Virtualenv](https://pypi.org/project/virtualenv/)
* [Git](https://git-scm.com/downloads)
* [VSCode (IDE)](https://code.visualstudio.com/)
* [Open API](https://www.openapis.org/)
* [Swagger](https://swagger.io/)
* [Postman](https://www.getpostman.com/)
* [PivotalTracker](https://www.pivotaltracker.com "PivotalTracker")

## Installing

##### Cloning and Configuring the Project to Your Local Machine

- Step 1: Open the Terminal (or git bash, for windows) on the Directory/Folder where you want to place the project.
- Step 2: Then run this command 

    `git clone https://github.com/HabibSentongo/iReporter2.git`

    This copies the entire project onto your local machine. Confirm that the project name is “iReporter2”
- Navigate to the root folder of the project using the command below.

    `cd iReporter2`

- Step 4: Change to the "develop" branch using the command below.

    `git checkout develop`

##### Setting Up the Virtual Environment
Inorder to set up the virtual environment, you need to install the python package called virtualenv using pip. Run the command below to install it.
- `pip install virtualenv` to install virtualenv
- `virtualenv venv`  to create a virtual environment named venv
- `. venv/scripts/activate` to activate the virtual environment.
- `. venv/scripts/deactivate` to deactivate the virtual environment when you need to.

### Installing Requirements
You need to install all the packages required by the project in the activated virtual environment. All these requirements are listed and stored in the requirements.txt file in the root folder of the project.
While in this folder, run the command below to install these requirements.
- `pip install -r requirements.txt`

With success of all the above steps, you have successfully cloned and configured the project to run on your local machine.

## Running the Application
To run this application, while in the root folder of the project via the Terminal or command prompt, run the command below:
- `py main.py`

On running that command, the application server will be launched and the URL to that server will be shown to you in the command-line/terminal.

## Unit Testing the Application

* Pytest has been used to test these API endpoints. To run unit tests for this application, you must install pytest, pytest-cov and coverage on your pc or in your virtual environment.
* While in the root directory of the project, run the command below to run the unit tests and also generate a coverage report.
- `pytest --cov`

## URL Versioning

The endpoints of this application have been versioned. The current version is one (1); i.e.: `api/v1`

## Deployed Version
### Heroku
Find the deployed API [here](https://ireporter-api-deploy.herokuapp.com/ "iReporter2 on Heroku")