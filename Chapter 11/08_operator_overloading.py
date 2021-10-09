class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num


n1 = Number(int(input("Enter a number: ")))
n2 = Number(int(input("Enter second number: ")))
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)