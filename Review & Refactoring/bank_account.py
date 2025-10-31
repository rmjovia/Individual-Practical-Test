# Question 1a: BankAccount Class


class BankAccount:
    def __init__(self, initial_balance=0):
        # The underscore (_) before balance indicates it's a private attribute
        self._balance = initial_balance

    def deposit(self, amount):
        
        # Only positive amounts can be deposited
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        
        # Withdrawal only happens if the balance is sufficient
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        # Method to return the current balance
        return self._balance



# Testing the BankAccount class


# Create two separate bank account objects
acc1 = BankAccount()        # Starts with default balance = 0
acc2 = BankAccount(100)     # Starts with initial balance = 100

# Perform transactions on the first account
acc1.deposit(5000)         
acc1.withdraw(200)          
print("Account 1 Balance:", acc1.get_balance())  # Display current balance

# Perform transactions on the second account
acc2.deposit(500)           
acc2.withdraw(180)         
print("Account 2 Balance:", acc2.get_balance())  # Display current balance
