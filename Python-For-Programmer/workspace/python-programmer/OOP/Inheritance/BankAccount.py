class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def getBalance(self):
        return self.balance


class SavingBankAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interest(self):
        return self.balance * (self.interestRate / 100)


bankAc = SavingBankAccount("Tarini", 20000, 20)
bankAc.deposit(20000)
print("Bank interest of {}% on Saving amount {} is {} Rs".format(bankAc.interestRate, bankAc.balance, bankAc.interest()))
bankAc.withdrawal(10000)
print("Bank interest of {}% on Saving amount {} is {} Rs".format(bankAc.interestRate, bankAc.balance, bankAc.interest()))
print("Bank balance :{}", bankAc.getBalance())