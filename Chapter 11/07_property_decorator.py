class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 400
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary
     
        


e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salaryBonus)


