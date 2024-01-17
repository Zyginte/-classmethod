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
    def __init__(self):
        self.astronauts = []

    def add_astronaut(self, name, nationality, missio_duration):
        dictionary = {'name': name, 'nationality': nationality, 'mission_duration': missio_duration }
        self.astronauts.append(dictionary)
        return self.astronauts

    def find_astronaut(self, name):
        for dictionary in self.astronauts:
            if name in dictionary['name']:
                return dictionary
            else:
                return None

    @classmethod
    def from_astronaut_list(cls, astronaut_list):
        return astronaut_list

    @staticmethod
    def is_long_term_mission(astronaut_dictionary):
        if astronaut_dictionary['mission_duration'] < 180:
            return False
        else:
            return True

    def remove_astronaut(self, name):
        for dictionary in self.astronauts:
            if name in dictionary['name']:
                self.astronauts.remove(dictionary)
                return self.astronauts
            else:
                return None


space_station = SpaceStation()

print(space_station.add_astronaut('Joseph M. Acab', 'USA', 12))
print(space_station.add_astronaut('Vladimir Aksyonov', 'China', 7))
print(space_station.find_astronaut('Vladimir Aksyonov'))

print(SpaceStation.from_astronaut_list(space_station.astronauts))

print(SpaceStation.is_long_term_mission({'name': 'Joseph M. Acab', 'nationality': 'USA', 'mission_duration': 12}))

print(space_station.remove_astronaut('Joseph'))

