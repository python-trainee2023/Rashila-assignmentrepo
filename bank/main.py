from bank.account import SavingAccount, CheckAccount
from bank.transaction import deposit, withdraw, balance_enquiry

saving_account = SavingAccount("12345", "Ram", 1000, 2.5)
check_account = CheckAccount("54321", "Shyam", 2000, 100)

deposit(saving_account, 500)
withdraw(saving_account, 200)
balance_enquiry(saving_account)
balance_enquiry(check_account)