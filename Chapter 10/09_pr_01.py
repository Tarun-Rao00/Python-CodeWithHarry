class Programmer:
    company = "Microsoft"
    def __init__(self, name, product, salary):
        self.name = name
        self.product = product
        self.salary = salary

    def getInfo(self):
        print(f"The name of the programmer is {self.name}\nWorks at {self.product}\nSalary is {self.salary}\n")

        with open("Programmer.txt",'a') as f:
            f.write(f"Name: {self.name}\nProduct: {self.product}\nSalary: {self.salary}\n\n")



tarun = Programmer("Tarun", "Azure", 10000000)
dushyant = Programmer("Dushyant", "Skype", 10000000)
vinayak = Programmer("Vinayak", "Edge", 10000000)
tarun.getInfo()
dushyant.getInfo()
vinayak.getInfo()

