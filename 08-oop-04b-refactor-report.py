# Refactoring - main.py to add a 2nd report
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


# this is the second section - this creates the data
employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 1800),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900),
]

# third section - we are refactoring to create two types of reports

def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.name}, {e.salary}")

def print_staffing_report():
    print("Staffing")
    print("==========")
    for e in employees:
        print(f"{e.name}, {e.job_title}")

print_accounting_report()
print() #empty line
print_staffing_report()
