class Vehicle:
    def __init__(self, name, model, year, speed):
        self.name = name
        self.model = model
        self.year = year
        self.speed = speed

    def describe(self):
        print(f"Car driven is {self.name} of model {self.model}.Licence expires by {self.year}.Max speed {self.speed}")


carMazda = Vehicle("mazda", "2015", "2015", "300")
carMazda.describe()
