class Account:
    # Constructor
    def __init__(self, acno, customer, balance=0):
        # Object Attributes
        self.acno = acno
        self.customer = customer
        self.__balance = balance  # private

    # Methods
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount >= 100:
            self.__balance -= amount
        else:
            print("Invalid transaction amount")

    def getbalance(self):
        return self.__balance


a1 = Account(1, "Scott")
a1.deposit(10000)
print(a1.__dict__)
#print(a1.__balance)
print(a1.getbalance())

a2 = Account(2, "Tom", 20000)
a2.deposit(5000)
