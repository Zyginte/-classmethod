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

    def __init__(self, name, acc_balance):
        self.name = name
        self.acc_balance = acc_balance
        self.account = self.name, self.acc_balance

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
        acc1.acc_balance = acc1.acc_balance - amount
        acc2.acc_balance = acc2.acc_balance + amount
        return f'acc1 balance: {acc1.acc_balance}\nacc2 balance: {acc2.acc_balance}'


acc1 = BankAccount('Paulina', 5000)
acc2 = BankAccount('Orinta', 13000)

print(BankAccount.from_balance(20))
print(BankAccount.transfer(20))
print(acc1.account)


print('\n@classmethod task nr. 5')


class SpaceStation:
    astronauts = []
    def __init__(self, name, nationality, mission_duration):
        self.name = name
        self.nationality = nationality
        self.mission_duration = mission_duration

    def add_astronaut(self):
        dictionary = {'name': self.name, 'nationality': self.nationality, 'mission_duration': self.mission_duration}
        self.astronauts.append(dictionary)
        return self.astronauts

    def find_astronaut(self, name):
        for dictionary in self.astronauts:
            if name in dictionary['name']:
                return dictionary
            else:
                return None

    @classmethod
    def from_astronaut_list(cls):
        return cls.astronauts


Joseph = SpaceStation('Joseph M. Acaba', 'USA', 12)
Vladimir = SpaceStation('Vladimir Aksyonov', 'China', 7)

print(Joseph.add_astronaut())
print(Vladimir.add_astronaut())
print(Vladimir.find_astronaut('Aksyonov'))
print(SpaceStation.from_astronaut_list())
