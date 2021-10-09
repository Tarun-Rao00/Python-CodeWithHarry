def add(n):
    if n==0:
        output = 0
    else:
        output = add(n-1) + n
    return output


n = int(input("Enter a number: "))
print(add(n))