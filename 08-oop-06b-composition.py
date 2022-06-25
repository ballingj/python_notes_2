##############################################
# Schedule Report - adding work schedule to produce
#  shift report (working schedule)
# OOP with Python - Loek van den Ouweland
####################################################

 
# main.py - add scheduled start and end time to employee
# OOP with Python - Loek van den Ouweland
###########################

import datetime
from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport
from reporting import ScheduleReport
from shift import MorningShift
from shift import AfternoonShift
from shift import NightShift

employees = [
    Manager("Vera", "Schmidt", 2000, MorningShift()),
    Attendant("Chuck", "Norris", 1800, MorningShift()),
    Attendant("Samantha", "Carrington", 1800, AfternoonShift()),
    Cook("Roberto", "Jacketti", 2100, MorningShift()),
    Mechanic("Dave", "DreiBig", 2200, MorningShift()),
    Mechanic("Tina", "River", 2300, MorningShift()),
    Mechanic("Ringo", "Rama", 1900, AfternoonShift()),
    Mechanic("Chuck", "Rainey", 1800, NightShift()),
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
# employee.py - composition
# tieing the shift class 
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
# Add the new ScheduleReport class inherited from Report
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

# replaced start and end time with shift.get.shift_info() object
class ScheduleReport(Report):
    def print_report(self):
        print("Schedule")
        print("=========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.shift.get_shift_info()}")

##################################################
# shift.py
# this is tied to the Employee object - each employee is assigned a shift
##################################################
# import datetime    # needed in independent file

class Shift:
    def get_shift_info(self):
        return f"{self.start_time:%H:%M} to {self.end_time:%H:%M}"

class MorningShift(Shift):
    start_time = datetime.time(8, 00)
    end_time = datetime.time(14, 00)

class AfternoonShift(Shift):
    start_time = datetime.time(12, 00)
    end_time = datetime.time(20, 00)


class NightShift(Shift):
    start_time = datetime.time(14, 00)
    end_time = datetime.time(22, 00)
