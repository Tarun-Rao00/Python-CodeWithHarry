def pat(n):
    for i in range(n):
        print("* "*(n-i))
    
n = int(input("Enter a number: "))
pat(n)
