from Account import Account

class Customer:
    def __init__(self, name: str):
        self._name = name
        self.customer_address = "NO ADDRESS"  # key: customer, value: address
        self.customer_phone_number = "NO PHONE NUMBER"  # key: customer, value: phone number
        self.accounts = []

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name
    
    def get_accounts(self):
        return self.accounts
    
    def set_accounts(self, accounts):
        self.accounts = accounts

    def get_address(self):
        return self.customer_address
    
    def set_address(self, address):
        self.customer_address = address

    def get_phone_number(self):
        return self.customer_phone_number
    
    def set_phone_number(self, phone_number):
        self.customer_phone_number = phone_number

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account: Account):
        account.close_account()
        self.accounts.remove(account)

