class Person:
    country = "India"
    
    def __init__(self):
        print("Initializing Person..\n")

    def takeBreath(self):
        print("I am breathing... ")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")


    def getSalary(self, salary):
        self.salary = salary
        print(f"Salary is {self.salary} Crore per annum")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so I am luckily breathing... ")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to programmers")
    
  


    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer, I am breathing++...")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()



    