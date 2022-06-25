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
    