class Car:
    def move(self):
        print("It moves on road")
        return ("It moves on road")

class Areoplane:
    def move(self):
        print("It flies in air")
        return ("It flies in air")

class Flying_Car(Car,Areoplane):
    def move(self):
        print(f"{Car.move(self)} and {Areoplane.move(self)}")


obj=Flying_Car()
obj.move()