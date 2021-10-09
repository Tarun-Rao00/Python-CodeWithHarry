num = int(input("Enter a number: "))
a = 1
i = 1
for i in range(num):
    print("  "*(num - i) + "* "*a)
    a = a+2
    i = i+1