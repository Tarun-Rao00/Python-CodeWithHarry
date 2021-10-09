num = int(input("Enter a number: "))
i = 1
pro = num
while pro<=num*10:
    print(f"{num} X {i} = {pro}")
    i = i+1
    pro = num*(i)