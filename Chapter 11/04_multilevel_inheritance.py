class Person:
    country = "India"
    
    def takeBreath(self):
        print("I am breathing... ")

class Employee(Person):
    company = "Honda"

    def getSalary(self, salary):
        self.salary = salary
        print(f"Salary is {self.salary} Crore per annum")

    def takeBreath(self):
        print("I am an employee so I am luckily breathing... ")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No slary to programmers")

    def takeBreath(self):
        print("I am a programmer, I am breathing++...")


p = Person()
p.takeBreath()
print(p.country, "\n*****************")

e = Employee()
e.getSalary(1)
e.takeBreath()
print(e.company, "\n****************")

pr = Programmer()
print(pr.country)
pr.getSalary()
pr.takeBreath()
print(pr.company, "\n***************")


    