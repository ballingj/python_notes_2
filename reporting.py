#############################################################
# reporting.py
# After refactoring report to create a Super class
# and subclass...polymorphism allows us for each subclass to have the same
# method name.   change print_accounting_report to print_report
# do the same for StaffingReport
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
