# Refactor - main.py
# OOP with Python - Loek van den Ouweland
###########################

""" When code grows, code changes.  Evaluating this code reveals that this 
codes must pe separated into three separate sections. 
"""
# after moving the classes, we have to import them here before we can use them

from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic


# this is the second section where we removed classes - this creates and display the data
employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 2100),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900),
]

# third section - displays the data
for e in employees:
    print(f"{e.name}, {e.salary}, {e.job_title}")
