
class Account:

    def __init__(self, id):
        self.id = id
        self.balance = 0 
        self.history = [0]




    def deposit(self, value1):
        self.balance = self.balance + value1
        self.history.append(self.balance)

    def withdraw(self, value2):
        if value2 <= self.balance:
            self.balance = (self.balance - value2)
            self.history.append(self.balance)
            return value2
        if   value2 > self.balance:
            self.history.append(self.balance)
            return 0 




if __name__ == "__main__":
    account = Account(123456789)
    print(f'In Account {account.id} has {account.balance} shakel')


    account.deposit(5234)
    print(f'In Account {account.id} has {account.balance} shakel')

    account.deposit(500)
    print(f'In Account {account.id} has {account.balance} shakel')

    account.withdraw(2000)
    print(f'In Account {account.id} has {account.balance} shakel')

    account.withdraw(2000)
    print(f'In Account {account.id} has {account.balance} shakel')


