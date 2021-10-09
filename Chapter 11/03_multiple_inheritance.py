class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 2

    def upGradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upGradeLevel()
print(p.level)
print(p.company)