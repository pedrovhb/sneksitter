from math import sqrt


class Calculator:
    def __init__(self, x: int) -> None:
        self.x = x

    def square_root(self) -> float:
        return sqrt(self.x)

    def cube(self) -> int:
        return self.x**3


if __name__ == "__main__":
    calc = Calculator(144)
    print(calc.square_root())
