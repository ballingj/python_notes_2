# Refactor - employee.py
# OOP with Python - Loek van den Ouweland
###########################

""" When code grows, code changes.  Evaluating this code reveals that this 
codes must pe separated into three separate sections. 
"""


# Now we are refactoring the Employee class to change name to first and last name
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


class Mechanic(Employee):
    job_title = "Mechanic"


class Attendant(Employee):
    job_title = "Station Attendant"


class Cook(Employee):
    job_title = "Cook"


class Manager(Employee):
    job_title = "Manager"

