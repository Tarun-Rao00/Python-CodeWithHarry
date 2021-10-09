marks = int(input("Enter Your Marks: "))
 
if(marks in range(90,100) or marks==100):
    print("Excellent")
elif(marks in range(80,90)):
    print("A")
elif(marks in range(70,80)):
    print("B")
elif(marks in range(60,70)):
    print("C")
elif(marks in range(50,60)):
    print("D")
else:
    print("F") 
