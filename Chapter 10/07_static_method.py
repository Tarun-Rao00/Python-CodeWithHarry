import time

class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary of the employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")




harry = Employee()

harry.greet()
harry.salary = 100000
harry.getSalary("Thanks")

