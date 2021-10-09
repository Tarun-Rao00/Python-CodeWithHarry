import cmath
from math import sqrt

class Calculator:
    @staticmethod
    def greet():
        print(f"Hello, Tarun")


    def __init__(self, num):
        self.num = num
        print(f"Square of {self.num} is {num*num}")
        print(f"Cube of {self.num} is {num*num*num}")
        print(f"Square root of {self.num} is {sqrt(float(self.num))}")
    


num = int(input("Enter a number: "))

num1 = Calculator(num)
num1.greet()


# num1.square(num)
# num1.cube(num)
# num1.squareRoot(num)
