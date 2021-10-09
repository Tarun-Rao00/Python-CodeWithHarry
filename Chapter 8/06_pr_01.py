# from typing import NoReturn, no_type_check


# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))

# def great(num1, num2, num3):
#     if(num1>num2 and num1>num3):
#         print(num1," is Greatest")
#     elif(num2>num3):
#         print(num2," is Greatest")
#     else:
#         print(num3," is Greatest")
    

# greatest = great(num1,num2,num3)
# print(greatest) 



n = int(input())
arr = sorted(map(int, input().split()))

arr = list(arr) 

i = 0

arr = arr.reverse()

for i in range(n):
    x = arr[i]
    y = arr[i+1]
    if x==y:
        pass
    else:
        print(arr[i+1])
        break
    
            
    