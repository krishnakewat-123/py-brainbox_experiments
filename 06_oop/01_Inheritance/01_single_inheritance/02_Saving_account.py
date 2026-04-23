'''######### output ##############
Balance: ₹1000
Deposited ₹500
Withdrawn ₹300
Balance: ₹1200
##############################'''
class Account:
    def __init__(self, holder, balance):
        self.holder = holder      # stores account holder name
        self.balance = balance    # stores initial balance

    def show_balance(self):
        print(f"Balance: ₹{self.balance}")   # displays current balance


class SavingsAccount(Account):   # child class inheriting from Account
    def deposit(self, amount):
        self.balance += amount   # adds amount to balance
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:   # check if sufficient balance
            self.balance -= amount   # deduct amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")   # error message


# creating object of child class
acc = SavingsAccount("Krishna", 1000)

acc.show_balance()     # parent method
acc.deposit(500)       # child method (add money)
acc.withdraw(300)      # child method (withdraw money)
acc.show_balance()     # check updated balance