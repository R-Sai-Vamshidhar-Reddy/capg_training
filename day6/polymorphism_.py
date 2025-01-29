#poly means many and polymorphism means many forms
class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")
for ani in [Cat(),Dog()]:
    ani.sound()