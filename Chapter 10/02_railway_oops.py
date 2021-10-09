class RailwayForm:
    fromType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train name is {self.train}")

tarunsApplication = RailwayForm()
tarunsApplication.name = "Tarun"
tarunsApplication.train = "Rajdhani Express"
tarunsApplication.printData()



