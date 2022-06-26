# Project Name
* DeletePermission - version 1.2.16

Project date: April 2022


## Additional infromation
- Icon from: https://icon-icons.com/icon/user-with-suit-tie-and-cancel-symbol/68274

- Deleting permission for one of system is time-consuming, because GUI isn't friendly. This project was for 1-st line, but they didn't want to used it :)
- I wrote this program after my job, because it is an element of my self-development.


## Table of Contents
* [General Info](#general-information)
* [Additional infromation](#additional-infromation)
* [General Information](#general-information)
* [Requirements](#requirements)
* [Technologies Used](#technologies-used)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
The program has:
- Connected to MSSQL
- Execute query
- Dump query results to file
- Logging activity
- Configuration inside program (cannot be edited after building exe)


## Requirements
- Install MSSQL ODBC on Windows


## Technologies Used
- Python - version 3.10.1
- PyODBC - version 4.0.32
- Logger - inner Python
- Pandas - version 1.4.2
- PyInstaller - version 5.1

<!--
## Features
None


## Screenshots
![Example screenshot](./img/screenshot.png)


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.
-->

## Usage

Generate EXE file - CMD ->
```batch
pip install pyinstaller --proxy http://user:pass@proxy.pl:3128
cd Building
pyinstaller DeletePermission.spec
```

1. Run DelPermission.exe
2. Look at the log file


## Project Status
Project is: _in DEV testing_

<!-- _complete_ / _no longer being worked on_ (and why) -->

<!--
## Room for Improvement
No plans
-->

## Contact
Created by [@Majster](mailto:rachuna.mikolaj@gmail.com)