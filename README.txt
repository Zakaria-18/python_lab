PYTHON LAB PROJECT
==================

Project Name: python_lab
GitHub Repository: python-lab

DESCRIPTION
-----------
This project demonstrates Python project setup, basic Python programming, Git version control, and GitHub branch and pull request workflows.

PROJECT STRUCTURE
-----------------
python_lab/
|-- src/
|   |-- main.py
|   |-- utils.py
|   |-- config.py
|-- tests/
|-- docs/
|   |-- README.md
|-- .gitignore
|-- README.txt

FEATURES
--------
1. Calculates the square of a number.
2. Checks whether a number is even or odd.
3. Converts Celsius temperatures to Fahrenheit.
4. Displays a personalized greeting using the user's name.

PYTHON FUNCTIONS
----------------
square(n)
    Returns the square of a number.

is_even(n)
    Returns True if a number is even and False otherwise.

celsius_to_fahrenheit(c)
    Converts Celsius to Fahrenheit using:
    F = (C * 9/5) + 32

greet(name)
    Returns a personalized greeting for the specified name.

REQUIREMENTS
------------
- Python 3
- Git
- A GitHub account for remote repository hosting

HOW TO RUN
----------
1. Open a terminal in the project directory.
2. Navigate to the source directory:

   cd src

3. Run the program:

   python main.py

4. Enter your name and a number when prompted.

GIT WORKFLOW
------------
The project uses Git for version control.

Main branch:
    Contains the initial project and numeric utility program.

Feature branch:
    feature/add-greeting

The feature branch adds the personalized greeting function.
Changes are pushed to GitHub and submitted for review through a
pull request into the main branch.

GITIGNORE
---------
The .gitignore file excludes:
- __pycache__/ directories
- Compiled Python .pyc files
- .env files

TESTING
-------
The program should be tested with at least three different numeric
inputs, including even and odd values and zero.

AUTHOR
------
Student Python Lab Assignment

LICENSE
-------
Created for educational purposes.
