#4-masala
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

b1 = BankAccount("Ali", 1000)

print(b1.balance)

b1.balance = 2500
print(b1.balance)
