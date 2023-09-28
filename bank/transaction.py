from bank.account import SavingAccount

def deposit(account, amount):
    account.deposit(amount)
    print(f"Deposited Rs{amount} into {account.acc_no}")
    print(f"New Balance is Rs{account.blnc}")

def withdraw(account, amount):
    account.withdraw(amount)
    print(f"Withdrew Rs{amount} from {account.acc_no}")
    print(f"New Balance is Rs{account.blnc}")

def balance_enquiry(account):
    print(f"Acoount: {account.acc_no} Balance: Rs{account.blnc}")


