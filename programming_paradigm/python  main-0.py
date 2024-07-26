from bank_account import BankAccount
account = BankAccount()

account.deposit(10000)
account.display_balance()

account.withdraw(50)
account.display_balance()

account.withdraw(70)  
account.display_balance()  

account.deposit(20) 
account.display_balance()