a = int(input("Enter Marks of Subject 1: "))
b = int(input("Enter Marks of Subject 2: "))
c = int(input("Enter Marks of Subject 3: "))

x = 100 #Assume maximum marks to be 100
t = (a+b+c)/3

if (a>=33 and b>=33 and c>=33):
    if(t>=40):
        print("PASS!")
else:
    print("FAIL!")