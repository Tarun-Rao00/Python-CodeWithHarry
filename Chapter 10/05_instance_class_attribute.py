class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salry for both the objects
harry.salary = 300
rajni.salary = 400

print(harry.salary)
print(rajni.salary)