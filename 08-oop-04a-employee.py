# Refactor - employee.py
# OOP with Python - Loek van den Ouweland
###########################

""" When code grows, code changes.  Evaluating this code reveals that this 
codes must pe separated into three separate sections. 
"""

# This is the first section where we extracted the Employee class and it's derivatives
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

