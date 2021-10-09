num = int(input("Enter a number: "))


print("* "*num)
for i in range(num-2):
    print("* " + "* "*(i+1) + "  "*(num-i-3) + "*")

if num!=1:
    print("* "*num)
