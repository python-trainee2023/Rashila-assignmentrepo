class Account:
    def __init__(self, account_no, holder_name, balance):
        self.acc_no= account_no
        self.acc_name= holder_name
        self.blnc=balance

    def deposit(self, amount):
        self.blnc += amount
    def withdraw(self, amount):
        if amount <= self.blnc:
            self.blnc -= amount
        else:
            print("insufficient balance")


class SavingAccount(Account):
    def __init__(self, account_no, holder_name, balance, interest_rate):
        super().__init__(account_no, holder_name, balance)
        self.intrs_rate = interest_rate

    def calc_interest(self):
        return self.blnc * (self.intrs_rate/100)

class CheckAccount(Account):
    def __init__(self, account_no, holder_name, balance, limit):
        super().__init__(account_no, holder_name, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount <= self.blnc + self.limit:
            self.blnc -= amount
        else:
            print("Transaction exceed limit")
