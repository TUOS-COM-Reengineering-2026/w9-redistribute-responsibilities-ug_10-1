from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff

# Account: data container for an account
# Branch: data container for a branch
# Customer: data container for a customer
# Payroll: a payroll
# PaySchedule: used internally in Payroll
# Staff: staff "don't edit this class"

# Aim: determine which of the Bank methods belong in the data classes
# (Account, Branch, or Customer).

# Branch refactoring: moved setup_branch, close_branch, and transfer_staff_member to Branch
# Moved opening time value for Branch into the class itself.

class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.customer_addresses = {}  # key: customer, value: address
        self.customer_phone_numbers = {}  # key: customer, value: phone number
        self.branches = []
        # moved to Branch: self.branch_opening_times = {}  # key: branch, value: opening time
        self.payroll = None

    # Altered by moving opening time to the Branch class
    def setup_branch(self, branch: Branch):
        branch.set_opening_time("9:00")
        self.branches.append(branch)

    # Calls the delegated method and removes from the list:
    def close_branch(self, branch: Branch, transfer_branch: Branch): # Branch
        branch.close_branch(transfer_branch)
        self.branches.remove(branch)

    # Removed as can just use set_opening_time instead on the branch.
    # Otherwise, it doesnt make logical sense to be in the Bank class; would be a static method.
    #def change_branch_opening_time(self, branch: Branch, time: str): # Branch
    #    self.branch_opening_times[branch] = time

    # Everything above has been refactored, rest will do later:

    def setup_new_account(self, account: Account, customer: Customer): # Account or Customer? maybe dont move.
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)
            self.customer_addresses[customer] = "NO ADDRESS"  # default address
            self.customer_phone_numbers[customer] = "NO PHONE NUMBER"  # default phone number

    def obtain_balance(self, account: Account):# Account
        return account.get_balance()

    def add_interest(self, account: Account): # Account
        balance = account.get_balance()
        interest_rate = account.get_interest_rate()
        interest = balance * interest_rate
        account.set_balance(balance + interest)

    def add_funds(self, account: Account, amount: float): # Account
        balance = account.get_balance()
        account.set_balance(balance + amount)

    def close_account(self, account: Account): # Account
        account.set_customer(None)
        account.set_balance(0)
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff): # Branch
        branch.get_staff().append(staff)


    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str): # maybe Payroll?
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category).set_pay_date(date)
