class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            print("Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        """Deduct the amount from the account balance if funds are sufficient."""
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current balance: {self.account_balance}")