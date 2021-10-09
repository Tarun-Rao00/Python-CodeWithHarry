num = int(input("Enter a number: "))


print("* "*num)
for i in range(num-2):
    print("* " + "  "*(num-2) + "*")

if num!=1:
    print("* "*num)
