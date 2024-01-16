import math

print('\n@classmethod task nr. 1')


class Math:
    @classmethod
    def factorial(cls, number):
        return math.factorial(number)


print(Math.factorial(4))


print('\n@classmethod task nr. 2')


class String:
    @classmethod
    def reverse_string(cls, string):
        reverse_string = [string[::-1]]
        return reverse_string


print(String.reverse_string('Labas'))

print('\n@classmethod task nr. 3')


class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def show_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        return BankAccount.total_accounts

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False


owner1 = BankAccount('Zyge', 50000.1)
owner2 = BankAccount('Marius', 20)

print(owner1.show_balance())
print(owner2.show_balance())

print(BankAccount.get_total_accounts())

print(BankAccount.validate_amount(20.1))
print(BankAccount.validate_amount(-50))

print('\n@classmethod task nr. 4')


class BankAccount:
    balance = 0
    def

    def deposit(self):
        deposit_amount = float(input('Insert amount: '))
        self.balance = deposit_amount
        return f'Your balance is: {self.balance}'

    def withdraw(self):
        withdraw_amount = float(input('Insert amount that you would like to withdraw: '))
        if withdraw_amount > self.balance:
            return 'Insufficient funds.'
        else:
            self.balance = self.balance - withdraw_amount
            return f'Your balance is: {self.balance}'

    @classmethod
    def from_balance(cls, starting_balance):
        cls.balance = starting_balance
        return cls.balance

    @staticmethod
    def transfer(amount):

acc1 = BankAccount(5000)
acc2 = BankAccount(300)
print(BankAccount.from_balance(20))