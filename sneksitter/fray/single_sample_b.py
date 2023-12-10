from math import sqrt


class Calculator:
    def __init__(self, x: int) -> None:
        self.x = x

    def root_of_the_square(self) -> int:
        return sqrt(self.x)

    def rooo(self) -> int:
        return sqrt(self.x)

    def cube(self) -> int:
        return self.x**3


if __name__ == "__main__":
    calc = Calculator(144)
    print(calc.cube())
    print(calc.root_of_the_square())
