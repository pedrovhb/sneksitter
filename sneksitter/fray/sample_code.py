import math

for i in range(10):
    print(math.sqrt(i))

# Simple expression
foo = 2 + 4

# Function call
bar = foo(2)


# Function definition
def foo(x):
    return x + 2


# Class definition
class Foo:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        return self.x + y


# Simple module
from math import sqrt


def take_square_root(x):
    return sqrt(x)


class Calculator:
    def __init__(self, x):
        self.x = x

    @cache
    def square_root(self):
        return sqrt(self.x)


if __name__ == "__main__":
    print(take_square_root(4))
    print(Calculator(4).square_root())


# Closure
def make_adder(x):
    def add(y):
        return x + y

    return add


# Decorator
def cache(fn):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return wrapper


@cache
def square(x):
    return x * x


# Generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
