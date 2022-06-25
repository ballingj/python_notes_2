############################################
# employee.py - composition
# 
############################################


class Employee:
    def __init__(self, first_name, last_name, salary, shift):
        # providing an underscore '_' before an attribute means do private attribute
        # optical indicator only - does not prevent the code from changing them
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        self.shift = shift

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def raise_salary(self, amount):
        self.salary = self.salary + amount


class Mechanic(Employee):
    job_title = "Mechanic"


class Attendant(Employee):
    job_title = "Station Attendant"


class Cook(Employee):
    job_title = "Cook"


class Manager(Employee):
    job_title = "Manager"
