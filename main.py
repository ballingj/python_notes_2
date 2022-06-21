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
from reporting import AccountingReport
from reporting import StaffingReport

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

# Loop through the available reports

reports = [
    AccountingReport(employees),
    StaffingReport(employees)
]

for r in reports:
    r.print_report()
    print()
