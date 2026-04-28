from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.customer_addresses = {}  # key: customer, value: address
        self.customer_phone_numbers = {}  # key: customer, value: phone number
        self.branches = []
        self.branch_opening_times = {}  # key: branch, value: opening time
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)
        self.branch_opening_times[branch] = "9:00"  # default opening time

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.remove_staff_member(staff)
        to_branch.add_staff_member(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)
            self.customer_addresses[customer] = "NO ADDRESS"  # default address
            self.customer_phone_numbers[customer] = "NO PHONE NUMBER"  # default phone number

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        account.apply_interest()

    def add_funds(self, account: Account, amount: float):
        balance = account.get_balance()
        account.set_balance(balance + amount)

    def close_account(self, account: Account):
        account.set_customer(None)
        account.set_balance(0)
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.add_staff_member(staff)

    def change_opening_time(self, branch: Branch, time: str):
        self.branch_opening_times[branch] = time

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category, date)
    