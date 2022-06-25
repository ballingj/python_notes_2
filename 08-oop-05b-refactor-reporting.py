##############################################
# Polymorphism 1 - first refactor the Reporting module to eliminate duplicate codes 
# We are using the inheritance toolbox to create Superclass and subclass
# OOP with Python - Loek van den Ouweland
####################################################

###########################################
# Main.py - no changes in this section
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
    Manager("Vera", "Schmidt", 2000),
    Attendant("Chuck", "Norris", 1800),
    Attendant("Samantha", "Carrington", 1800),
    Cook("Roberto", "Jacketti", 2100),
    Mechanic("Dave", "DreiBig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic("Ringo", "Rama", 1900),
    Mechanic("Chuck", "Rainey", 1800),
]

# finally separated the reporting function into its own module

accounting_report = AccountingReport(employees)
accounting_report.print_accounting_report()

print()  # empty line

staffing_report = StaffingReport(employees)
staffing_report.print_staffing_report()


#############################################################
# reporting.py
# we are refactoring report to create a Super Class Report
# and subclass AccountingReport and StaffingReport
# applying the principle of inheritance
###############################################################

class Report:
    def __init__(self, emp_list):
        self._emp_list = emp_list


class AccountingReport(Report):
    def print_accounting_report(self):
        print("Accounting")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.salary}")


class StaffingReport(Report):
    def print_staffing_report(self):
        print("Staffing")
        print("=========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.job_title}")


###########################################################################
# employee.py - no changes in this section
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
        # providing an underscore '_' before an attribute means do private attribute
        self._first_name = first_name
        # optical indicator only - does not prevent the code from changing them
        self._last_name = last_name
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
