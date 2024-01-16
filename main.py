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
