class Vechile:
    def display_Vechile(self):
        print("It is a vechile")

class Car(Vechile):
    def display_car(self):
        print("It is a car")

class Bike(Vechile):
    def display_bike(self):
        print("It is a Bike")


class ElectricCar(Car):
    def display_electricvechile(self):
        print("It is a electric vechile")

bike=Bike()
bike.display_bike()
bike.display_Vechile()

print("\n")

car=Car()
car.display_car()
car.display_Vechile()

print("\n")

electricCar=ElectricCar()
electricCar.display_electricvechile()
electricCar.display_car()
electricCar.display_Vechile()

