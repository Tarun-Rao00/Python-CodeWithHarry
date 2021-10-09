# name = input("Enter Your Name: ")
# date = input("Date: ")

# print("Dear", name,  "\nYou are Selected!\n",date)
name = input("Enter Your Name: ")
date = input("Please Enter Date (DD Month YYYY): ")

temp = '''Dear Name,\n\tYou Are Selected!\n\tDate: DATE'''

temp = temp.replace("Name", name)
temp = temp.replace("DATE", date)

# temp_new = temp
print(temp)