from PaySchedule import PaySchedule


class Payroll:
    def __init__(self):
        self.staff_category_pay_schedules = {"Manager": PaySchedule("1st")}

    def get_staff_category_pay_schedule(self, staff_category):
        return self.staff_category_pay_schedules[staff_category]

    def get_staff_category_pay_day(self, staff_category):
        return self.staff_category_pay_schedules[staff_category].get_pay_date()

    def change_payroll_date(self, date: str, staff_category: str): # maybe Payroll?
        self.get_staff_category_pay_schedule(staff_category).set_pay_date(date)
