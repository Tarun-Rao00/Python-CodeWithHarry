class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"

    def getLang(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e = Employee()
e.showDetails()
p = Programmer()
print(p.company)
p.getLang()
p.showDetails()
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"

    def getLang(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e = Employee()
e.showDetails()
p = Programmer()
print(p.company)
p.getLang()
p.showDetails()
