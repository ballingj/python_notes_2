# Refactor - employee.py
# OOP with Python - Loek van den Ouweland
###########################


""" Encapsulation involves creating a method in class that manipulates the data.  That data should not be manipulated 
outside of class, so we create a method to manipulate them.  For example, if we want to reverse printing last name, first name 
instead of first name last name, we can add a method to do that function.  
In python, we indicate the attribute that we don't want changed outside of class with an underscore '_'
as in _first_name; _last_name.   Unfortunately python does not prevent changing of attributes outside of class--indicator only.
"""

# Now we are refactoring the Employee class to change name to first and last name
class Employee:
    def __init__(self, first_name, last_name, salary):
        self._first_name = first_name   # providing an underscore '_' before an attribute means do private attribute
        self._last_name = last_name     # optical indicator only - does not prevent the code from changing them
        self.salary = salary

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

class Mechanic(Employee):
    job_title = "Mechanic"


class Attendant(Employee):
    job_title = "Station Attendant"


class Cook(Employee):
    job_title = "Cook"


class Manager(Employee):
    job_title = "Manager"

