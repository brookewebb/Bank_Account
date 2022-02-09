class BankAccount: 
    
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
    

Account1 = BankAccount(.05, 232)
Account2 = BankAccount(.13, 856)

Account1.deposit(15).deposit(83).deposit(59).withdraw(158).yield_interest().display_account_info()
Account2.deposit(1000).deposit(681).withdraw(321).withdraw(174).withdraw(533).withdraw(12).yield_interest().display_account_info()