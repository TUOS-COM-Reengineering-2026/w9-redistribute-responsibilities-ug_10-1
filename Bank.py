from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.customers = []
        self.branches = []
        self.payroll = None

    def setup_branch(self, branch):
        self.branches.append(branch)

    def remove_branch(self, branch):
        self.branches.remove(branch)

    def get_branch(self, branch):
        return branch if branch in self.branches else Branch()

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, account):
        self.customers.remove(account)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.remove_branch(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.remove_staff(staff)
        to_branch.add_staff_member(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        customer.add_account(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def close_account(self, customer: Customer, account: Account):
        customer.remove_account(account)

        if customer.accounts:
            self.remove_customer(customer) 

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category).set_pay_date(date)
