##############################################
# Schedule Report - adding work schedule to produce
#  shift report (working schedule)
# OOP with Python - Loek van den Ouweland
####################################################

 
# main.py - add scheduled start and end time to employee
# OOP with Python - Loek van den Ouweland
###########################
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
import datetime


employees = [
    Manager("Vera", "Schmidt", 2000, datetime.time(8, 00), datetime.time(14, 00)),
    Attendant("Chuck", "Norris", 1800, datetime.time(8, 00), datetime.time(14, 00)),
    Attendant("Samantha", "Carrington", 1800, datetime.time(12, 00), datetime.time(20, 00)),
    Cook("Roberto", "Jacketti", 2100, datetime.time(8, 00), datetime.time(14, 00)),
    Mechanic("Dave", "DreiBig", 2200, datetime.time(8, 00), datetime.time(14, 00)),
    Mechanic("Tina", "River", 2300, datetime.time(8, 00), datetime.time(14, 00)),
    Mechanic("Ringo", "Rama", 1900, datetime.time(12, 00), datetime.time(20, 00)),
    Mechanic("Chuck", "Rainey", 1800, datetime.time(12, 00), datetime.time(20, 00)),
]

# Loop through the available reports

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees),
]

for r in reports:
    r.print_report()
    print()


############################################
# employee.py
# refactor Employee class to track work schedule
############################################


class Employee:
    def __init__(self, first_name, last_name, salary, start_time, end_time):
        # providing an underscore '_' before an attribute means do private attribute
        self._first_name = first_name
        # optical indicator only - does not prevent the code from changing them
        self._last_name = last_name
        self.salary = salary
        self.start_time = start_time
        self.end_time = end_time

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


#############################################################
# reporting.py
#  
###############################################################

class Report:
    def __init__(self, emp_list):
        self._emp_list = emp_list


class AccountingReport(Report):
    def print_report(self):
        print("Accounting")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.salary}")

class StaffingReport(Report):
    def print_report(self):
        print("Staffing")
        print("=========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.job_title}")

class ScheduleReport(Report):
    def print_report(self):
        print("Schedule")
        print("=========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.start_time:%H:%M} to {e.end_time:%H:%M}")
