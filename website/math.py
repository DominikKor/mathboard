from itertools import islice, count
from math import sqrt


class Number:
    def __init__(self, number):
        self.number: int = number
        self.is_prime: bool = is_prime(number)
        self.divisors: list = get_divisors(number)

    def __repr__(self):
        return self.number

    def __str__(self):
        return str(self.number)

    def __len__(self):
        return len(str(self.number))


def is_prime(num):
    if num < 2:
        return False
    for number in islice(count(2), int(sqrt(num) - 1)):
        if num % number == 0:
            return False
    return True


def get_divisors(num):
    div_numbers = []
    for number in range(2, int(num / 2 + 1)):
        if num % number == 0:
            div_numbers.append(number)
    div_numbers.reverse()
    return div_numbers
