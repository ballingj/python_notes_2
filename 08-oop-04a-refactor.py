# Refactor
# OOP with Python - Loek van den Ouweland
###########################

""" When code grows, code changes.  Evaluating this code reveals that this 
codes must pe separated into three separate sections. 
"""


# first section is classes - create a new file called employee.py
# if you don't know how to split your code, separating the classes is a good first step
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Mechanic(Employee):
    job_title = "Mechanic"


class Attendant(Employee):
    job_title = "Station Attendant"


class Cook(Employee):
    job_title = "Cook"


class Manager(Employee):
    job_title = "Manager"

# second section - creates the data - create a new file called main.py
employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 1800),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900),
]

# third section - displays the data - add this in main.py
for e in employees:
    print(f"{e.name}, {e.salary}, {e.job_title}")
