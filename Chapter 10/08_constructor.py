class Employee:
    company = "Google"
    
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
        

    def getDetails(self):
        print(f"The name of the employee is: {self.name}")
        print(f"The salary of {self.name} is: {self.salary}")
        print(f"The subunit of {self.name} is: {self.subunit}")
      

    @staticmethod
    def greet():
        print("Good Morning, Sir")




harry = Employee("Harry", 100000, "Junior Engineer")
harry.getDetails()


# harry.greet()
# harry.salary = 100000
# harry.getSalary("Thanks")

