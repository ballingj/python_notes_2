# Inheritance
# OOP with Python - Loek van den Ouweland
###########################

""" When a job title change, each line of code will have to be updated: Attendant is now 'Station Attendant' and 'Car Repair to "Mechanic'
This is where inheritance is useful.
"""

# class Employee:
#     def __init__(self, name, salary, job_title):
#         self.name = name
#         self.salary = salary
#         self.job_title = job_title


# employees = [
#     Employee("Vera", 2000, "Manager"),
#     Employee("Chuck", 1800, "Station Attendant"),
#     Employee("Samantha", 1800, "Station Attendant"),
#     Employee("Roberto", 1800, "Cook"),
#     Employee("Dave", 2200, "Mechanic"),
#     Employee("Tina", 2300, "Mechanic"),
#     Employee("Ringo", 1900, "Mechanic"),
# ]

# for e in employees:
#     print(f"{e.name}, {e.salary}, , {e.job_title}")


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

employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 1800),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300),
    Mechanic("Ringo", 1900),
]

for e in employees:
    print(f"{e.name}, {e.salary}, {e.job_title}")
