class Vehicle:
    fuelCap = 90

    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    fuelCap = 50

    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        super().printDetails()
        print("Doors:", self.doors)
        self.printDetails()

    def printDetails(self):
        print("child fuelCap : ", self.fuelCap)
        print("parent fuelCap:", super().fuelCap)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
# obj1.printDetails()
