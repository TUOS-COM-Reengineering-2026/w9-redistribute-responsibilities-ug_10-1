class Account:

    def __init__(self):
        self.customer = None
        self.balance = 0
        self.interest_rate = 0.05

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, rate):
        self.interest_rate = rate

    def add_interest(self): # Account
        balance = self.get_balance()
        interest_rate = self.get_interest_rate()
        interest = balance * interest_rate
        self.set_balance(balance + interest)

    def add_funds(self, amount: float): # Account
        balance = self.get_balance()
        self.set_balance(balance + amount)

    def close_account(self): # Account
        self.set_customer(None)
        self.set_balance(0)