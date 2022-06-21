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


# now we have to add first and last name data to distinguish two people with same name
employees = [
    Manager("Vera", "Scmidt", 2000),
    Attendant("Chuck", "Norris", 1800),
    Attendant("Samantha", "Carrington", 1800),
    Cook("Roberto", "Jacketti", 1800),
    Mechanic("Dave", "DreiBig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic("Ringo", "Rama", 1900),
    Mechanic("Chuck", "Rainey", 1800),
]

# third section - we are refactoring again to change to first and last name

def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.get_full_name()}, {e.salary}")


def print_staffing_report():
    print("Staffing")
    print("=========")
    for e in employees:
        print(f"{e.get_full_name()}, {e.job_title}")


print_accounting_report()
print()  # empty line
print_staffing_report()
