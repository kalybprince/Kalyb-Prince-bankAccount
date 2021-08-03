class BankAccount:
    all_accounts = []

    def __init__(self, int_rate=1.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append([self.int_rate, self.balance])

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        return f"Balance: {self.balance}"
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self
        else:
            print("Insufficient funds: Cannot yield interest.")
    
    @classmethod
    def display_all_accounts(cls):
        for i in cls.all_accounts:
            print(i)

account_1 = BankAccount()
account_2 = BankAccount()

print(account_1.deposit(50).deposit(50).deposit(50).withdraw(25).display_account_info())

print(account_2.deposit(50).deposit(50).withdraw(25).yield_interest().display_account_info())

print(BankAccount.all_accounts)